// GET /api/pedido?payment_id=...&ref=...
// Le pregunta a Mercado Pago cómo está el pago y devuelve qué libros se pueden descargar.
const { pagoVerificado, titulo, responderError } = require('./_comun');

module.exports = async (req, res) => {
  try {
    const { pago, pedido, aprobado } = await pagoVerificado(req.query.payment_id, req.query.ref);
    res.setHeader('Cache-Control', 'no-store');
    res.status(200).json({
      estado: aprobado ? 'aprobado' : pago.status === 'rejected' || pago.status === 'cancelled' ? 'rechazado' : 'pendiente',
      nombre: pedido.nombre,
      genero: pedido.genero,
      libros: pedido.libros.map(l => ({ id: l, titulo: titulo(l, pedido.nombre) })),
    });
  } catch (e) { responderError(res, e); }
};
