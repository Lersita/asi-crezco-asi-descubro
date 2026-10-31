#!/usr/bin/env python3
"""Recopilatorio de los libros 1 a 4 para Amazon KDP: "Tommy's First Year" / "El primer año de Tommy".
Interior: 2 páginas de presentación + los interiores de KDP de los libros 1 a 4 (24 páginas cada uno) = 98 páginas.
Tapa: un álbum de fotos del primer año (cuatro polaroids de Tomi que suben como una escalera de crecimiento),
armado con las tapas de los cuatro libros, sin ilustraciones nuevas. Lomo para 98 páginas, con texto.

Uso: python3 maqueta/kdp_bundle.py es|en
  → maqueta/kdp-bundle14-<lang>-intro.html y maqueta/kdp-tapa-bundle14-<lang>.html
  Después:
  python3 maqueta/kdp_bundle.py es --pdf   (arma kdp/bundle14-es-interior.pdf con las capturas y los interiores)
  node maqueta/kdp_pdf.js maqueta/kdp-tapa-bundle14-es.html kdp/bundle14-es-tapa.pdf 17.4800in 8.75in"""
import sys, html, subprocess, tempfile, glob
from pathlib import Path
from PIL import Image

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
SANGRADO, REFILE, PAGINAS = 0.125, 8.5, 98
LOMO = PAGINAS * 0.002347
ANCHO = 2 * SANGRADO + 2 * REFILE + LOMO
ALTO = REFILE + 2 * SANGRADO
COLS = ["#D9452B", "#EE8A2A", "#E9B21C", "#5E9E44", "#4FA3D9", "#8A5CB8"]
e = html.escape

# Recortes de Tomi en las tapas ampliadas de cada libro (4096 × 4096)
FOTOS = {
    1: ("img-kdp/p01-portada-v2.jpg", (183, 1207, 2683, 3707)),
    2: ("img-kdp/l2-p01-portada-v1.jpg", (224, 961, 2724, 3461)),
    3: ("img-kdp/l3-p01.jpg", (265, 1125, 2765, 3625)),
    4: ("img-kdp/l4-p01.jpg", (984, 1271, 3684, 3971)),
}

T = {
    "en": {
        "coleccion": "I Grow, I Discover · Books 1–4",
        "t1": "Tommy's", "t2": "First Year",
        "badge": ("4", "books", "in 1"),
        "sub": "4 Books in 1: Roll Over, Sit Up, Crawl, and Stand Up",
        "fotos": [("Roll over", "about 4–6 months"), ("Sit up", "about 6–8 months"),
                  ("Crawl", "about 7–10 months"), ("Stand up", "about 9–12 months")],
        "contra": "Four first milestones, four big discoveries. In his first year, Tommy learns to roll over, sit up, crawl, and stand up. With Rula, his big colorful ball, he discovers why round things roll, how balance works, what friction does, and how gravity pulls everything down. And along the way he counts, compares, and measures: up and down, tall and short, near and far, hands and knees.",
        "serie": "A series that follows a baby's first big milestones, from rolling over to riding a bike, with one physics idea and one math idea in every book. For reading aloud with kids ages 4 to 7.",
        "adentro_t": "Inside",
        "adentro": ["4 complete picture books in one volume", "4 hands-on experiments with things from home", "4 pages for grown-ups: the science, the milestone, and safety tips"],
        "libros": ["Tommy Learns to Roll Over", "Tommy Learns to Sit Up", "Tommy Learns to Crawl", "Tommy Learns to Stand Up"],
        "conceptos": ["Physics: round things roll · Math: up and down, counting 1 to 3",
                      "Physics: balance · Math: tall and short, near and far",
                      "Physics: friction · Math: counting hands and knees",
                      "Physics: gravity, things fall · Math: comparing heights"],
        "contenido": "In this book",
        "libro": "Book",
        "nota": "Every book is a complete story, with an experiment and a page for grown-ups. Read them in order and watch Tommy grow, or start with any one you like.",
        "legal": "© 2026 LERSA. All rights reserved. Illustrations created with the help of AI tools.",
        "lomo": "TOMMY'S FIRST YEAR · BOOKS 1–4",
    },
    "es": {
        "coleccion": "Así crezco, así descubro · Libros 1 a 4",
        "t1": "El primer año", "t2": "de Tommy",
        "badge": ("4", "libros", "en 1"),
        "sub": "4 libros en 1: girar, sentarse, gatear y pararse",
        "fotos": [("Girar", "de 4 a 6 meses, más o menos"), ("Sentarse", "de 6 a 8 meses, más o menos"),
                  ("Gatear", "de 7 a 10 meses, más o menos"), ("Pararse", "de 9 a 12 meses, más o menos")],
        "contra": "Cuatro primeros logros, cuatro grandes descubrimientos. En su primer año, Tommy aprende a girar, sentarse, gatear y pararse. Con Rula, su pelota grande y de colores, descubre por qué lo redondo rueda, cómo funciona el equilibrio, para qué sirve la fricción y cómo la gravedad atrae todo hacia abajo. Y en el camino cuenta, compara y mide: arriba y abajo, alto y bajo, cerca y lejos, manos y rodillas.",
        "serie": "Una colección que sigue los primeros logros de un bebé, de girar a andar en bicicleta, y en cada libro enseña un concepto de física y uno de matemática. Para leer en voz alta con niños de 4 a 7 años.",
        "adentro_t": "Adentro",
        "adentro": ["4 libros ilustrados completos en un solo tomo", "4 experimentos con cosas de la casa", "4 páginas para los grandes: la ciencia, el hito y consejos de seguridad"],
        "libros": ["Tommy aprende a girar", "Tommy aprende a sentarse", "Tommy aprende a gatear", "Tommy aprende a pararse"],
        "conceptos": ["Física: lo redondo rueda · Matemática: arriba y abajo, contar del 1 al 3",
                      "Física: el equilibrio · Matemática: alto y bajo, cerca y lejos",
                      "Física: la fricción · Matemática: contar manos y rodillas",
                      "Física: la gravedad, las cosas caen · Matemática: comparar alturas"],
        "contenido": "En este libro",
        "libro": "Libro",
        "nota": "Cada libro es una historia completa, con un experimento y una página para los grandes. Se pueden leer en orden, para ver crecer a Tommy, o empezar por el que más te guste.",
        "legal": "© 2026 LERSA. Todos los derechos reservados. Ilustraciones creadas con ayuda de inteligencia artificial.",
        "lomo": "EL PRIMER AÑO DE TOMMY · LIBROS 1 A 4",
    },
}

