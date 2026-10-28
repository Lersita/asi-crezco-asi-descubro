#!/usr/bin/env python3
# Segunda corrección del pelo (28/10/2026): baja el pelo de Tomi en las páginas de los libros 3 y 4 con Nano Banana 2.
# uso: pelo2.py N URL_HOJA nombre=URL_IMAGEN [...]  → ilustraciones/libroN/<nombre>-pelo2.png
import sys, subprocess
from concurrent.futures import ThreadPoolExecutor
n, hoja, *pares = sys.argv[1:]
PELO = {
  "3": "a soft, fine, light chestnut-brown baby fuzz that lies flat and close to the scalp, so the round shape of the head is clearly visible and the scalp shows through a little; no locks, no fringe, no volume; keep the single brown curl standing up on top of the head",
  "4": "very short, fine and thin light chestnut-brown baby hair lying flat close to the scalp, so the round shape of the head is clearly visible; a few tiny wisps at the forehead, no fringe, no volume, no long locks, not covering the ears; no curl on top",
}[n]
PROMPT = ("Edit the first image with minimal changes: change ONLY the hair of the baby boy so it matches the character sheet "
  f"(second image): {PELO}. If there are several copies of the baby, change every one of them. Keep EVERYTHING else exactly "
  "identical: the baby's face, eyes, teeth, expression, pose, size, position and clothes; the adults (same faces, same light skin, "
  "same hair, same clothes); the ball, the sofa, the room, the rug, the floor, any arrows or dotted lines, the colors, the "
  "cut-paper style and the composition. The second image is ONLY a hair and face reference: never copy its layout, poses or "
  "extra figures into the page. No text.")
def correr(par):
    nombre, url = par.split("=", 1)
    aspecto = "1:1" if nombre.startswith(("p01", "p24")) else "3:2" if nombre.startswith("exp") else "21:9"
    r = subprocess.run(["python3", "ilustraciones/herramientas/kie.py", "nano-banana-2", aspecto, "2K",
        f"ilustraciones/libro{n}/{nombre}-pelo2.png", PROMPT, url, hoja], capture_output=True, text=True)
    return nombre, (r.stdout + r.stderr).strip()[-160:]
with ThreadPoolExecutor(7) as ex:
    for k, s in ex.map(correr, pares): print(k, s, flush=True)
