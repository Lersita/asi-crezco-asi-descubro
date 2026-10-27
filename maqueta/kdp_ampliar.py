#!/usr/bin/env python3
"""Amplía las ilustraciones de los libros 1 a 4 para la imprenta de KDP (300 dpi o más), sin IA:
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
L3 = {"p01": "p01-v1", "d01": "d01-v1", "d02": "d02-v1", "d03": "d03-v1", "d04": "d04-v1", "d05": "d05-v1", "d06": "d06-v2", "d07": "d07-v1", "d08": "d08-v2", "d09": "d09-v1", "d10": "d10-v2", "exp": "exp-v1", "p24": "p24-v1"}
L4 = {"p01": "p01-v2", "d01": "d01-v2", "d02": "d02-v2", "d03": "d03-v2", "d04": "d04-v2", "d05": "d05-v2", "d06": "d06-v1", "d07": "d07-v2", "d08": "d08-v1", "d09": "d09-v1", "d10": "d10-v1", "exp": "exp-v1", "p24": "p24-v1"}
FUENTES.update({"l3-" + k: f"ilustraciones/libro3/{v}.png" for k, v in L3.items()})
FUENTES.update({"l4-" + k: f"ilustraciones/libro4/{v}.png" for k, v in L4.items()})

SALIDA.mkdir(exist_ok=True)
for nombre, ruta in FUENTES.items():
    im = Image.open(RAIZ / ruta).convert("RGB")
    chica = nombre.endswith(("exp-v2", "p24-cuna-v2", "exp-v1", "p24-v1", "-exp", "-p24"))
    if not chica:
        im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    im.save(SALIDA / f"{nombre}.jpg", quality=92)
    print(nombre, im.size)
