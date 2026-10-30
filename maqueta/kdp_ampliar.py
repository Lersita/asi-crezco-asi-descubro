#!/usr/bin/env python3
"""Amplía las ilustraciones de los libros 1 a 6 para la imprenta de KDP (300 dpi o más), sin IA:
ampliación Lanczos ×2 desde el PNG original más un leve realce de nitidez, que conserva la textura del papel.
Las imágenes que se imprimen chicas (experimento y viñeta de la página 24) se pasan sin ampliar, a calidad alta.
Uso: python3 maqueta/kdp_ampliar.py → maqueta/img-kdp/<mismo nombre que en maqueta/img>.jpg (no se guarda en Git)"""
from pathlib import Path
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "maqueta" / "img-kdp"

FUENTES = {}
for n in ["d01-v3", "d02-v4", "d03-v3", "d04-v3-compuesta", "d05-v2", "d06-v3", "d07-v2", "d08-v2", "d09-v2", "d10-v3-compuesta", "exp-v2", "p01-portada-v2", "p24-cuna-v2"]:
    FUENTES[n] = f"ilustraciones/borradores/{n}.png"
for n in ["d01-v1", "d02-v1", "d03-v1", "d04-v1", "d05-v1", "d06-v1", "d07-v1", "d08-v1", "d09-v1", "d10-compuesta", "exp-v1", "p01-portada-v1", "p24-v1"]:
    FUENTES["l2-" + n] = f"ilustraciones/libro2/{n}.png"
# Desde el 28/10/2026, versión con menos pelo (segunda corrección del pelo): -pelo2 y, donde se arregló a mano, -pelo2-c.
L3 = {k: f"{k}-pelo2" for k in ["p01", "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10"]}
L3.update({"p24": "p24-pelo2-c", "exp": "exp-v1"})
L4 = {k: f"{k}-pelo2" for k in ["p01", "d01", "d02", "d05", "d06", "d07", "d08", "d09", "p24"]}
L4.update({"d03": "d03-pelo2-c", "d04": "d04-pelo2-c", "d10": "d10-pelo2-c", "exp": "exp-v1"})
FUENTES.update({"l3-" + k: f"ilustraciones/libro3/{v}.png" for k, v in L3.items()})
FUENTES.update({"l4-" + k: f"ilustraciones/libro4/{v}.png" for k, v in L4.items()})
FUENTES.update({f"l6-{k}": f"ilustraciones/libro6/{k}-v2.png" if k == "d03" else f"ilustraciones/libro6/{k}-v1.png" for k in ["p01", "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10", "exp", "p24"]})
FUENTES.update({f"l7-{k}": f"ilustraciones/libro7/{k}-v1.png" for k in ["p01", "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10", "exp", "p24"]})
FUENTES.update({f"l5-{k}": f"ilustraciones/libro5/{k}-v1.png" for k in ["p01", "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10", "exp", "p24"]})

SALIDA.mkdir(exist_ok=True)
for nombre, ruta in FUENTES.items():
    im = Image.open(RAIZ / ruta).convert("RGB")
    chica = nombre.endswith(("exp-v2", "p24-cuna-v2", "exp-v1", "p24-v1", "-exp", "-p24"))
    if not chica:
        im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    im.save(SALIDA / f"{nombre}.jpg", quality=92)
    print(nombre, im.size)
