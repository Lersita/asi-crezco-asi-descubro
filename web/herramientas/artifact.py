"""Arma la versión para publicar como Artifact de Claude: sin la envoltura del documento
y sin los bloques marcados <!--solo-web--> (la descarga no funciona dentro del Artifact).
Uso: python3 web/herramientas/artifact.py  ->  web/_artifact.html"""
import re
from pathlib import Path
WEB = Path(__file__).resolve().parent.parent
s = (WEB / "index.html").read_text(encoding="utf-8")
s = re.sub(r"<!--solo-web-->.*?<!--/solo-web-->\n?", "", s, flags=re.S)
s = re.sub(r"<!--artifact:(.*?)-->", r"\1", s, flags=re.S)
for etiqueta in ['<!doctype html>', '<html lang="es">', '<head>', '<meta charset="utf-8">',
                 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">', '</head>', '<body>', '</body>', '</html>']:
    s = s.replace(etiqueta + "\n", "", 1)
(WEB / "_artifact.html").write_text(s, encoding="utf-8")
print("ok")
