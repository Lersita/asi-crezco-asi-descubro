#!/usr/bin/env python3
"""Imágenes para el contenido A+ de Amazon de cada libro (inglés y español neutro).
Arma cada imagen en HTML y la saca con el navegador al tamaño exacto que pide Amazon.
Uso: python3 maqueta/aplus.py [N-lang ...] (sin nada: todos) → kdp/aplus/libroN-<lang>-*.jpg y kdp/aplus/serie-<lang>.jpg\n(la imagen de la serie es una sola por idioma, la misma para todos los libros)
Las tapas de la serie salen de los PDF de tapa (kdp/aplus/tapas/libroN-<lang>.jpg)."""
import html, subprocess, json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
SALIDA = RAIZ / "kdp" / "aplus"
IMG = f"file://{AQUI}/img"
TAPAS = f"file://{SALIDA}/tapas"
e = html.escape
COLS = ["#D9452B", "#EE8A2A", "#E9B21C", "#5E9E44", "#4FA3D9", "#8A5CB8"]
FUENTES = '<link href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Fraunces:opsz,wght@9..144,700;9..144,800;9..144,900&display=swap" rel="stylesheet">'

LIBROS = {
    (1, "en"): {
        "serie": "I Grow, I Discover · Book 1",
        "titulo": "Tommy Learns to Roll Over",
        "lema": "Big science for little ones",
        "bajada": "A read-aloud picture book about a baby's first big milestone, and why round things roll.",
        "edad": "Ages 4–7 · Read aloud",
        "cuadros": [("d07-v2.jpg", "22% 50%"), ("d06-v3.jpg", "80% 55%"), ("exp-v2.jpg", "20% 80%")],
        "adentro_t": "What's inside",
        "adentro": [("d01-v3.jpg", "15% 60%", "A gentle story", "told by Tommy himself"),
                    ("d08-v2.jpg", "65% 60%", "Real, simple physics", "round things roll, flat ones don't"),
                    ("exp-v2.jpg", "20% 80%", "A home experiment", "with things from home"),
                    ("p24-cuna-v2.jpg", "50% 70%", "A page for grown-ups", "science, milestone and safety")],
        "serie_t": "Follow Tommy as he grows",
        "serie_b": "One milestone, one physics idea and one math idea in every book.",
        "libros": ["Roll Over", "Sit Up", "Crawl", "Stand Up"],
        "mas": "More books coming soon",
    },
    (1, "es"): {
        "serie": "Así crezco, así descubro · Libro 1",
        "titulo": "Tommy aprende a girar",
        "lema": "Gran ciencia para los más pequeños",
        "bajada": "Un libro ilustrado para leer en voz alta sobre el primer gran logro de un bebé, y por qué lo redondo rueda.",
        "edad": "De 4 a 7 años · En voz alta",
        "cuadros": [("d07-v2.jpg", "22% 50%"), ("d06-v3.jpg", "80% 55%"), ("exp-v2.jpg", "20% 80%")],
        "adentro_t": "Qué hay adentro",
        "adentro": [("d01-v3.jpg", "15% 60%", "Una historia tierna", "contada por el propio Tommy"),
                    ("d08-v2.jpg", "65% 60%", "Física simple y verdadera", "lo redondo rueda, lo plano no"),
                    ("exp-v2.jpg", "20% 80%", "Un experimento", "con cosas de la casa"),
                    ("p24-cuna-v2.jpg", "50% 70%", "Para los grandes", "la ciencia, el hito y la seguridad")],
        "serie_t": "Acompaña a Tommy mientras crece",
        "serie_b": "Un logro, un concepto de física y uno de matemática en cada libro.",
        "libros": ["Girar", "Sentarse", "Gatear", "Pararse"],
        "mas": "Pronto, más libros",
    },
}

COMUN_EN = {"lema": "Big science for little ones", "edad": "Ages 4–7 · Read aloud", "adentro_t": "What's inside",
            "serie_t": "Follow Tommy as he grows", "serie_b": "One milestone, one physics idea and one math idea in every book.",
            "libros": ["Roll Over", "Sit Up", "Crawl", "Stand Up"], "mas": "More books coming soon"}
