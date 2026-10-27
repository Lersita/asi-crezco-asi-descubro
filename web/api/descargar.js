// GET /api/descargar?payment_id=...&ref=...&libro=libro1
// Si el pago está aprobado y el libro es parte de la compra, arma el PDF y lo entrega.
const { pagoVerificado, titulo, sinTildes, responderError } = require('./_comun');
const { generarLibro } = require('./_pdf');

module.exports = async (req, res) => {
  try {
    const { pedido, aprobado } = await pagoVerificado(req.query.payment_id, req.query.ref);
    if (!aprobado) return res.status(402).json({ error: 'El pago todavía no está aprobado. Probá de nuevo en unos minutos.' });
    const libro = String(req.query.libro || '');
    if (!pedido.libros.includes(libro)) return res.status(403).json({ error: 'Ese libro no es parte de esta compra.' });
    const bytes = await generarLibro({ libro, genero: pedido.genero, nombre: pedido.nombre });
    const nombre = `${titulo(libro, pedido.nombre)}.pdf`;
    res.setHeader('Content-Type', 'application/pdf');
    res.setHeader('Content-Disposition', `attachment; filename="${sinTildes(nombre).replace(/[^\w .-]/g, '')}"; filename*=UTF-8''${encodeURIComponent(nombre)}`);
    res.setHeader('Cache-Control', 'private, no-store');
    res.status(200).send(Buffer.from(bytes));
  } catch (e) { responderError(res, e); }
};
