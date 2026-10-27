#!/usr/bin/env python3
"""Interior de los libros para Amazon KDP (tapa blanda, 8,5 × 8,5 pulgadas, con sangrado).
Parte de la maqueta de la versión Tomi (maqueta/libroN.html), cambia los textos a español neutro
o inglés (maqueta/kdp_textos.py), saca las etiquetas de borrador y los números de página,
deja los textos dentro de los márgenes de KDP y parte cada doble en dos páginas con sangrado.

Uso: python3 maqueta/kdp.py N es|en  → maqueta/kdp-libroN-es.html
     (después: node maqueta/kdp_pdf.js maqueta/kdp-libroN-es.html salida.pdf)
Si existe maqueta/img-kdp/<imagen>.jpg (ilustración ampliada para imprenta), se usa esa."""
import re, sys, html
from pathlib import Path
from kdp_textos import COMUNES, PALABRAS, TITULOS, LIBROS

AQUI = Path(__file__).resolve().parent
COLS = ["#D9452B", "#EE8A2A", "#E9B21C", "#5E9E44", "#4FA3D9", "#8A5CB8"]
SANGRADO = 3.175            # 0,125 pulgadas, en mm
REFILE = 215.9              # 8,5 pulgadas
PAG_W, PAG_H = REFILE + SANGRADO, REFILE + 2 * SANGRADO   # página con sangrado: 219,075 × 222,25 mm
ESCALA = PAG_H / 216        # la maqueta mide 432 × 216 mm por doble

# Ajustes de posición solo para KDP (márgenes más estrictos que la maqueta de la web)
AJUSTES = {
    1: [('<div class="txt" style="left:300mm;top:188mm;', '<div class="txt" style="left:300mm;top:172mm;')],
    2: [('<div class="palabra" style="left:150mm;top:64mm;', '<div class="palabra" style="left:136mm;top:64mm;')],
}

LEGAL = {
    "es": "© 2026 LERSA. Todos los derechos reservados. Ilustraciones creadas con ayuda de inteligencia artificial.",
    "en": "© 2026 LERSA. All rights reserved. Illustrations created with the help of AI tools.",
}


def traducir(doc, n, i):
    tabla = {**COMUNES, **LIBROS[n]}
    faltan = []
    t1, t2 = TITULOS[n][i]
    doc = re.sub(r"<h1>[^<]*<br>[^<]*</h1>", f"<h1>{html.escape(t1)}<br>{html.escape(t2)}</h1>", doc)
    doc = re.sub(r"<title>[^<]*</title>", f"<title>{html.escape(t1)} {html.escape(t2)}</title>", doc)
    doc = re.sub(r'<div class="borrador">[^<]*</div>', "", doc)
    tabla.update({t1: (t1, t1), t2: (t2, t2), "by LERSA": ("by LERSA", "by LERSA")})

    def nodo(m):
        crudo = m.group(1)
        texto = html.unescape(crudo).strip()
        if not texto or re.fullmatch(r"[\d\s]+|[A-ZÁÉÍÓÚÑ]", texto):
            return m.group(0)
        if texto in tabla:
            nuevo = html.escape(tabla[texto][i], quote=False)
            pre = crudo[:len(crudo) - len(crudo.lstrip())]
            post = crudo[len(crudo.rstrip()):]
            return ">" + pre + nuevo + post + "<"
        faltan.append(texto)
        return m.group(0)

    cuerpo_ini = doc.index("<body>")
    cuerpo = re.sub(r">([^<>]+)<", nodo, doc[cuerpo_ini:])
    doc = doc[:cuerpo_ini] + cuerpo

    def palabra(m):
        letras = "".join(re.findall(r">(.)</span>", m.group(2)))
        nueva = PALABRAS[letras][i]
        return m.group(1) + "".join(f'<span style="color:{COLS[k % 6]}">{html.escape(c)}</span>' for k, c in enumerate(nueva))
    doc = re.sub(r'(<div class="palabra"[^>]*>)((?:<span style="color:[^"]+">.</span>)+)', palabra, doc)

    return doc, faltan


def correr_textos(doc):
    """Textos de la página derecha: 4 mm más lejos del pliegue (margen interior de KDP)."""
    def mover(m):
        x = float(m.group(2))
        return m.group(1) + (f"{x + 4:g}" if 216 <= x < 240 else m.group(2)) + "mm"
    return re.sub(r'(<div class="txt" style="left:)([\d.]+)mm', mover, doc)


def armar(n, lang):
    i = 0 if lang == "es" else 1
    doc = (AQUI / f"libro{n}.html").read_text(encoding="utf-8")
    doc, faltan = traducir(doc, n, i)
    if faltan:
        raise SystemExit("Faltan traducciones:\n- " + "\n- ".join(faltan))
    for viejo, nuevo in AJUSTES.get(n, []):
        assert viejo in doc, viejo
        doc = doc.replace(viejo, nuevo)
    doc = correr_textos(doc)
    # Ilustraciones ampliadas para imprenta, si existen
    doc = re.sub(r"img/([\w.-]+)\.jpg", lambda m: f"img-kdp/{m.group(1)}.jpg" if (AQUI / "img-kdp" / f"{m.group(1)}.jpg").exists() else m.group(0), doc)

    secciones = re.findall(r'<section class="spread[^"]*">.*?</section>', doc, re.S)
    assert len(secciones) == 13, len(secciones)
    paginas = []
    for k, s in enumerate(secciones):
        lados = ["der"] if k == 0 else ["izq"] if k == 12 else ["izq", "der"]
        for lado in lados:
            x = -SANGRADO if lado == "izq" else -PAG_H
            extra = f'<div class="legal">{html.escape(LEGAL[lang])}</div>' if k == 12 else ""
            paginas.append(f'<div class="kpage"><div class="kspread" style="left:{x:.3f}mm">{s}</div>{extra}</div>')
    assert len(paginas) == 24, len(paginas)

    css = f"""
@page{{size:{PAG_W}mm {PAG_H}mm;margin:0}}
body{{margin:0}}
.kpage{{width:{PAG_W}mm;height:{PAG_H}mm;position:relative;overflow:hidden;page-break-after:always;background:#FFF9E7}}
.kspread{{position:absolute;top:0;width:432mm;height:216mm;transform:scale({ESCALA:.6f});transform-origin:0 0}}
.kspread>section{{page-break-after:auto}}
.folio,.borrador,.fold{{display:none!important}}
.txt{{translate:0 3mm}}
.legal{{position:absolute;left:24mm;right:24mm;bottom:15mm;font:7pt/1.3 Andika,sans-serif;color:#8A7562;text-align:center}}
"""
    doc = doc.replace("</style>", css + "</style>", 1)
    doc = re.sub(r"<body>.*</body>", "<body>" + "".join(paginas) + "</body>", doc, flags=re.S)
    doc = doc.replace('lang="es"', f'lang="{lang}"')
    salida = AQUI / f"kdp-libro{n}-{lang}.html"
    salida.write_text(doc, encoding="utf-8")
    print("ok", salida.name)


if __name__ == "__main__":
    armar(int(sys.argv[1]), sys.argv[2])
