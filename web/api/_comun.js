// Piezas que comparten las funciones del servidor.
// Los archivos de api/ que empiezan con "_" no se publican como direcciones.
const crypto = require('crypto');
const PRECIOS = require('../precios.json');

const GENEROS = ['mujer', 'varon'];
const MP = 'https://api.mercadopago.com';

// Mismas reglas que la web: letras, espacios, apóstrofo y guion; hasta 14; primera en mayúscula
function limpiarNombre(v) {
  v = String(v || '').replace(/[^A-Za-zÁÉÍÓÚÜÑáéíóúüñ' -]/g, '').replace(/\s+/g, ' ').trim().slice(0, 14);
  return v ? v.charAt(0).toUpperCase() + v.slice(1) : '';
}

// Valida lo que pide la web y devuelve el pedido con el precio que manda el servidor
const invalido = m => Object.assign(new Error(m), { status: 400 });
function armarPedido({ libros, genero, nombre }) {
  if (!Array.isArray(libros) || !libros.length) throw invalido('Elegí al menos un libro.');
  libros = [...new Set(libros)];
  for (const l of libros) {
    if (!PRECIOS.libros[l] || !PRECIOS.libros[l].disponible) throw invalido('Ese libro todavía no está disponible.');
  }
  if (!GENEROS.includes(genero)) throw invalido('Elegí mujer o varón.');
  nombre = limpiarNombre(nombre);
  if (!nombre) throw invalido('Escribí el nombre para la tapa.');
  const pack = PRECIOS.packs.find(p => p.cantidad === libros.length && p.disponible);
  if (!pack) throw invalido('Esa cantidad de libros todavía no se puede comprar.');
  libros.sort();
  return { libros, genero, nombre, precio: pack.precio };
}

// El pedido viaja dentro del pago, en external_reference (máximo 256 caracteres):
// clave.libros.genero.nombre — la clave al azar evita que alguien adivine el link de otra compra
function codificar(p) {
  const clave = crypto.randomBytes(9).toString('base64url');
  return [clave, p.libros.join('-'), p.genero, Buffer.from(p.nombre, 'utf8').toString('base64url')].join('.');
}
function decodificar(ref) {
  const [clave, libros, genero, nombre64] = String(ref || '').split('.');
  if (!clave || !libros || !genero || !nombre64) return null;
  return { libros: libros.split('-'), genero, nombre: Buffer.from(nombre64, 'base64url').toString('utf8') };
}

async function mp(ruta, opciones = {}) {
  const token = String(process.env.MP_ACCESS_TOKEN || '').trim();
  if (!token) throw new Error('Falta configurar el pago (MP_ACCESS_TOKEN en Vercel).');
  const r = await fetch(MP + ruta, {
    ...opciones,
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json', ...(opciones.headers || {}) },
  });
  const datos = await r.json().catch(() => ({}));
  if (!r.ok) { const e = new Error(datos.message || `Mercado Pago respondió ${r.status}`); e.status = r.status; throw e; }
  return datos;
}

// Busca el pago y confirma que corresponde a esta compra
async function pagoVerificado(paymentId, ref) {
  if (!/^\d+$/.test(String(paymentId || ''))) throw Object.assign(new Error('Falta el número de pago.'), { status: 400 });
  const pago = await mp(`/v1/payments/${paymentId}`);
  if (!ref || pago.external_reference !== ref) throw Object.assign(new Error('Ese link no corresponde a esta compra.'), { status: 403 });
  const pedido = decodificar(pago.external_reference);
  if (!pedido) throw Object.assign(new Error('No se encontró el pedido de este pago.'), { status: 404 });
  const pack = PRECIOS.packs.find(p => p.cantidad === pedido.libros.length);
  const pagado = Number(pago.transaction_amount || 0);
  const aprobado = pago.status === 'approved' && pago.currency_id === 'ARS' && pack && pagado >= pack.precio;
  return { pago, pedido, aprobado };
}

const titulo = (libro, nombre) => `${nombre} ${PRECIOS.libros[libro].titulo}`;
const sinTildes = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '');
function responderError(res, e) {
  res.status(e.status && e.status < 500 ? e.status : 500).json({ error: e.message || 'Algo salió mal. Probá de nuevo en un rato.' });
}

module.exports = { PRECIOS, limpiarNombre, armarPedido, codificar, decodificar, mp, pagoVerificado, titulo, sinTildes, responderError };