LIBROS[(2, "en")] = {**COMUN_EN,
    "serie": "I Grow, I Discover · Book 2", "titulo": "Tommy Learns to Sit Up",
    "bajada": "A read-aloud picture book about sitting up for the first time, and the secret of balance.",
    "cuadros": [("l2-d04-v1.jpg", "68% 50%"), ("l2-d07-v1.jpg", "72% 50%"), ("l2-exp-v1.jpg", (0, 130, 1195, 1530))],
    "adentro": [("l2-d03-v1.jpg", "85% 60%", "A gentle story", "told by Tommy himself"),
                ("l2-d05-v1.jpg", "80% 60%", "Real, simple physics", "a wide base doesn't fall"),
                ("l2-exp-v1.jpg", "0% 50%", "A home experiment", "with things from home"),
                ("l2-p24-v1.jpg", "50% 60%", "A page for grown-ups", "science, milestone and safety")]}
LIBROS[(3, "en")] = {**COMUN_EN,
    "serie": "I Grow, I Discover · Book 3", "titulo": "Tommy Learns to Crawl",
    "bajada": "A read-aloud picture book about crawling, and the friction that keeps little hands from slipping.",
    "cuadros": [("l3-d05.jpg", (1420, 290, 2148, 1018)), ("l3-d02.jpg", "84% 50%"), ("l3-exp.jpg", (0, 100, 1268, 1530))],  # al cuadro 3 se le tapa a mano un puntito abajo a la derecha
    "adentro": [("l3-d10.jpg", "12% 60%", "A gentle story", "told by Tommy himself"),
                ("l3-d08.jpg", "0% 50%", "Real, simple physics", "friction keeps us from slipping"),
                ("l3-exp.jpg", "0% 30%", "A home experiment", "with things from home"),
                ("l3-p24.jpg", "50% 60%", "A page for grown-ups", "science, milestone and safety")]}

LIBROS[(4, "en")] = {**COMUN_EN,
    "serie": "I Grow, I Discover · Book 4", "titulo": "Tommy Learns to Stand Up",
    "bajada": "A read-aloud picture book about standing up for the first time, and the gravity that pulls everything down.",
    "cuadros": [("l4-d05.jpg", (1232, 0, 2250, 1018)), ("l4-d10.jpg", (60, 0, 1078, 1018)), ("l4-exp.jpg", (330, 0, 2110, 1610))],
    "adentro": [("l4-d01.jpg", "25% 60%", "A gentle story", "told by Tommy himself"),
                ("l4-d06.jpg", "85% 50%", "Real, simple physics", "gravity pulls things down"),
                ("l4-exp.jpg", "0% 20%", "A home experiment", "with things from home"),
                ("l4-p24.jpg", "50% 60%", "A page for grown-ups", "science, milestone and safety")]}

LIBROS[(5, "en")] = {**COMUN_EN,
    "libros": ["Roll Over", "Sit Up", "Crawl", "Stand Up", "Walk"], "serie_n": [1, 2, 3, 4, 5],
    "serie": "I Grow, I Discover · Book 5", "titulo": "Tommy Learns to Walk",
    "bajada": "A read-aloud picture book about first steps, and the forces that make things move: pushing and pulling.",
    "cuadros": [("l5-d05.jpg", (240, 0, 1258, 1018)), ("l5-d03.jpg", (200, 0, 1218, 1018)), ("l5-exp.jpg", (0, 0, 2400, 1610))],
    "adentro": [("l5-d01.jpg", "30% 60%", "A gentle story", "told by Tommy himself"),
                ("l5-d06.jpg", "75% 50%", "Real, simple physics", "pushing and pulling are forces"),
                ("l5-exp.jpg", "50% 50%", "A home experiment", "with things from home"),
                ("l5-p24.jpg", "50% 70%", "A page for grown-ups", "science, milestone and safety")]}

