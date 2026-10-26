// Genera las plantillas del PDF personalizado a partir de las maquetas.
// Uso (desde la raíz del repositorio): node web/herramientas/plantillas.js
// Saca una imagen por doble, sin el título de tapa ni el texto con el nombre,
// y guarda dónde iban esos textos en web/plantillas/<libro>/medidas.json.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const RAIZ = path.resolve(__dirname, '..', '..');
const LIBROS = [
  { id: 'libro1-varon', html: 'maqueta/libro1.html' },
  { id: 'libro1-mujer', html: 'maqueta/libro1-emi.html' },
  { id: 'libro2-varon', html: 'maqueta/libro2.html' },
  { id: 'libro2-mujer', html: 'maqueta/libro2-emi.html' },
];
(async () => {
  const b = await chromium.launch();
  for (const L of LIBROS) {
    const out = path.join(RAIZ, 'web', 'plantillas', L.id); fs.mkdirSync(out, { recursive: true });
    // 432 mm = 1632,76 px a 96 ppp; con escala 1,47 cada doble sale de unos 2.400 px de ancho
    const p = await b.newPage({ viewport: { width: 1640, height: 820 }, deviceScaleFactor: 1.47 });
    await p.goto('file://' + path.join(RAIZ, L.html), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const medidas = await p.evaluate(() => {
      const mm = px => +(px * 25.4 / 96).toFixed(2);
      const sec = [...document.querySelectorAll('section.spread')];
      const caja = (el, s) => { const r = el.getBoundingClientRect(), o = s.getBoundingClientRect(); return { x: mm(r.left - o.left), y: mm(r.top - o.top), w: mm(r.width), h: mm(r.height) }; };
      const h1 = sec[0].querySelector('h1'), t = sec[1].querySelector('.txt');
      const res = { titulo: caja(h1, sec[0]), titulo_texto: h1.innerText, nombre: caja(t, sec[1]), nombre_texto: t.innerText,
                    nombre_maximo: mm(parseFloat(getComputedStyle(t).width)), nombre_estilo: t.getAttribute('style'), dobles: sec.length };
      h1.style.visibility = 'hidden'; t.style.visibility = 'hidden';
      return res;
    });
    const secs = await p.$$('section.spread');
    for (let i = 0; i < secs.length; i++) {
      await secs[i].screenshot({ path: path.join(out, `d${String(i).padStart(2, '0')}.jpg`), type: 'jpeg', quality: 84 });
    }
    fs.writeFileSync(path.join(out, 'medidas.json'), JSON.stringify(medidas, null, 2));
    console.log(L.id, medidas.dobles, 'dobles', JSON.stringify(medidas.titulo), JSON.stringify(medidas.nombre), medidas.nombre_estilo);
    await p.close();
  }
  await b.close();
})();
