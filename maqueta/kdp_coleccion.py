#!/usr/bin/env python3
"""La colección completa (los 11 libros) para Amazon KDP: "I Grow, I Discover: The Complete Collection" /
"Así crezco, así descubro: la colección completa".
Interior: 2 páginas de presentación + los interiores de KDP de los 11 libros (24 páginas cada uno) = 266 páginas.
Tapa: la pared de crecimiento. Una ilustración del living con el marco de una puerta (ilustraciones/coleccion/tapa-v1.png);
encima, las rayitas de altura y una fotito de Tommy de cada libro, de bebé abajo a nene en bici arriba (se arman acá).

Uso: python3 maqueta/kdp_coleccion.py es|en          → maqueta/kdp-coleccion-<lang>-intro.html y maqueta/kdp-tapa-coleccion-<lang>.html
     python3 maqueta/kdp_coleccion.py es|en --pdf    → kdp/coleccion-<lang>-interior.pdf (unos 400 MB)
     python3 maqueta/kdp_achicar.py kdp/coleccion-es-interior.pdf /tmp/x.pdf 82 && mv /tmp/x.pdf kdp/coleccion-es-interior.pdf   (unos 270 MB)
     node maqueta/kdp_pdf.js maqueta/kdp-tapa-coleccion-es.html kdp/coleccion-es-tapa.pdf 17.8743in 8.75in"""
import sys, html, subprocess, tempfile, glob
from pathlib import Path
from PIL import Image
import kdp_bundle as kb

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
SANGRADO, REFILE, PAGINAS = 0.125, 8.5, 2 + 24 * 11
LOMO = PAGINAS * 0.002347
ANCHO = 2 * SANGRADO + 2 * REFILE + LOMO
ALTO = REFILE + 2 * SANGRADO
e = html.escape
COLS = kb.COLS

# Recorte de Tommy en la tapa de cada libro (los mismos de los recopilatorios)
FOTOS = {}
for grupo, primero in ((kb.FOTOS14, 1), (kb.FOTOS58, 5), (kb.FOTOS911, 9)):
    for i, v in grupo.items():
        FOTOS[primero + i - 1] = v

T = {
    "en": {
        "serie": "I Grow, I Discover", "t2": "The Complete Collection",
        "badge": ("11", "books", "in 1"),
        "sub": "From rolling over to riding a bike: 11 first milestones, 11 physics ideas, and 11 math ideas",
        "edad": ["4–6 mo", "6–8 mo", "7–10 mo", "9–12 mo", "12–15 mo", "18–24 mo", "2–3 yrs", "2–3 yrs", "3–4 yrs", "4–5 yrs", "5–6 yrs"],
        "hitos": ["Roll over", "Sit up", "Crawl", "Stand up", "Walk", "Run", "Jump", "Climb the stairs", "Throw a ball", "Swim", "Ride a bike"],
        "libros": [kb.T14["en"]["libros"][i] for i in range(4)] + [kb.T58["en"]["libros"][i] for i in range(4)] + [kb.T911["en"]["libros"][i] for i in range(3)],
        "conceptos": kb.T14["en"]["conceptos"] + kb.T58["en"]["conceptos"] + kb.T911["en"]["conceptos"],
        "contra": "Eleven first milestones, eleven big discoveries. Follow Tommy as he grows, from a baby rolling over on the rug to a boy riding his bike in the park. With Rula, his big colorful ball, he discovers rolling, balance, friction, gravity, force, speed, trajectories, floating, and balance on the move. And along the way he counts, measures, compares, and finds shapes, sequences, and cycles.",
        "adentro_t": "Inside",
        "adentro": ["11 complete picture books in one volume", "11 hands-on experiments with things from home", "11 pages for grown-ups: the science, the milestone, and safety tips"],
        "pie": "A series that follows a baby's first big milestones, with one physics idea and one math idea in every book. For reading aloud with kids ages 4 to 7.",
        "contenido": "In this book", "libro": "Book",
        "nota": "Every book is a complete story. Read them in order and watch Tommy grow, or start with any one you like.",
        "legal": kb.T14["en"]["legal"],
        "lomo": "I GROW, I DISCOVER · THE COMPLETE COLLECTION",
    },
    "es": {
        "serie": "Así crezco, así descubro", "t2": "La colección completa",
        "badge": ("11", "libros", "en 1"),
        "sub": "De girar a andar en bicicleta: 11 primeros logros, 11 ideas de física y 11 de matemática",
        "edad": ["4–6 meses", "6–8 meses", "7–10 meses", "9–12 meses", "12–15 meses", "18–24 meses", "2–3 años", "2–3 años", "3–4 años", "4–5 años", "5–6 años"],
        "hitos": ["Girar", "Sentarse", "Gatear", "Pararse", "Caminar", "Correr", "Saltar", "Subir la escalera", "Lanzar una pelota", "Nadar", "Andar en bicicleta"],
        "libros": [kb.T14["es"]["libros"][i] for i in range(4)] + [kb.T58["es"]["libros"][i] for i in range(4)] + [kb.T911["es"]["libros"][i] for i in range(3)],
        "conceptos": kb.T14["es"]["conceptos"] + kb.T58["es"]["conceptos"] + kb.T911["es"]["conceptos"],
        "contra": "Once primeros logros, once grandes descubrimientos. Acompaña a Tommy mientras crece, desde que es un bebé que gira en la alfombra hasta que anda en bicicleta por el parque. Con Rula, su pelota grande y de colores, descubre cómo se rueda, el equilibrio, la fricción, la gravedad, la fuerza, la velocidad, la trayectoria, la flotación y el equilibrio en movimiento. Y en el camino cuenta, mide, compara y encuentra figuras, secuencias y ciclos.",
        "adentro_t": "Adentro",
        "adentro": ["11 libros ilustrados completos en un solo tomo", "11 experimentos con cosas de la casa", "11 páginas para los grandes: la ciencia, el hito y consejos de seguridad"],
        "pie": "Una colección que sigue los primeros logros de un bebé, con un concepto de física y uno de matemática en cada libro. Para leer en voz alta con niños de 4 a 7 años.",
        "contenido": "En este libro", "libro": "Libro",
        "nota": "Cada libro es una historia completa. Se pueden leer en orden, para ver crecer a Tommy, o empezar por el que más te guste.",
        "legal": kb.T14["es"]["legal"],
        "lomo": "ASÍ CREZCO, ASÍ DESCUBRO · LA COLECCIÓN COMPLETA",
    },
}


