// POST /api/crear-pago  { libros: ["libro1"], genero: "mujer", nombre: "Sofía" }
// Arma el cobro en Mercado Pago (Checkout Pro) y devuelve el link de pago.
const { armarPedido, codificar, mp, titulo, responderError } = require('./_comun');

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Usá POST.' });
  try {
    const pedido = armarPedido(req.body || {});
    const ref = codificar(pedido);
    const base = `https://${req.headers['x-forwarded-host'] || req.headers.host}`;
    const nombres = pedido.libros.map(l => `“${titulo(l, pedido.nombre)}”`).join(' y ');
    const preferencia = await mp('/checkout/preferences', {
      method: 'POST',
      body: JSON.stringify({
        items: [{
          id: `libros-${pedido.libros.join('-')}`,
          title: pedido.libros.length === 1 ? `Libro personalizado ${nombres}` : `${pedido.libros.length} libros personalizados de ${pedido.nombre}`,
          description: `PDF para imprimir: ${nombres}`,
          category_id: 'learnings',
          quantity: 1,
          currency_id: 'ARS',
          unit_price: pedido.precio,
        }],
        external_reference: ref,
        back_urls: { success: `${base}/gracias`, pending: `${base}/gracias`, failure: `${base}/gracias` },
        auto_return: 'approved',
        statement_descriptor: 'ASI CREZCO',
      }),
    });
    const prueba = String(process.env.MP_ACCESS_TOKEN || '').trim().startsWith('TEST-');
    res.status(200).json({ link: prueba ? preferencia.sandbox_init_point : preferencia.init_point });
  } catch (e) { responderError(res, e); }
};
