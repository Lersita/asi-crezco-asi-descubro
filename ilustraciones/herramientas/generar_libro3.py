#!/usr/bin/env python3
# Genera las páginas del libro 3 (versión varón) a partir de libros/03-gatear/ilustraciones.md.
# uso: generar_libro3.py URL_HOJA URL_PORTADA [nombre ...]   (sin nombres: todas)
import re, sys, subprocess
from concurrent.futures import ThreadPoolExecutor
hoja, portada, *solo = sys.argv[1:]
md = open("libros/03-gatear/ilustraciones.md").read()
estilo = open("ilustraciones/herramientas/style-libro3.txt").read().strip()
reglas = re.search(r"\*\*\[REGLAS\]\*\*\n```\n(.*?)\n```", md, re.S).group(1).strip()
bloques = re.findall(r"## (Página[s]? [\d–]+)[^\n]*\n```\n(.*?)\n```", md, re.S)
nombres = ["p01", "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10", "exp", "p24"]
def correr(par):
    nombre, prompt = par
    prompt = prompt.replace("[ESTILO]", estilo).replace("[REGLAS]", reglas)
    aspecto = "1:1" if nombre in ("p01", "p24") else "3:2" if nombre == "exp" else "21:9"
    refs = [portada] if nombre == "exp" else [hoja, portada]
    r = subprocess.run(["python3", "ilustraciones/herramientas/kie.py", "nano-banana-pro", aspecto, "2K",
                        f"ilustraciones/libro3/{nombre}-v1.png", prompt, *refs], capture_output=True, text=True)
    return nombre, (r.stdout + r.stderr).strip()
trabajos = [(n, p) for n, (_, p) in zip(nombres, bloques) if not solo or n in solo]
with ThreadPoolExecutor(7) as ex:
    for n, salida in ex.map(correr, trabajos): print(n, salida, flush=True)
