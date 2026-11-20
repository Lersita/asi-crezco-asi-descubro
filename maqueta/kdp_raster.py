#!/usr/bin/env python3
"""Arma el PDF interior de KDP con una imagen por página (400 dpi, 8,625 × 8,75 pulgadas exactas).
Las imágenes salen de maqueta/kdp_capturas.js (fotos de la página en pantalla): el modo de impresión
del navegador achicaba el contenido y KDP lo mostraba en un rincón.
Uso: python3 maqueta/kdp_raster.py maqueta/kdp-libroN-xx.html kdp/libroN-xx-interior.pdf"""
import sys, subprocess, tempfile, glob
from PIL import Image
entrada, salida = sys.argv[1], sys.argv[2]
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run(["node", "maqueta/kdp_capturas.js", entrada, tmp], check=True)
    paginas = []
    for f in sorted(glob.glob(f"{tmp}/p*.png")):
        im = Image.open(f).convert("RGB")
        if im.size != (3450, 3500):
            print("ajuste de tamaño", f, im.size)
            im = im.resize((3450, 3500), Image.LANCZOS)
        paginas.append(im)
    assert len(paginas) == 24, len(paginas)
    paginas[0].save(salida, save_all=True, append_images=paginas[1:], resolution=400, quality=92)
print(salida, len(paginas), "páginas")
