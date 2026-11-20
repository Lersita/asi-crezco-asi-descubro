#!/usr/bin/env python3
"""Vuelve a comprimir un interior de KDP (una foto JPEG por página, 400 dpi) con otra calidad, para que pese menos.
Uso: python3 maqueta/kdp_achicar.py entrada.pdf salida.pdf 82   (la colección de 11 pasa de unos 400 MB a unos 270 MB)"""
import sys, pypdf, io
from PIL import Image
src, dst, q = sys.argv[1], sys.argv[2], int(sys.argv[3])
r = pypdf.PdfReader(src)
pags = []
for i, p in enumerate(r.pages):
    ims = p.images
    assert len(ims) == 1, (i, len(ims))
    im = ims[0].image.convert("RGB")
    assert im.size == (3450, 3500), im.size
    b = io.BytesIO(); im.save(b, "JPEG", quality=q); b.seek(0)
    pags.append(Image.open(b))
pags[0].save(dst, save_all=True, append_images=pags[1:], resolution=400, quality=q)
print(dst, len(pags))
