// Saca una imagen de cada página del interior de KDP tal como se ve en pantalla, a 400 dpi exactos
// (3450 × 3500 píxeles). No usa el modo de impresión del navegador, que achicaba el contenido.
// Uso: node maqueta/kdp_capturas.js maqueta/kdp-libro1-en.html carpeta_salida
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const [, , entrada, carpeta] = process.argv;
  fs.mkdirSync(carpeta, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 828, height: 840 }, deviceScaleFactor: 3450 / 828 });
  await p.goto('file://' + path.resolve(entrada), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const paginas = await p.$$('.kpage');
  for (let i = 0; i < paginas.length; i++) {
    await paginas[i].screenshot({ path: path.join(carpeta, `p${String(i + 1).padStart(2, '0')}.png`) });
  }
  console.log(paginas.length, 'páginas');
  await b.close();
})();
