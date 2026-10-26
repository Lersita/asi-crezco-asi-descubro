// Uso: node maqueta/pdf.js maqueta/libro1.html salida.pdf
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.resolve(process.argv[2]), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: process.argv[3], width: '432mm', height: '216mm', printBackground: true });
  await b.close();
})();
