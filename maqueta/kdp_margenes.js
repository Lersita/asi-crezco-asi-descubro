// Revisa que ningún texto quede fuera de los márgenes de KDP (con sangrado):
// 0,375 in desde el refile en los bordes de afuera, arriba y abajo; 0,375 in en el margen interior (pliegue).
// Uso: node maqueta/kdp_margenes.js maqueta/kdp-libro1-en.html
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1000, height: 1000 } });
  await p.goto('file://' + path.resolve(process.argv[2]), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const problemas = await p.evaluate(() => {
    const MM = 96 / 25.4, SANG = 3.175, MARGEN = 9.525, W = 219.075, H = 222.25;
    const out = [];
    [...document.querySelectorAll('.kpage')].forEach((pg, i) => {
      const n = i + 1, izq = n % 2 === 0;           // páginas pares a la izquierda
      const r0 = pg.getBoundingClientRect();
      const walker = document.createTreeWalker(pg, NodeFilter.SHOW_TEXT);
      let t;
      while ((t = walker.nextNode())) {
        if (!t.textContent.trim()) continue;
        const rg = document.createRange(); rg.selectNodeContents(t);
        for (const r of rg.getClientRects()) {
          if (r.width < 1) continue;
          const x1 = (r.left - r0.left) / MM, x2 = (r.right - r0.left) / MM, y1 = (r.top - r0.top) / MM, y2 = (r.bottom - r0.top) / MM;
          if (x2 < 0 || x1 > W || y2 < 0 || y1 > H) continue;   // fuera de la página: no se imprime
          const minX = izq ? SANG + MARGEN : MARGEN, maxX = izq ? W - MARGEN : W - SANG - MARGEN;
          const malo = x1 < minX - 0.2 || x2 > maxX + 0.2 || y1 < SANG + MARGEN - 0.2 || y2 > H - SANG - MARGEN + 0.2;
          if (malo) out.push(`página ${n}: "${t.textContent.trim().slice(0, 40)}" x ${x1.toFixed(1)}–${x2.toFixed(1)} y ${y1.toFixed(1)}–${y2.toFixed(1)} mm`);
        }
      }
    });
    return out;
  });
  console.log(path.basename(process.argv[2]), problemas.length ? '\n  ' + problemas.join('\n  ') : 'OK');
  await b.close();
})();