BASE = f"""<!doctype html><html><head><meta charset="utf-8">{FUENTES}<style>
*{{box-sizing:border-box}}body{{margin:0;font-family:Andika,sans-serif;color:#23304A}}
.lienzo{{position:relative;overflow:hidden;background:#FFF9E7}}
.col{{font-family:Fraunces,serif;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:#C4532E}}
h1,h2{{font-family:Fraunces,serif;font-weight:900;margin:0;line-height:1;letter-spacing:-.01em}}
.foto{{background-size:cover;border-radius:14px;box-shadow:0 4px 10px rgba(70,45,20,.22)}}
</style></head><body>"""


def cabecera(t):
    return BASE + f"""<div class="lienzo" style="width:970px;height:600px">
<div class="foto" style="position:absolute;left:40px;top:40px;width:520px;height:520px;background-image:url({TAPAS}/libro{N}-{LANG}.jpg)"></div>
<div style="position:absolute;left:600px;top:70px;width:330px">
<div class="col" style="font-size:14px">{e(t['serie'])}</div>
<h2 style="font-size:46px;margin-top:16px">{e(t['lema'])}</h2>
<p style="font-size:21px;line-height:1.4;margin:22px 0 0">{e(t['bajada'])}</p>
<div style="display:inline-block;margin-top:24px;padding:9px 16px;border-radius:30px;background:#5E9E44;color:#fff;font-weight:700;font-size:18px">{e(t['edad'])}</div>
</div></div></body></html>"""


