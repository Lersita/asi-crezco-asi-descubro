#!/usr/bin/env python3
"""Fija el tamaño exacto de cada página de un PDF (el navegador redondea unas centésimas de punto).
Uso: python3 maqueta/kdp_medida.py archivo.pdf ANCHO_PULGADAS ALTO_PULGADAS"""
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
ruta, w, h = sys.argv[1], float(sys.argv[2]) * 72, float(sys.argv[3]) * 72
r = PdfReader(ruta); out = PdfWriter()
for p in r.pages:
    caja = RectangleObject([0, 0, w, h])
    p.mediabox = caja; p.cropbox = caja; p.trimbox = caja; p.bleedbox = caja
    out.add_page(p)
with open(ruta, "wb") as f: out.write(f)
print(ruta, f"{w:.2f} x {h:.2f} pt")
