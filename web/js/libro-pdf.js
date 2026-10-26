// Arma el PDF personalizado en el navegador, con pdf-lib.
// Usa las plantillas de web/plantillas/<libro>-<genero>/ (una imagen por doble,
// sin el título de tapa ni el texto con el nombre) y escribe esos dos textos.
// Sale un PDF de 24 páginas cuadradas de 21,6 cm, en el orden del libro.
(function () {
  const MM = 72 / 25.4;              // puntos por milímetro
  const LADO = 216;                  // una página: 216 × 216 mm
  const TINTA = [35 / 255, 48 / 255, 74 / 255];
  // Métricas verticales de las tipografías (iguales en hhea y OS/2)
  const ANDIKA = { asc: 2500 / 2048, desc: 800 / 2048 };
  const FRAUNCES = { asc: 1956 / 2000, desc: 510 / 2000 };

  const LIBROS = {
    libro1: {
      titulo2: 'a girar',
      generos: ['varon', 'mujer'],
      nombreTexto: (n, g) => `Me llamo ${n}. Soy ${g('chiquito', 'chiquita')}, muy ${g('chiquito', 'chiquita')}.`,
    },
    libro2: {
      titulo2: 'a sentarse',
      generos: ['varon'],
      nombreTexto: n => `Soy ${n}. Ya sé girar: boca arriba, boca abajo.`,
    },
  };

  // Etiqueta de papel cortado: mismos puntos que el clip-path de la maqueta (en %)
  const ETIQUETA = [[0.8, 6], [18, 1.5], [41, 3.5], [63, 0.5], [86, 3], [99.4, 0], [98.6, 34], [100, 68], [98.8, 97], [77, 99.2], [52, 96.8], [29, 100], [6, 97.5], [0, 99], [1.2, 62], [0, 30]];

  function cortarLineas(texto, fuente, tam, ancho) {
    const palabras = texto.split(' '), lineas = [];
    let actual = '';
    for (const p of palabras) {
      const prueba = actual ? actual + ' ' + p : p;
      if (actual && fuente.widthOfTextAtSize(prueba, tam) > ancho) { lineas.push(actual); actual = p; }
      else actual = prueba;
    }
    if (actual) lineas.push(actual);
    return lineas;
  }
  // Distancia desde el borde superior de una línea hasta su línea de base, como la calcula el navegador
  const base = (m, tam, alto) => (alto - (m.asc + m.desc) * tam) / 2 + m.asc * tam;

  async function traer(url) {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`No se pudo cargar ${url} (${r.status}). Revisá la conexión y probá de nuevo.`);
    return r;
  }

  async function generarLibro({ libro, genero, nombre, alAvanzar }) {
    const L = LIBROS[libro];
    if (!L) throw new Error('Ese libro todavía no está disponible.');
    if (!L.generos.includes(genero)) throw new Error('Este libro todavía no tiene versión mujer. Elegí varón o el libro 1.');
    const { PDFDocument, rgb } = window.PDFLib;
    const carpeta = `plantillas/${libro}-${genero}/`;
    const G = (o, a) => (genero === 'mujer' ? a : o);
    const avisar = (h, t) => alAvanzar && alAvanzar(h, t);

    const medidas = await (await traer(carpeta + 'medidas.json')).json();
    const doc = await PDFDocument.create();
    doc.registerFontkit(window.fontkit);
    const [andikaB, frauncesB] = await Promise.all([
      traer('fuentes/Andika-Regular.ttf').then(r => r.arrayBuffer()),
      traer('fuentes/Fraunces-ExtraBold.ttf').then(r => r.arrayBuffer()),
    ]);
    const andika = await doc.embedFont(andikaB, { subset: true });
    const fraunces = await doc.embedFont(frauncesB, { subset: true });
    doc.setTitle(`${nombre} aprende ${L.titulo2}`);
    doc.setAuthor('Así crezco, así descubro');
    doc.setLanguage('es-AR');

    const P = LADO * MM;
    const nueva = () => doc.addPage([P, P]);
    // Dibuja la mitad izquierda o derecha de una doble en una página
    const mitad = (pag, img, lado) => pag.drawImage(img, { x: lado === 'der' ? -P : 0, y: 0, width: 2 * P, height: P });

    const total = medidas.dobles;
    let hechas = 0;
    for (let i = 0; i < total; i++) {
      const bytes = await (await traer(carpeta + `d${String(i).padStart(2, '0')}.jpg`)).arrayBuffer();
      const img = await doc.embedJpg(bytes);
      if (i === 0) {                       // tapa interior: solo la mitad derecha
        const pag = nueva(); mitad(pag, img, 'der');
        dibujarTitulo(pag, medidas.titulo, fraunces, [`${nombre} aprende`, L.titulo2]);
      } else if (i === total - 1) {        // "Para los grandes": solo la mitad izquierda
        mitad(nueva(), img, 'izq');
      } else {
        const izq = nueva(); mitad(izq, img, 'izq');
        const der = nueva(); mitad(der, img, 'der');
        if (i === 1) dibujarEtiqueta(medidas.nombre.x >= LADO ? der : izq, medidas.nombre, andika, L.nombreTexto(nombre, G), rgb);
      }
      avisar(++hechas, total);
    }
    return doc.save();
  }

  function dibujarTitulo(pag, caja, fuente, lineas) {
    // La caja está en milímetros de la doble; la tapa es la página derecha
    const x = (caja.x - LADO) * MM, arriba = caja.y * MM;
    const limite = 150 * MM;             // deja libre la insignia de la esquina
    let tam = 60;
    while (tam > 30 && Math.max(...lineas.map(l => fuente.widthOfTextAtSize(l, tam))) > limite) tam -= 1;
    const alto = tam;                    // interlineado 1, como en la maqueta
    lineas.forEach((l, k) => {
      const y = LADO * MM - (arriba + k * alto + base(FRAUNCES, tam, alto));
      pag.drawText(l, { x, y, size: tam, font: fuente, color: window.PDFLib.rgb(...TINTA) });
    });
  }

  function dibujarEtiqueta(pag, caja, fuente, texto, rgb) {
    const tam = 22, alto = tam * 1.27;
    const padX = 7 * MM, padArriba = 4.5 * MM, padAbajo = 5 * MM;
    const x0 = (caja.x >= LADO ? caja.x - LADO : caja.x) * MM, y0 = caja.y * MM, w = caja.w * MM;
    const lineas = cortarLineas(texto, fuente, tam, w - 2 * padX);
    const h = padArriba + padAbajo + lineas.length * alto;
    const H = LADO * MM;
    const camino = ETIQUETA.map(([px, py], k) => `${k ? 'L' : 'M'} ${(px / 100 * w).toFixed(2)} ${(py / 100 * h).toFixed(2)}`).join(' ') + ' Z';
    // Sombra suave en dos capas y después el papel
    pag.drawSvgPath(camino, { x: x0, y: H - y0 - 0.9 * MM, color: rgb(70 / 255, 45 / 255, 20 / 255), opacity: 0.08 });
    pag.drawSvgPath(camino, { x: x0, y: H - y0 - 0.45 * MM, color: rgb(70 / 255, 45 / 255, 20 / 255), opacity: 0.14 });
    pag.drawSvgPath(camino, { x: x0, y: H - y0, color: rgb(1, 248 / 255, 232 / 255) });
    lineas.forEach((l, k) => {
      const y = H - (y0 + padArriba + k * alto + base(ANDIKA, tam, alto));
      pag.drawText(l, { x: x0 + padX, y, size: tam, font: fuente, color: rgb(...TINTA) });
    });
  }

  window.LibroPDF = { generarLibro, LIBROS };
})();