FUENTES = '<link href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800;9..144,900&display=swap" rel="stylesheet">'
PAPEL = "background:#FFF9E7 radial-gradient(circle at 30% 20%,rgba(255,255,255,.7),rgba(255,255,255,0) 60%)"


def fotos():
    for n, (ruta, caja) in FOTOS.items():
        im = Image.open(AQUI / ruta).convert("RGB").crop(caja).resize((1000, 1000), Image.LANCZOS)
        im.save(AQUI / "img-kdp" / f"bundle14-foto{n}.jpg", quality=92)


def badge(t, size):
    num, a, b = t["badge"]
    return (f'<div class="badge" style="width:{size}in;height:{size}in"><span>{e(a)}</span><b>{e(num)}</b><span>{e(b)}</span></div>')


def polaroid(n, t, x, y, w, giro, unidad="in"):
    tit, edad = t["fotos"][n - 1]
    return (f'<div class="pol" style="left:{x}{unidad};top:{y}{unidad};width:{w}{unidad};transform:rotate({giro}deg)">'
            f'<div class="cinta" style="background:{COLS[(n * 2) % 6]}55"></div>'
            f'<img src="img-kdp/bundle14-foto{n}.jpg"><div class="pie"><b><i style="background:{COLS[(n - 1) * 2 % 6]}">{n}</i>{e(tit)}</b><small>{e(edad)}</small></div></div>')