def cuadro(img, pos):
    """pos: posición CSS del recorte, o una caja (x0, y0, x1, y1) en píxeles para recortar antes."""
    if isinstance(pos, tuple):
        from PIL import Image
        nombre = f"recorte-{img}"
        rec = Image.open(AQUI / "img" / img).convert("RGB").crop(pos)
        lado = max(rec.size)   # si la caja no es cuadrada, se completa con el color del fondo (crema liso)
        cuadrado = Image.new("RGB", (lado, lado), rec.getpixel((5, 5)))
        cuadrado.paste(rec, ((lado - rec.width) // 2, (lado - rec.height) // 2))
        cuadrado.save(SALIDA / nombre, quality=92)
        return BASE + f'<div class="lienzo" style="width:300px;height:300px;background:url(file://{SALIDA}/{nombre}) center/cover no-repeat"></div></body></html>'
    return BASE + f'<div class="lienzo" style="width:300px;height:300px;background:url({IMG}/{img}) {pos}/cover no-repeat"></div></body></html>'


def adentro(t):
    tiles = "".join(
        f'<div style="width:215px;text-align:center"><div class="foto" style="width:215px;height:150px;background:url({IMG}/{img}) {pos}/cover no-repeat"></div>'
        f'<div style="font-family:Fraunces,serif;font-weight:800;font-size:19px;margin-top:10px;color:{['#C4442A', '#4E8A37', '#3F7FB0', '#7D51AB'][k]}">{e(a)}</div>'
        f'<div style="font-size:15px;margin-top:3px">{e(b)}</div></div>'
        for k, (img, pos, a, b) in enumerate(t["adentro"]))
    return BASE + f"""<div class="lienzo" style="width:970px;height:300px;padding:18px 25px">
<h2 style="font-size:28px;text-align:center">{e(t['adentro_t'])}</h2>
<div style="display:flex;justify-content:space-between;margin-top:14px">{tiles}</div></div></body></html>"""


SERIE = {
    "en": {"t": "Follow Tommy as he grows", "b": "From rolling over to riding a bike: one milestone, one physics idea and one math idea in every book.",
           "hitos": ["Roll over", "Sit up", "Crawl", "Stand up", "Walk", "Run", "Jump", "Climb stairs", "Throw a ball", "Swim", "Ride a bike"]},
    "es": {"t": "Acompaña a Tommy mientras crece", "b": "De girar a andar en bicicleta: un logro, un concepto de física y uno de matemática en cada libro.",
           "hitos": ["Girar", "Sentarse", "Gatear", "Pararse", "Caminar", "Correr", "Saltar", "Subir escaleras", "Lanzar", "Nadar", "Andar en bici"]},
}


def serie(lang):
    """Imagen genérica de la serie, la misma para todos los libros: Tommy de cada libro, creciendo en escalera
    (las fotitos salen de maqueta/img-kdp/coleccion-fotoN.jpg, que arma kdp_coleccion.py). No nombra tapas
    ni cuántos libros hay publicados, así no hay que cambiarla cuando sale un libro nuevo."""
    t = SERIE[lang]
    puntos, items = [], []
    for i in range(11):
        n = i + 1
        lado = 58 + i * 1.6
        cx = 62 + i * 84.6
        cy = 492 - i * 24
        puntos.append(f"{cx:.0f},{cy:.0f}")
        items.append(
            f'<div style="position:absolute;left:{cx - lado / 2:.0f}px;top:{cy - lado / 2:.0f}px;width:{lado:.0f}px">'
            f'<div class="foto" style="width:{lado:.0f}px;height:{lado:.0f}px;border:4px solid #fff;background-image:url(file://{AQUI}/img-kdp/coleccion-foto{n}.jpg);transform:rotate({[-3, 2, -2, 3, -1, 2][i % 6]}deg)"></div>'
            f'<span style="position:absolute;left:-9px;top:-9px;display:flex;width:24px;height:24px;border-radius:50%;background:{COLS[i % 6]};color:#fff;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:900;font-size:13px;box-shadow:0 1px 3px rgba(0,0,0,.3)">{n}</span>'
            f'<div style="position:absolute;left:-14px;right:-14px;top:{lado + 8:.0f}px;text-align:center;font-family:Fraunces,serif;font-weight:800;font-size:14px;line-height:1.05">{e(t["hitos"][i])}</div></div>')
    return BASE + f"""<div class="lienzo" style="width:970px;height:600px">
<h2 style="position:absolute;left:0;right:0;top:46px;font-size:44px;text-align:center">{e(t['t'])}</h2>
<p style="position:absolute;left:90px;right:90px;top:108px;font-size:20px;line-height:1.35;text-align:center;margin:0">{e(t['b'])}</p>
<svg width="970" height="600" style="position:absolute;left:0;top:0"><polyline points="{' '.join(puntos)}" fill="none" stroke="#C4532E" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round" opacity=".55"/></svg>
{''.join(items)}</div></body></html>"""


JS = """const { chromium } = require('playwright');
(async () => { const trabajos = JSON.parse(process.argv[2]); const b = await chromium.launch();
  for (const [html, png, w, h] of trabajos) { const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + html, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: png, type: 'jpeg', quality: 90 }); await p.close(); }
  await b.close(); })();"""

if __name__ == "__main__":
    trabajos = []
    import sys
    elegidos = [(int(a.split("-")[0]), a.split("-")[1]) for a in sys.argv[1:]] or list(LIBROS)
    for (N, LANG) in elegidos:
        t = LIBROS[(N, LANG)]
        piezas = [("1-cabecera", cabecera(t), 970, 600), ("3-adentro", adentro(t), 970, 300)]
        piezas += [(f"2-cuadro{k + 1}", cuadro(*c), 300, 300) for k, c in enumerate(t["cuadros"])]
        for nombre, doc, w, h in piezas:
            f = SALIDA / f"libro{N}-{LANG}-{nombre}.html"
            f.write_text(doc, encoding="utf-8")
            trabajos.append([str(f), str(SALIDA / f"libro{N}-{LANG}-{nombre}.jpg"), w, h])
    for lang in sorted({l for _, l in elegidos}):
        f = SALIDA / f"serie-{lang}.html"
        f.write_text(serie(lang), encoding="utf-8")
        trabajos.append([str(f), str(SALIDA / f"serie-{lang}.jpg"), 970, 600])
    js = SALIDA / "capturar.js"
    js.write_text(JS, encoding="utf-8")
    subprocess.run(["node", str(js), json.dumps(trabajos)], check=True, cwd=AQUI)
    for _, png, *_ in trabajos:
        Path(png.replace(".jpg", ".html")).unlink()
    js.unlink()
    print("ok", len(trabajos), "imágenes en", SALIDA)
