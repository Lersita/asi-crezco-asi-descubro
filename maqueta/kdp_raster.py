#!/usr/bin/env python3
"""Convierte el PDF interior de KDP en un PDF de imágenes a 400 dpi (una imagen por página).
KDP no interpreta bien los PDF que arma el navegador (dibuja el contenido más chico); con imágenes
no hay nada que interpretar. A 400 dpi, 8,625 × 8,75 pulgadas son exactamente 3450 × 3500 píxeles.
Uso: python3 maqueta/kdp_raster.py entrada.pdf salida.pdf"""
import sys, subprocess, tempfile, glob
from PIL import Image
entrada, salida = sys.argv[1], sys.argv[2]
DPI = 400
with tempfile.TemporaryDirectory() as tmp:
    # 4 tandas en paralelo (una por procesador): mucho más rápido que de a una página
    procs = [subprocess.Popen(["pdftoppm", "-r", str(DPI), "-png", "-f", str(a), "-l", str(a + 5), entrada, f"{tmp}/p"]) for a in (1, 7, 13, 19)]
    for pr in procs:
        assert pr.wait() == 0
    paginas = []
    for f in sorted(glob.glob(f"{tmp}/p-*.png")):
        im = Image.open(f).convert("RGB")
        if im.size != (3450, 3500):
            im = im.resize((3450, 3500), Image.LANCZOS)
        paginas.append(im)
    paginas[0].save(salida, save_all=True, append_images=paginas[1:], resolution=DPI, quality=92)
print(salida, len(paginas), "páginas")
