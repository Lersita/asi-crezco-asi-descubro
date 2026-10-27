#!/usr/bin/env python3
# Ajusta el pelo del bebé en páginas ya hechas, según la hoja de personajes aprobada.
# uso: pelo.py varon|mujer 2|3 URL_HOJA imagen.png [...]   (2|3 = libro, para la cantidad de pelo)  → guarda imagen-pelo.png al lado de cada una
import sys, subprocess, json
from concurrent.futures import ThreadPoolExecutor
genero, libro, hoja, *imgs = sys.argv[1:]
NIVEL = {"2": " The hair is only a very short, soft, thin light chestnut fuzz over the whole scalp: the skin of the head still shows through it; it is NOT a haircut, has no volume and no fringe.",
         "3": " The hair is a short, even baby haircut that fully covers the scalp, clearly more than a fuzz, not reaching the eyebrows."}[libro]
nene = ("Change ONLY the baby's hair so it matches exactly the hair of the baby in the second image (the approved character sheet): "
        "same amount, length, coverage of the scalp and light chestnut-brown color, keeping his big curl standing up above the forehead.")
nena = ("Change ONLY the baby girl's hair so it matches exactly the hair of the baby girl in the second image (the approved character sheet): "
        "same amount, length, coverage of the scalp and light chestnut-brown color, with her small tuft and the small coral flower clip on top.")
PROMPT = ("Edit the first image with minimal changes. " + (nene if genero == "varon" else nena) +
          NIVEL + " If the baby appears several times, change every copy. Keep EVERYTHING else exactly identical: the baby's face, expression, "
          "pose, clothes and size; the adults (same faces, light skin, hair and clothes); the ball, the room, the rug, the floor, "
          "the colors, the composition and the cut-paper style. No text.")
def subir(f):
    r = subprocess.run(["python3", "herramientas/subir.py", f], capture_output=True, text=True).stdout.strip()
    return r
def correr(f):
    url = subir(f); out = f[:-4] + "-pelo.png"
    r = subprocess.run(["python3", "herramientas/kie.py", "nano-banana-2", "auto", "2K", out, PROMPT, url, hoja], capture_output=True, text=True)
    return f, (r.stdout + r.stderr).strip()[-160:]
with ThreadPoolExecutor(8) as ex:
    for f, s in ex.map(correr, imgs): print(f, s, flush=True)
