#!/usr/bin/env python3
"""Pasa una tapa de KDP a una sola imagen JPEG a 400 dpi dentro de un PDF de la misma medida
(sin textos ni tipografías adentro). Así pasó la vista previa de KDP el recopilatorio 1 a 4 el 10/11/2026.
Uso: python3 maqueta/kdp_tapa_imagen.py kdp/bundle14-en-tapa.pdf 17.48 8.75   (lo reemplaza en el lugar)"""
import sys, subprocess, tempfile, os
import img2pdf

pdf, ancho, alto = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run(["pdftoppm", "-r", "400", "-jpeg", "-jpegopt", "quality=92", "-singlefile", pdf, f"{tmp}/tapa"], check=True)
    pagina = img2pdf.get_layout_fun((img2pdf.in_to_pt(ancho), img2pdf.in_to_pt(alto)))
    with open(pdf + ".nuevo", "wb") as f:
        f.write(img2pdf.convert([f"{tmp}/tapa.jpg"], layout_fun=pagina))
    os.replace(pdf + ".nuevo", pdf)
print("ok", pdf)