def fotos():
    for n, (ruta, caja) in FOTOS.items():
        im = Image.open(AQUI / ruta).convert("RGB").crop(caja).resize((700, 700), Image.LANCZOS)
        im.save(AQUI / "img-kdp" / f"coleccion-foto{n}.jpg", quality=90)


def pared(t, x0, y0):
    """Las rayitas de altura sobre el poste izquierdo del marco de la puerta y una fotito por libro,
    alternando a cada lado del poste, de bebé abajo a nene en bici arriba (pulgadas)."""
    out = []
    poste = x0 + 4.98          # borde izquierdo del poste del marco en la ilustración
    for i in range(11):
        n = i + 1
        y = y0 + 5.45 - i * 0.462
        out.append(f'<div style="position:absolute;left:{poste + 0.02}in;top:{y}in;width:.28in;height:.03in;background:#5B4636;border-radius:.02in;opacity:.85"></div>')
        fx = poste - 0.76 if i % 2 == 0 else poste + 0.42
        out.append(f'<div class="foto" style="left:{fx}in;top:{y - 0.3}in;transform:rotate({[-4, 3, -2, 4, -3, 2][i % 6]}deg)">'
                   f'<img src="img-kdp/coleccion-foto{n}.jpg"><i style="background:{COLS[(n - 1) % 6]}">{n}</i></div>')
    return "".join(out)


CSS = """
.foto{position:absolute;width:.62in;background:#fffdf8;padding:.04in .04in .04in;box-shadow:0 .6mm 1.4mm rgba(70,45,20,.35)}
.foto img{display:block;width:100%;aspect-ratio:1;object-fit:cover}
.foto i{position:absolute;right:-.09in;top:-.09in;font-style:normal;width:.24in;height:.24in;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:900;font-size:8.5pt;box-shadow:0 .4mm .8mm rgba(0,0,0,.3)}
"""


def tapa(lang):
    t = T[lang]
    frente_x = SANGRADO + REFILE + LOMO
    ilus = RAIZ / "ilustraciones" / "coleccion" / "tapa-v1.png"
    im = Image.open(ilus).convert("RGB")
    im.resize((im.width * 2, im.height * 2), Image.LANCZOS).save(AQUI / "img-kdp" / "coleccion-tapa.jpg", quality=92)
    lista = "".join(f"<li>{e(x)}</li>" for x in t["adentro"])
    minis = "".join(f'<div class="mini"><img src="img-kdp/coleccion-foto{n}.jpg"><span><b>{n}</b> {e(t["hitos"][n - 1])}</span></div>' for n in range(1, 12))
    doc = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{e(t['serie'])} · tapa</title>{kb.FUENTES}