CSS_COMUN = """
.coleccion{font-family:Fraunces,serif;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:#C4532E}
h1{font-family:Fraunces,serif;font-weight:800;line-height:.95;margin:0;letter-spacing:-.01em;color:#23304A}
.autor{display:inline-block;font-family:Fraunces,serif;font-weight:700;letter-spacing:.12em;color:#C4532E;background:#FFF8E8;border-radius:1.5mm;box-shadow:0 .5mm 1mm rgba(70,45,20,.2)}
.badge{position:absolute;border-radius:50%;background:conic-gradient(#D9452B 0 60deg,#EE8A2A 0 120deg,#E9B21C 0 180deg,#5E9E44 0 240deg,#4FA3D9 0 300deg,#8A5CB8 0 360deg);display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:900;color:#fff;text-shadow:0 .5mm 1mm rgba(0,0,0,.4);line-height:.85;box-shadow:0 1mm 2mm rgba(70,45,20,.25);transform:rotate(8deg)}
.badge b{font-size:17mm}.badge span{font-size:3.6mm;letter-spacing:.12em;text-transform:uppercase}
.pol{position:absolute;background:#fffdf8;padding:2.6mm 2.6mm 0;box-shadow:0 1.2mm 2.5mm rgba(70,45,20,.28),0 0 0 .2mm rgba(70,45,20,.08)}
.pol img{display:block;width:100%;aspect-ratio:1;object-fit:cover}
.pol .pie{padding:2mm 0 2.6mm;text-align:center;font-family:Andika,sans-serif;color:#23304A}
.pol .pie b{display:flex;align-items:center;justify-content:center;gap:1.8mm;font-family:Fraunces,serif;font-weight:800;font-size:4.6mm}
.pol .pie i{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:5.6mm;height:5.6mm;border-radius:50%;color:#fff;font-size:3.4mm}
.pol .pie small{display:block;font-size:2.7mm;color:#6E5F52;margin-top:.6mm}
.pol .cinta{position:absolute;left:50%;top:-2.6mm;width:16mm;height:5.5mm;margin-left:-8mm;transform:rotate(-4deg);backdrop-filter:blur(.3px)}
"""


def camino_svg(puntos, ancho, alto):
    """Línea punteada que une las fotos, de abajo a la izquierda hacia arriba a la derecha (coordenadas en pulgadas)."""
    d = f"M{puntos[0][0]},{puntos[0][1]} " + " ".join(f"Q{(a[0] + b[0]) / 2},{max(a[1], b[1]) + 0.35} {b[0]},{b[1]}" for a, b in zip(puntos, puntos[1:]))
    return (f'<svg style="position:absolute;left:0;top:0" width="{ancho}in" height="{alto}in" viewBox="0 0 {ancho} {alto}">'
            f'<path d="{d}" fill="none" stroke="#C4532E" stroke-width="0.035" stroke-dasharray="0.09 0.08" stroke-linecap="round" opacity=".7"/></svg>')


def tapa(lang):
    t = T[lang]
    frente_x = SANGRADO + REFILE + LOMO
    # Fotos del frente (pulgadas, desde el borde de refile del frente)
    W = 1.95
    pos = [(0.4, 5.55, -6), (2.33, 4.8, 4), (4.26, 4.05, -3), (6.2, 3.3, 5)]
    pols = "".join(polaroid(n + 1, t, frente_x + x, SANGRADO + y, W, g) for n, (x, y, g) in enumerate(pos))
    centros = [(frente_x + x + W / 2, SANGRADO + y + W / 2) for x, y, _ in pos]
    lista = "".join(f"<li>{e(x)}</li>" for x in t["adentro"])
    minis = "".join(f'<div class="mini"><img src="img-kdp/{FOTOS[n][0].split("/")[1]}"><div><b>{e(t["libro"])} {n}</b><span>{e(t["libros"][n - 1])}</span></div></div>' for n in range(1, 5))
    doc = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{e(t['t1'])} {e(t['t2'])} · tapa</title>{FUENTES}
