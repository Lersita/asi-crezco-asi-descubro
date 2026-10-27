#!/usr/bin/env python3
# Versión mujer del libro 4: edita cada imagen elegida de Tomi con Nano Banana 2 y la hoja de Emi.
# uso: emi_libro3.py URL_HOJA_EMI nombre=URL_IMAGEN_TOMI [...]   → ilustraciones/libro4-emi/nombre.png
import sys, subprocess
from concurrent.futures import ThreadPoolExecutor
hoja, *pares = sys.argv[1:]
PROMPT = ("Edit the first image with minimal changes: replace the baby boy with the baby girl from the character sheet "
  "(second image): same pose, same size, same position and same expression, with the same softly messy light chestnut-brown "
  "hair, tiny eyelashes and a small hair clip with a coral-pink flower on one side of her head, just above the ear. No ponytail, "
  "no tuft on top, no headband. Same leaf-green t-shirt with the tiny colorful ball, same white diaper, barefoot, four tiny teeth "
  "when smiling. If there are several copies of the baby, change every one of them. Keep EVERYTHING else exactly identical: the "
  "adults (same faces, same light skin, same hair, same clothes), the ball, the sofa, the room, the rug, the floor, the arrows, "
  "the colors, the cut-paper style and the composition. The second image is ONLY a character reference: never copy its layout, "
  "poses or extra figures into the page. No text.")
PROMPT_EXP = ("Edit the first image with minimal changes: the 6-year-old child becomes a 6-year-old girl with short light "
  "chestnut hair and a small coral-pink flower hair clip, same green shirt, same pose. Keep everything else exactly identical, "
  "same cut-paper style. No text.")
def correr(par):
    nombre, url = par.split("=", 1)
    aspecto = "1:1" if nombre in ("p01", "p24") else "3:2" if nombre == "exp" else "21:9"
    refs = [url] if nombre == "exp" else [url, hoja]
    r = subprocess.run(["python3", "ilustraciones/herramientas/kie.py", "nano-banana-2", aspecto, "2K",
        f"ilustraciones/libro4-emi/{nombre}.png", PROMPT_EXP if nombre == "exp" else PROMPT, *refs], capture_output=True, text=True)
    return nombre, (r.stdout + r.stderr).strip()
with ThreadPoolExecutor(7) as ex:
    for n, s in ex.map(correr, pares): print(n, s, flush=True)
