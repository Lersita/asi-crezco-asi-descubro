#!/usr/bin/env python3
# Versión mujer del libro 3: edita cada imagen elegida de Tomi con Nano Banana 2 y la hoja de Emi.
# uso: emi_libro3.py URL_HOJA_EMI nombre=URL_IMAGEN_TOMI [...]   → ilustraciones/libro3-emi/nombre.png
import sys, subprocess
from concurrent.futures import ThreadPoolExecutor
hoja, *pares = sys.argv[1:]
PROMPT = ("Edit the first image with minimal changes: replace the baby boy with the baby girl from the character sheet "
  "(second image): same pose, same size, same position and same expression, but with her very short light baby fuzz, "
  "the thin little tuft and the small coral-pink flower hair clip on top of her head, tiny eyelashes. Same leaf-green "
  "bodysuit with the tiny colorful ball, same soft warm-grey long pants, barefoot, two tiny lower teeth when smiling. "
  "If there are several copies of the baby, change every one of them. Keep EVERYTHING else exactly identical: the adults "
  "(same faces, same light skin, same hair, same clothes), the ball, the room, the rug, the floor, the colors, the "
  "cut-paper style and the composition. No text.")
PROMPT_EXP = ("Edit the first image with minimal changes: the 6-year-old child crawling on the rug becomes a 6-year-old girl "
  "with short light chestnut hair and a small coral-pink flower hair clip, same green shirt, same pose. Keep everything else "
  "exactly identical, same cut-paper style. No text.")
def correr(par):
    nombre, url = par.split("=", 1)
    aspecto = "1:1" if nombre in ("p01", "p24") else "3:2" if nombre == "exp" else "21:9"
    refs = [url] if nombre == "exp" else [url, hoja]
    r = subprocess.run(["python3", "ilustraciones/herramientas/kie.py", "nano-banana-2", aspecto, "2K",
        f"ilustraciones/libro3-emi/{nombre}.png", PROMPT_EXP if nombre == "exp" else PROMPT, *refs], capture_output=True, text=True)
    return nombre, (r.stdout + r.stderr).strip()
with ThreadPoolExecutor(7) as ex:
    for n, s in ex.map(correr, pares): print(n, s, flush=True)
