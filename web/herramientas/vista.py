"""Arma las imágenes del visor de la web a partir de las plantillas del PDF.
Las primeras 4 dobles se guardan nítidas; desde la quinta, ya borrosas
(así la imagen nítida nunca llega a la página).
Uso, desde la raíz del repositorio: python3 web/herramientas/vista.py"""
from pathlib import Path
from PIL import Image, ImageFilter
WEB = Path(__file__).resolve().parent.parent
LIBRES = 4
for carpeta in sorted((WEB / "plantillas").iterdir()):
    if not carpeta.is_dir(): continue
    destino = WEB / "vista" / carpeta.name; destino.mkdir(parents=True, exist_ok=True)
    for f in sorted(carpeta.glob("d*.jpg")):
        im = Image.open(f).convert("RGB"); i = int(f.stem[1:])
        if i < LIBRES:
            im.resize((1600, 800), Image.LANCZOS).save(destino / f.name, quality=78, optimize=True, progressive=True)
        else:
            im = im.resize((320, 160), Image.LANCZOS).filter(ImageFilter.GaussianBlur(5))
            im.resize((800, 400), Image.LANCZOS).save(destino / f.name, quality=70, optimize=True)
    print(carpeta.name, len(list(destino.glob("*.jpg"))))
