#!/usr/bin/env python3
# Genera las páginas de un libro (versión varón) a partir de libros/NN-*/ilustraciones.md.
# uso: generar_libro.py N URL_HOJA URL_REFERENCIA_ESTILO[,URL_SET...] [nombre ...]   (sin nombres: todas)
# Guarda en ilustraciones/libroN/<nombre>-v1.png. Estilo: herramientas/style-libroN.txt
import re, sys, subprocess, glob
from concurrent.futures import ThreadPoolExecutor
n, hoja, estilo_ref, *solo = sys.argv[1:]
md = open(glob.glob(f"libros/{int(n):02d}-*/ilustraciones.md")[0]).read()
estilo = open(f"ilustraciones/herramientas/style-libro{n}.txt").read().strip()
reglas = re.search(r"\*\*\[REGLAS\]\*\*\n```\n(.*?)\n```", md, re.S).group(1).strip()
bloques = re.findall(r"## (Página[s]? [\d–]+)[^\n]*\n```\n(.*?)\n```", md, re.S)
nombres = ["p01", "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10", "exp", "p24"]
assert len(bloques) == 13, len(bloques)
def correr(par):
    nombre, prompt = par
    prompt = prompt.replace("[ESTILO]", estilo).replace("[REGLAS]", reglas)
    aspecto = "1:1" if nombre in ("p01", "p24") else "3:2" if nombre == "exp" else "21:9"
    extra = estilo_ref.split(",")
    refs = [extra[0]] if nombre == "exp" else [hoja, *extra]
    r = subprocess.run(["python3", "ilustraciones/herramientas/kie.py", "nano-banana-pro", aspecto, "2K",
                        f"ilustraciones/libro{n}/{nombre}-v1.png", prompt, *refs], capture_output=True, text=True)
    return nombre, (r.stdout + r.stderr).strip()[-200:]
trabajos = [(k, p) for k, (_, p) in zip(nombres, bloques) if not solo or k in solo]
with ThreadPoolExecutor(7) as ex:
    for k, salida in ex.map(correr, trabajos): print(k, salida, flush=True)
