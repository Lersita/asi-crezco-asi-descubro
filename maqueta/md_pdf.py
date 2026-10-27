#!/usr/bin/env python3
"""Pasa un documento Markdown a HTML imprimible (para hacer un PDF con maqueta/kdp_pdf.js en tamaño carta).
Uso: python3 maqueta/md_pdf.py entrada.md salida.html"""
import sys, markdown
md = open(sys.argv[1], encoding="utf-8").read()
cuerpo = markdown.markdown(md, extensions=["tables"])
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:8.5in 11in;margin:.7in}} body{{font:11pt/1.5 Georgia,serif;color:#222;margin:0}}
h1{{font-size:20pt;color:#23304A}} h2{{font-size:15pt;color:#C4532E;border-bottom:1px solid #ddd;padding-bottom:3px;margin-top:22px}} h3{{font-size:12.5pt;color:#23304A}}
table{{border-collapse:collapse;width:100%;margin:8px 0;font-size:10pt}} th,td{{border:1px solid #ccc;padding:5px 7px;vertical-align:top;text-align:left}} th{{background:#F3EDE2}}
blockquote{{margin:8px 0;padding:8px 14px;background:#F7F4EE;border-left:4px solid #5E9E44}} code{{background:#F3EDE2;padding:1px 4px;border-radius:3px;font-size:9.5pt}}
hr{{border:0;border-top:1px solid #ddd;margin:18px 0}} tr{{page-break-inside:avoid}}
</style></head><body>{cuerpo}</body></html>"""
open(sys.argv[2], "w", encoding="utf-8").write(html)
