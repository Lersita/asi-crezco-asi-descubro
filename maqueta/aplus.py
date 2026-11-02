#!/usr/bin/env python3
"""Imágenes para el contenido A+ de Amazon (libro 1), en inglés y en español neutro.
Arma cada imagen en HTML y la saca con el navegador al tamaño exacto que pide Amazon.
Uso: python3 maqueta/aplus.py → kdp/aplus/libro1-<lang>-*.jpg
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

T = {
    "en": {
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
    "es": {
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

BASE = f"""<!doctype html><html><head><meta charset="utf-8">{FUENTES}<style>
*{{box-sizing:border-box}}body{{margin:0;font-family:Andika,sans-serif;color:#23304A}}
.lienzo{{position:relative;overflow:hidden;background:#FFF9E7}}
.col{{font-family:Fraunces,serif;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:#C4532E}}
h1,h2{{font-family:Fraunces,serif;font-weight:900;margin:0;line-height:1;letter-spacing:-.01em}}
.foto{{background-size:cover;border-radius:14px;box-shadow:0 4px 10px rgba(70,45,20,.22)}}
</style></head><body>"""


def cabecera(t):
    return BASE + f"""<div class="lienzo" style="width:970px;height:600px">
<div class="foto" style="position:absolute;left:40px;top:40px;width:520px;height:520px;background-image:url({TAPAS}/libro1-{LANG}.jpg)"></div>
<div style="position:absolute;left:600px;top:70px;width:330px">
<div class="col" style="font-size:14px">{e(t['serie'])}</div>
<h2 style="font-size:46px;margin-top:16px">{e(t['lema'])}</h2>
<p style="font-size:21px;line-height:1.4;margin:22px 0 0">{e(t['bajada'])}</p>
<div style="display:inline-block;margin-top:24px;padding:9px 16px;border-radius:30px;background:#5E9E44;color:#fff;font-weight:700;font-size:18px">{e(t['edad'])}</div>
</div></div></body></html>"""


def cuadro(img, pos):
    return BASE + f'<div class="lienzo" style="width:300px;height:300px;background:url({IMG}/{img}) {pos}/auto 100%"></div></body></html>'


def adentro(t):
    tiles = "".join(
        f'<div style="width:215px;text-align:center"><div class="foto" style="width:215px;height:150px;background:url({IMG}/{img}) {pos}/auto 100%"></div>'
        f'<div style="font-family:Fraunces,serif;font-weight:800;font-size:19px;margin-top:10px;color:{['#C4442A', '#4E8A37', '#3F7FB0', '#7D51AB'][k]}">{e(a)}</div>'
        f'<div style="font-size:15px;margin-top:3px">{e(b)}</div></div>'
        for k, (img, pos, a, b) in enumerate(t["adentro"]))
    return BASE + f"""<div class="lienzo" style="width:970px;height:300px;padding:18px 25px">
<h2 style="font-size:28px;text-align:center">{e(t['adentro_t'])}</h2>
<div style="display:flex;justify-content:space-between;margin-top:14px">{tiles}</div></div></body></html>"""


def serie(t):
    tapas = "".join(
        f'<div style="text-align:center"><div class="foto" style="width:185px;height:185px;background-image:url({TAPAS}/libro{n}-{LANG}.jpg);transform:rotate({[-3, 2, -2, 3][n - 1]}deg)"></div>'
        f'<div style="margin-top:14px;font-family:Fraunces,serif;font-weight:800;font-size:19px"><span style="display:inline-flex;width:28px;height:28px;border-radius:50%;background:{COLS[(n - 1) * 2 % 6]};color:#fff;align-items:center;justify-content:center;font-size:15px;margin-right:6px">{n}</span>{e(t["libros"][n - 1])}</div></div>'
        for n in range(1, 5))
    return BASE + f"""<div class="lienzo" style="width:970px;height:600px;padding:72px 40px">
<h2 style="font-size:44px;text-align:center">{e(t['serie_t'])}</h2>
<p style="font-size:21px;text-align:center;margin:14px 0 0">{e(t['serie_b'])}</p>
<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-top:48px;padding:0 10px">{tapas}</div>
<div style="text-align:center;margin-top:34px;font-weight:700;font-size:17px;color:#C4532E">{e(t['mas'])}</div></div></body></html>"""


JS = """const { chromium } = require('playwright');
(async () => { const trabajos = JSON.parse(process.argv[2]); const b = await chromium.launch();
  for (const [html, png, w, h] of trabajos) { const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + html, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: png, type: 'jpeg', quality: 90 }); await p.close(); }
  await b.close(); })();"""

if __name__ == "__main__":
    trabajos = []
    for LANG, t in T.items():
        piezas = [("1-cabecera", cabecera(t), 970, 600), ("3-adentro", adentro(t), 970, 300), ("4-serie", serie(t), 970, 600)]
        piezas += [(f"2-cuadro{k + 1}", cuadro(*c), 300, 300) for k, c in enumerate(t["cuadros"])]
        for nombre, doc, w, h in piezas:
            f = SALIDA / f"libro1-{LANG}-{nombre}.html"
            f.write_text(doc, encoding="utf-8")
            trabajos.append([str(f), str(SALIDA / f"libro1-{LANG}-{nombre}.jpg"), w, h])
    js = SALIDA / "capturar.js"
    js.write_text(JS, encoding="utf-8")
    subprocess.run(["node", str(js), json.dumps(trabajos)], check=True, cwd=AQUI)
    for _, png, *_ in trabajos:
        Path(png.replace(".jpg", ".html")).unlink()
    js.unlink()
    print("ok", len(trabajos), "imágenes en", SALIDA)
