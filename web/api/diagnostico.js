// TEMPORAL: muestra si la credencial de Mercado Pago está bien cargada, sin mostrar su valor.
module.exports = async (req, res) => {
  const t = process.env.MP_ACCESS_TOKEN || '';
  const info = { cargada: !!t, empieza_con: t.slice(0, 8), largo: t.length, tiene_espacios_o_comillas: /[\s"']/.test(t),
    parece: /^(APP_USR|TEST)-\d{6,}-\d{6}-[0-9a-f]{32}-\d+$/.test(t.trim()) ? 'Access Token' : /^(APP_USR|TEST)-[0-9a-f-]{36}$/.test(t.trim()) ? 'Public Key (no sirve acá)' : 'formato desconocido' };
  try {
    const r = await fetch('https://api.mercadopago.com/users/me', { headers: { Authorization: `Bearer ${t.trim()}` } });
    const d = await r.json();
    info.mercado_pago = r.ok ? { reconoce_la_cuenta: true, pais: d.site_id, es_usuario_de_prueba: /^TEST/i.test(d.nickname || '') || (d.tags || []).includes('test_user') } : { reconoce_la_cuenta: false, respuesta: d.message || r.status };
  } catch (e) { info.mercado_pago = { error: e.message }; }
  res.setHeader('Cache-Control', 'no-store'); res.status(200).json(info);
};