<style>
@page{{size:{ANCHO}in {ALTO}in;margin:0}}*{{box-sizing:border-box}}
body{{margin:0;font-family:Andika,sans-serif;color:#23304A}}
.tapa{{position:relative;width:{ANCHO}in;height:{ALTO}in;overflow:hidden;{kb.PAPEL}}}
{kb.CSS_COMUN}{CSS}
.frente{{position:absolute;left:{frente_x}in;top:0;width:{REFILE + SANGRADO}in;height:100%;background:url(img-kdp/coleccion-tapa.jpg) center/cover}}
.titulo{{position:absolute;left:{frente_x + 0.5}in;top:{SANGRADO + 0.5}in;width:3.55in}}
.titulo h1{{font-size:40pt;line-height:.98}}
.titulo .t2{{font-family:Fraunces,serif;font-weight:700;font-size:19pt;color:#C4532E;margin-top:2.5mm}}
.titulo .sub{{font-weight:700;font-size:11.5pt;color:#4E4036;margin-top:4mm;line-height:1.3;text-shadow:0 0 1.2mm #fff,0 0 2.4mm #fff}}
.titulo .autor{{font-size:13pt;margin-top:4mm;padding:1.2mm 3.5mm}}
.lomo{{position:absolute;left:{SANGRADO + REFILE}in;top:0;width:{LOMO}in;height:100%;display:flex;align-items:center;justify-content:center;background:#23304A}}
.lomo div{{transform:rotate(90deg);white-space:nowrap;font-family:Fraunces,serif;font-weight:800;font-size:13pt;letter-spacing:.12em;color:#FFF9E7}}
.lomo div span{{color:#E9B21C;margin-left:5mm}}
.texto{{position:absolute;left:{SANGRADO + 0.7}in;top:{SANGRADO + 0.6}in;width:{REFILE - 1.4}in}}
.texto .coleccion{{font-size:11pt;margin-bottom:3mm}}
.texto h2{{font-family:Fraunces,serif;font-weight:800;font-size:24pt;line-height:1.05;margin:0 0 4mm}}
.texto p{{font-size:11pt;line-height:1.42;margin:0 0 3.5mm}}
.minis{{display:grid;grid-template-columns:repeat(4,1fr);gap:2mm 3mm;margin:1mm 0 4mm}}
.mini{{display:flex;gap:2mm;align-items:center}}
.mini img{{width:.48in;height:.48in;border-radius:1.4mm;box-shadow:0 .5mm 1.2mm rgba(70,45,20,.25)}}
.mini span{{font-size:8.6pt;line-height:1.15}}
.mini b{{font-family:Fraunces,serif;color:#C4532E}}
.adentro{{background:#FFF3DC;border-radius:3mm;padding:3mm 6mm}}
.adentro b{{font-family:Fraunces,serif;font-size:11.5pt;color:#C4532E}}
.adentro ul{{margin:1.5mm 0 0;padding-left:6mm;font-size:10pt;line-height:1.45}}
.pie{{font-size:9.6pt;color:#6E5F52;margin-top:3mm}}
.rula{{position:absolute;left:{SANGRADO + 0.7}in;bottom:{SANGRADO + 0.45}in;width:1in}}
.firma{{position:absolute;left:{SANGRADO + 1.9}in;bottom:{SANGRADO + 0.62}in;font-family:Fraunces,serif;font-weight:700;font-size:12pt;letter-spacing:.12em;color:#C4532E}}
</style></head><body><div class="tapa">
<div class="frente"></div>
{pared(t, frente_x, SANGRADO)}
<div class="titulo"><div class="coleccion" style="font-size:10.5pt;margin-bottom:3mm">{e(t['badge'][0])} {e(t['badge'][1])} {e(t['badge'][2])}</div><h1>{e(t['serie'])}</h1><div class="t2">{e(t['t2'])}</div><div class="sub">{e(t['sub'])}</div><div class="autor">by LERSA</div></div>
<div class="lomo"><div>{e(t['lomo'])}<span>LERSA</span></div></div>
<div class="texto"><div class="coleccion">{e(t['serie'])} · {e(t['t2'])}</div><h2>{e(t['t2'])}</h2>
<p>{e(t['contra'])}</p><div class="minis">{minis}</div>
<div class="adentro"><b>{e(t['adentro_t'])}</b><ul>{lista}</ul></div><p class="pie">{e(t['pie'])}</p></div>
<img class="rula" src="../web/img/rula.webp" alt=""><div class="firma">by LERSA</div>
</div></body></html>"""
    salida = AQUI / f"kdp-tapa-coleccion-{lang}.html"
    salida.write_text(doc, encoding="utf-8")
    print("ok", salida.name, f"{ANCHO:.4f} x {ALTO} in, lomo {LOMO:.4f} in")


def intro(lang):
    t = T[lang]
    W, H = 219.075, 222.25
    fotos_html = "".join(
        f'<div class="foto" style="left:{22 + (i % 6) * 30 + (15 if i >= 6 else 0)}mm;top:{128 + (i // 6) * 38}mm;width:24mm;transform:rotate({[-4, 3, -2, 4, -3, 2][i % 6]}deg)">'
        f'<img src="img-kdp/coleccion-foto{i + 1}.jpg"><i style="background:{COLS[i % 6]}">{i + 1}</i></div>' for i in range(11))
    items = "".join(f'<div class="item"><i style="background:{COLS[(n - 1) % 6]}">{n}</i><div><b>{e(t["libros"][n - 1])}</b><span>{e(t["conceptos"][n - 1])}</span></div></div>' for n in range(1, 12))
    doc = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{e(t['serie'])} · interior</title>{kb.FUENTES}
<style>
@page{{size:{W}mm {H}mm;margin:0}}*{{box-sizing:border-box}}
html,body{{margin:0;width:{W}mm}}body{{font-family:Andika,sans-serif;color:#23304A}}
.kpage{{contain:paint;width:{W}mm;height:{H}mm;position:relative;overflow:hidden;{kb.PAPEL}}}
{kb.CSS_COMUN}{CSS}
.foto i{{width:6mm;height:6mm;font-size:3.4mm;right:-2mm;top:-2mm}}
.p1 .titulo{{position:absolute;left:22mm;top:28mm;right:20mm}}
.p1 h1{{font-size:44pt}}
.p1 .t2{{font-family:Fraunces,serif;font-weight:700;font-size:20pt;color:#C4532E;margin-top:2mm}}
.p1 .sub{{font-weight:700;font-size:12pt;color:#6E5F52;margin-top:5mm;line-height:1.3;max-width:150mm}}
.p1 .autor{{font-size:12pt;margin-top:5mm;padding:1.2mm 3.5mm}}
.p2 .caja{{position:absolute;left:20mm;right:20mm;top:18mm}}
.p2 h2{{font-family:Fraunces,serif;font-weight:800;font-size:22pt;margin:0 0 4mm}}
.item{{display:flex;gap:3.5mm;align-items:center;margin-bottom:2.6mm}}
.item i{{flex:none;font-style:normal;width:8mm;height:8mm;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:900;font-size:4.2mm}}
.item b{{display:block;font-family:Fraunces,serif;font-weight:800;font-size:11.5pt;line-height:1.1}}
.item span{{font-size:8.8pt;color:#6E5F52}}
.nota{{font-size:10pt;line-height:1.4;background:#FFF3DC;border-radius:3mm;padding:3mm 5mm;margin-top:2mm}}
.legal{{position:absolute;left:24mm;right:24mm;bottom:12mm;font:7pt/1.3 Andika,sans-serif;color:#6E5F52;text-align:center}}
</style></head><body>
<div class="kpage p1"><div class="titulo"><div class="coleccion" style="font-size:10pt;margin-bottom:3mm">{e(t['badge'][0])} {e(t['badge'][1])} {e(t['badge'][2])}</div><h1>{e(t['serie'])}</h1><div class="t2">{e(t['t2'])}</div><div class="sub">{e(t['sub'])}</div><div class="autor">by LERSA</div></div>{fotos_html}</div>
<div class="kpage p2"><div class="caja"><h2>{e(t['contenido'])}</h2>{items}<div class="nota">{e(t['nota'])}</div></div><div class="legal">{e(t['legal'])}</div></div>
</body></html>"""
    salida = AQUI / f"kdp-coleccion-{lang}-intro.html"
    salida.write_text(doc, encoding="utf-8")
    print("ok", salida.name)


def pdf_interior(lang):
    import pypdf
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["node", str(AQUI / "kdp_capturas.js"), str(AQUI / f"kdp-coleccion-{lang}-intro.html"), tmp], check=True)
        pags = [Image.open(f).convert("RGB").resize((3450, 3500), Image.LANCZOS) for f in sorted(glob.glob(f"{tmp}/p*.png"))]
        assert len(pags) == 2, len(pags)
        intro_pdf = Path(tmp) / "intro.pdf"
        pags[0].save(intro_pdf, save_all=True, append_images=pags[1:], resolution=400, quality=92)
        w = pypdf.PdfWriter()
        for f in [intro_pdf] + [RAIZ / "kdp" / f"libro{n}-{lang}-interior.pdf" for n in range(1, 12)]:
            for p in pypdf.PdfReader(str(f)).pages:
                w.add_page(p)
        assert len(w.pages) == PAGINAS, len(w.pages)
        salida = RAIZ / "kdp" / f"coleccion-{lang}-interior.pdf"
        with open(salida, "wb") as fh:
            w.write(fh)
    print(salida, PAGINAS, "páginas")


if __name__ == "__main__":
    lang = sys.argv[1]
    if "--pdf" in sys.argv:
        pdf_interior(lang)
    else:
        fotos()
        intro(lang)
        if (RAIZ / "ilustraciones" / "coleccion" / "tapa-v1.png").exists():
            tapa(lang)
