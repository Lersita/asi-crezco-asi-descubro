#!/usr/bin/env python3
"""Rearma un interior de KDP armado uniendo PDF (recopilatorios, colección) como un PDF nuevo y simple:
saca la foto JPEG de cada página tal cual (sin volver a comprimir) y la pone en una página de 8,625 × 8,75 in.
Se hizo el 10/11/2026 porque KDP dio "Error processing interior" con el recopilatorio unido con pypdf;
los libros sueltos, que son un PDF de fotos simple, pasaron sin problema.
Uso: python3 maqueta/kdp_limpiar.py kdp/bundle14-en-interior.pdf   (lo reemplaza en el lugar)
Necesita: pip install img2pdf, y pdfimages (poppler)."""
import sys, glob, subprocess, tempfile, os
import img2pdf

entrada = sys.argv[1]
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run(["pdfimages", "-j", entrada, f"{tmp}/p"], check=True)
    fotos = sorted(glob.glob(f"{tmp}/p-*.jpg"))
    paginas = int(subprocess.run(["pdfinfo", entrada], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0])
    assert len(fotos) == paginas, (len(fotos), paginas)
    pagina = img2pdf.get_layout_fun((img2pdf.in_to_pt(8.625), img2pdf.in_to_pt(8.75)))
    salida = entrada + ".nuevo"
    with open(salida, "wb") as f:
        f.write(img2pdf.convert(fotos, layout_fun=pagina))
    os.replace(salida, entrada)
print("ok", entrada, paginas, "páginas")
