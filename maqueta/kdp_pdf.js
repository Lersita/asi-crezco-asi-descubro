// PDF para Amazon KDP: páginas de 8,625 × 8,75 pulgadas (8,5 × 8,5 con sangrado).
// Uso: node maqueta/kdp_pdf.js maqueta/kdp-libro1-es.html salida.pdf [ancho alto, por ejemplo 17.306in 8.75in]
// Para la tapa se pasan las medidas de la tapa completa.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [, , entrada, salida, w = '8.625in', h = '8.75in'] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.resolve(entrada), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: salida, width: w, height: h, printBackground: true, preferCSSPageSize: false });
  await b.close();
})();