<style>
@page{{size:{ANCHO}in {ALTO}in;margin:0}}*{{box-sizing:border-box}}
body{{margin:0;font-family:Andika,sans-serif;color:#23304A}}
.tapa{{position:relative;width:{ANCHO}in;height:{ALTO}in;overflow:hidden;{PAPEL}}}
{CSS_COMUN}
.frente{{position:absolute;left:{frente_x}in;top:0;width:{REFILE + SANGRADO}in;height:100%;background:linear-gradient(#FFF9E7 0,#FFF3DC 100%)}}
.alfombra{{position:absolute;left:{frente_x}in;bottom:0;width:{REFILE + SANGRADO}in;height:1.25in;background:repeating-linear-gradient(90deg,#EBD3A6 0 .09in,#E2C38E .09in .18in);opacity:.55}}
.titulo{{position:absolute;left:{frente_x + 0.6}in;top:{SANGRADO + 0.55}in;width:5.6in}}
.titulo .coleccion{{font-size:11pt;margin-bottom:3mm}}
.titulo h1{{font-size:62pt}}
.titulo .sub{{font-family:Andika,sans-serif;font-weight:700;font-size:13pt;color:#6E5F52;margin-top:4mm;max-width:4.6in;line-height:1.3}}
.titulo .autor{{font-size:13pt;margin-top:4mm;padding:1.2mm 3.5mm}}
.lomo{{position:absolute;left:{SANGRADO + REFILE}in;top:0;width:{LOMO}in;height:100%;display:flex;align-items:center;justify-content:center}}
.lomo div{{transform:rotate(90deg);white-space:nowrap;font-family:Fraunces,serif;font-weight:800;font-size:6.2pt;letter-spacing:.12em;color:#23304A}}
.lomo div span{{color:#C4532E;margin-left:3mm}}
.texto{{position:absolute;left:{SANGRADO + 0.7}in;top:{SANGRADO + 0.62}in;width:{REFILE - 1.4}in}}
.texto .coleccion{{font-size:11pt;margin-bottom:3mm}}
.texto h2{{font-family:Fraunces,serif;font-weight:800;font-size:24pt;line-height:1.05;margin:0 0 4mm}}
.texto p{{font-size:11.6pt;line-height:1.42;margin:0 0 3.5mm}}
.texto .serie{{font-size:10pt;color:#6E5F52}}
.minis{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm 4mm;margin:1mm 0 4mm}}
.mini{{display:flex;gap:2.5mm;align-items:center}}
.mini img{{width:.62in;height:.62in;border-radius:1.5mm;box-shadow:0 .5mm 1.2mm rgba(70,45,20,.25)}}
.mini b{{display:block;font-family:Fraunces,serif;font-size:9pt;color:#C4532E;letter-spacing:.06em;text-transform:uppercase}}
.mini span{{font-size:10pt;line-height:1.2}}
.adentro{{background:#FFF3DC;border-radius:3mm;padding:3mm 6mm}}
.adentro b{{font-family:Fraunces,serif;font-size:11.5pt;color:#C4532E}}
.adentro ul{{margin:1.5mm 0 0;padding-left:6mm;font-size:10.4pt;line-height:1.45}}
.rula{{position:absolute;left:{SANGRADO + 0.7}in;bottom:{SANGRADO + 0.5}in;width:1.15in}}
.firma{{position:absolute;left:{SANGRADO + 2.05}in;bottom:{SANGRADO + 0.72}in;font-family:Fraunces,serif;font-weight:700;font-size:12pt;letter-spacing:.12em;color:#C4532E}}
.rula2{{position:absolute;left:{frente_x + 6.55}in;top:{SANGRADO + 6.95}in;width:1.05in;transform:rotate(-12deg)}}
</style></head><body><div class="tapa">
<div class="frente"></div><div class="alfombra"></div>
{camino_svg(centros, ANCHO, ALTO)}
{pols}
<img class="rula2" src="../web/img/rula.webp" alt="">
<div class="titulo"><div class="coleccion">{e(t['coleccion'])}</div><h1>{e(t['t1'])}<br>{e(t['t2'])}</h1><div class="sub">{e(t['sub'])}</div><div class="autor">by LERSA</div></div>
<div style="position:absolute;left:{frente_x + REFILE - 0.55 - 1.5}in;top:{SANGRADO + 0.5}in">{badge(t, 1.5)}</div>
<div class="lomo"><div>{e(t['lomo'])}<span>LERSA</span></div></div>
<div class="texto"><div class="coleccion">{e(t['coleccion'])}</div><h2>{e(t['t1'])} {e(t['t2'])}</h2>
<p>{e(t['contra'])}</p><div class="minis">{minis}</div>
<div class="adentro"><b>{e(t['adentro_t'])}</b><ul>{lista}</ul></div><p class="serie" style="margin-top:3.5mm">{e(t['serie'])}</p></div>
<img class="rula" src="../web/img/rula.webp" alt=""><div class="firma">by LERSA</div>
</div></body></html>"""
    salida = AQUI / f"kdp-tapa-bundle14-{lang}.html"
    salida.write_text(doc, encoding="utf-8")
    print("ok", salida.name, f"{ANCHO:.4f} x {ALTO} in, lomo {LOMO:.4f} in")


def intro(lang):
    """Las dos páginas de presentación del interior (misma medida que las páginas de KDP: 219,075 × 222,25 mm)."""
    t = T[lang]
    W, H = 219.075, 222.25
    pols = "".join(polaroid(n, t, x, y, 40, g, "mm") for n, (x, y, g) in zip(range(1, 5), [(18, 136, -5), (63, 128, 4), (108, 120, -3), (153, 112, 5)]))
    items = "".join(f'<div class="item"><i style="background:{COLS[(n - 1) * 2 % 6]}">{n}</i><div><b>{e(t["libros"][n - 1])}</b><span>{e(t["conceptos"][n - 1])}</span></div></div>' for n in range(1, 5))
    doc = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{e(t['t1'])} {e(t['t2'])} · interior</title>{FUENTES}
<style>
@page{{size:{W}mm {H}mm;margin:0}}*{{box-sizing:border-box}}
html,body{{margin:0;width:{W}mm}}body{{font-family:Andika,sans-serif;color:#23304A}}
.kpage{{contain:paint;width:{W}mm;height:{H}mm;position:relative;overflow:hidden;{PAPEL}}}
{CSS_COMUN}
.p1 .titulo{{position:absolute;left:22mm;top:30mm;right:20mm}}
.p1 .coleccion{{font-size:10pt;margin-bottom:4mm}}
.p1 h1{{font-size:50pt}}
.p1 .sub{{font-weight:700;font-size:12.5pt;color:#6E5F52;margin-top:5mm;line-height:1.3;max-width:130mm}}
.p1 .autor{{font-size:12pt;margin-top:5mm;padding:1.2mm 3.5mm}}
.p2 .caja{{position:absolute;left:22mm;right:22mm;top:24mm}}
.p2 h2{{font-family:Fraunces,serif;font-weight:800;font-size:26pt;margin:0 0 7mm}}
.item{{display:flex;gap:5mm;align-items:flex-start;margin-bottom:7mm}}
.item i{{flex:none;font-style:normal;width:11mm;height:11mm;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:900;font-size:6mm;box-shadow:0 .5mm 1mm rgba(70,45,20,.25)}}
.item b{{display:block;font-family:Fraunces,serif;font-weight:800;font-size:15pt;line-height:1.15}}
.item span{{font-size:11pt;color:#6E5F52}}
.nota{{font-size:11.5pt;line-height:1.45;background:#FFF3DC;border-radius:3mm;padding:4mm 6mm;margin-top:3mm}}
.legal{{position:absolute;left:24mm;right:24mm;bottom:16mm;font:7pt/1.3 Andika,sans-serif;color:#6E5F52;text-align:center}}
</style></head><body>
<div class="kpage p1"><div class="titulo"><div class="coleccion">{e(t['coleccion'])}</div><h1>{e(t['t1'])}<br>{e(t['t2'])}</h1><div class="sub">{e(t['sub'])}</div><div class="autor">by LERSA</div></div>{pols}</div>
<div class="kpage p2"><div class="caja"><h2>{e(t['contenido'])}</h2>{items}<div class="nota">{e(t['nota'])}</div></div><div class="legal">{e(t['legal'])}</div></div>
</body></html>"""
    salida = AQUI / f"kdp-bundle14-{lang}-intro.html"
    salida.write_text(doc, encoding="utf-8")
    print("ok", salida.name)


def pdf_interior(lang):
    import pypdf
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["node", str(AQUI / "kdp_capturas.js"), str(AQUI / f"kdp-bundle14-{lang}-intro.html"), tmp], check=True)
        pags = [Image.open(f).convert("RGB").resize((3450, 3500), Image.LANCZOS) for f in sorted(glob.glob(f"{tmp}/p*.png"))]
        assert len(pags) == 2, len(pags)
        intro_pdf = Path(tmp) / "intro.pdf"
        pags[0].save(intro_pdf, save_all=True, append_images=pags[1:], resolution=400, quality=92)
        w = pypdf.PdfWriter()
        for f in [intro_pdf] + [RAIZ / "kdp" / f"libro{n}-{lang}-interior.pdf" for n in range(1, 5)]:
            for p in pypdf.PdfReader(str(f)).pages:
                w.add_page(p)
        assert len(w.pages) == PAGINAS, len(w.pages)
        salida = RAIZ / "kdp" / f"bundle14-{lang}-interior.pdf"
        with open(salida, "wb") as fh:
            w.write(fh)
    print(salida, PAGINAS, "páginas")


if __name__ == "__main__":
    lang = sys.argv[1]
    if "--pdf" in sys.argv:
        pdf_interior(lang)
    else:
        fotos()
        tapa(lang)
        intro(lang)
