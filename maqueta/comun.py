"""Piezas comunes de la maqueta: estilos y bloques de página.
Cada libro (libro1.py, libro2.py…) arma su lista de dobles y llama a escribir()."""
import html
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
B = "img/"
e = html.escape
COLS = ["#D9452B", "#EE8A2A", "#E9B21C", "#5E9E44", "#4FA3D9", "#8A5CB8"]

def palabra(txt, x, y, size=34, flecha=None):
    letras = "".join(f'<span style="color:{COLS[i % 6]}">{e(c)}</span>' for i, c in enumerate(txt))
    fl = ""
    if flecha:
        rot = 0 if flecha == "arriba" else 180
        fl = f'<svg class="flecha" viewBox="0 0 40 60" style="transform:rotate({rot}deg)"><path d="M20 4 L36 24 H26 V56 H14 V24 H4 Z" fill="#23304A"/></svg>'
    return f'<div class="palabra" style="left:{x}mm;top:{y}mm;font-size:{size}mm">{letras}{fl}</div>'

def numero(n, x, y, color):
    return f'<div class="num" style="left:{x-9}mm;top:{y}mm;background:{color}">{n}</div>'

def texto(t, x, y, w, size=None):
    st = f"left:{x}mm;top:{y}mm;width:{w}mm" + (f";font-size:{size}pt" if size else "")
    return f'<div class="txt" style="{st}">{e(t)}</div>'

def doble(img, extras, folios, pos="center", ajuste="cover"):
    """ajuste="contain" muestra la imagen entera (para las dobles con fondo crema liso)."""
    return (f'<section class="spread"><div class="art" style="background-image:url({B}{img});background-position:{pos};background-size:{ajuste}"></div>'
            f'<div class="fold"></div>{"".join(extras)}'
            f'<div class="folio izq">{folios[0]}</div><div class="folio der">{folios[1]}</div></section>')


def portada(img, titulo_html, n):
    return (f'''<section class="spread"><div class="guarda"></div>
<div class="page-r art" style="background-image:url({B}{img})"></div><div class="fold"></div>
<div class="cover-t"><div class="coleccion">Así crezco, así descubro</div>
<h1>{titulo_html}</h1><div class="autor">by LERSA</div><div class="badge"><span>Libro</span>{n}</div></div>
<div class="borrador">Borrador · ilustraciones de prueba</div></section>''')

def experimento(titulo_html, necesitas, pasos, img, columnas, objetos, nota, descubrimos):
    filas = "".join(f'<tr><td><i style="background:{COLS[i % 6]}"></i>{e(o)}</td>' + "<td></td>" * (len(columnas) - 1) + "</tr>"
                    for i, o in enumerate(objetos))
    cab = "".join(f"<th>{e(c)}</th>" for c in columnas)
    li = "".join(f"<li>{p}</li>" for p in pasos)
    return (f'''<section class="spread papel">
<div class="exp-izq"><div class="etiqueta">Experimento · para hacer con un adulto</div><h2>{titulo_html}</h2>
<p><b>Necesitás:</b> {e(necesitas)}</p><ol>{li}</ol><img src="{B}{img}"></div>
<div class="exp-der"><table><tr>{cab}</tr>{filas}</table><p class="nota">{e(nota)}</p>
<div class="descubrimos"><b>Qué descubrimos</b>{e(descubrimos)}</div></div>
<div class="fold"></div><div class="folio izq">22</div><div class="folio der">23</div></section>''')

def grandes(img, parrafos):
    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in parrafos)
    return (f'''<section class="spread"><div class="page-l art" style="background-image:url({B}{img})"></div><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')

CSS = """@page{size:432mm 216mm;margin:0}*{box-sizing:border-box}
:root{--grano:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 .45 0 0 0 0 .32 0 0 0 0 .18 0 0 0 .09 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
body{margin:0;font-family:Andika,sans-serif;color:#23304A}
.spread{width:432mm;height:216mm;position:relative;overflow:hidden;page-break-after:always;background:#FFF9E7}
.art{position:absolute;inset:0;background-size:cover;background-repeat:no-repeat}
.page-r{left:216mm}.page-l{right:216mm}
.fold{position:absolute;left:206mm;width:20mm;top:0;bottom:0;pointer-events:none;
 background:linear-gradient(90deg,rgba(0,0,0,0) 0,rgba(60,40,20,.10) 45%,rgba(60,40,20,.18) 50%,rgba(60,40,20,.10) 55%,rgba(0,0,0,0) 100%)}
.txt{position:absolute;font-size:22pt;line-height:1.27;padding:4.5mm 7mm 5mm;width:fit-content;isolation:isolate;filter:drop-shadow(0 .5mm .9mm rgba(70,45,20,.28))}
.txt::before{content:"";position:absolute;inset:0;z-index:-1;background:#FFF8E8 var(--grano);
 clip-path:polygon(0.8% 6%,18% 1.5%,41% 3.5%,63% 0.5%,86% 3%,99.4% 0%,98.6% 34%,100% 68%,98.8% 97%,77% 99.2%,52% 96.8%,29% 100%,6% 97.5%,0% 99%,1.2% 62%,0% 30%)}
.palabra{position:absolute;font-family:Fraunces,serif;font-weight:900;letter-spacing:.02em;line-height:1;display:flex;align-items:center;gap:3mm;
 text-shadow:.5mm .7mm 0 rgba(70,45,20,.22)}
.flecha{height:.9em;filter:drop-shadow(.5mm .7mm 0 rgba(70,45,20,.22))}
.num{position:absolute;width:18mm;height:18mm;border-radius:50%;color:#fff;font-family:Fraunces,serif;font-weight:800;font-size:12mm;
 display:flex;align-items:center;justify-content:center;box-shadow:.5mm .8mm 0 rgba(70,45,20,.25)}
.folio{position:absolute;bottom:6mm;font-family:Fraunces,serif;font-size:9pt;color:#8A7562}.folio.izq{left:10mm}.folio.der{right:10mm}
.guarda{position:absolute;left:0;top:0;width:216mm;height:216mm;background-color:#23304A;
 background-image:var(--grano),radial-gradient(circle at 25% 25%,rgba(233,178,28,.55) 0 2.2mm,transparent 2.4mm),radial-gradient(circle at 75% 75%,rgba(79,163,217,.45) 0 2.2mm,transparent 2.4mm);background-size:auto,36mm 36mm,36mm 36mm}
.guarda.der{left:216mm}
.cover-t{position:absolute;left:216mm;top:0;width:216mm;padding:16mm 16mm 0}
.coleccion{font-family:Fraunces,serif;font-weight:600;font-size:12pt;letter-spacing:.22em;text-transform:uppercase;color:#C4532E}
h1{font-family:Fraunces,serif;font-weight:800;font-size:60pt;line-height:1;margin:4mm 0 0;color:#23304A;letter-spacing:-.01em}
.autor{display:inline-block;font-family:Fraunces,serif;font-weight:700;font-size:13pt;letter-spacing:.12em;color:#C4532E;margin-top:3mm;padding:1.2mm 3.5mm;background:#FFF8E8;border-radius:1.5mm;box-shadow:0 .5mm 1mm rgba(70,45,20,.2)}
.badge{position:absolute;right:16mm;top:16mm;width:22mm;height:22mm;border-radius:50%;background:conic-gradient(#D9452B 0 60deg,#EE8A2A 0 120deg,#E9B21C 0 180deg,#5E9E44 0 240deg,#4FA3D9 0 300deg,#8A5CB8 0 360deg);
 display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:900;font-size:13mm;color:#fff;text-shadow:0 .5mm 1mm rgba(0,0,0,.35);line-height:.9}
.badge span{font-size:3mm;letter-spacing:.15em;text-transform:uppercase}
.borrador{position:absolute;left:12mm;bottom:8mm;font-size:8pt;color:#8A7562;background:#FFF9E7;padding:1mm 3mm;border-radius:2mm}
.papel{background:#FFF9E7 var(--grano)}
.exp-izq{position:absolute;left:0;top:0;width:216mm;height:216mm;padding:14mm 16mm}
.exp-der{position:absolute;left:216mm;top:0;width:216mm;height:216mm;padding:16mm 16mm}
.etiqueta{display:inline-block;font-family:Fraunces,serif;font-weight:700;font-size:9pt;letter-spacing:.16em;text-transform:uppercase;color:#fff;background:#C4532E;padding:1.5mm 3.5mm;border-radius:1.5mm}
h2{font-family:Fraunces,serif;font-weight:800;font-size:26pt;line-height:1.02;margin:3mm 0 3mm}
.exp-izq p,.exp-izq li{font-size:10.5pt;line-height:1.38;margin:0 0 1.5mm}.exp-izq ol{margin:1mm 0 0;padding-left:5mm}
.exp-izq img{position:absolute;left:18mm;bottom:9mm;width:150mm;border-radius:2mm}
table{width:100%;border-collapse:separate;border-spacing:0;font-size:11pt;border-radius:3mm;overflow:hidden;box-shadow:0 .6mm 2mm rgba(70,45,20,.15)}
th{background:#23304A;color:#fff;font-family:Fraunces,serif;font-weight:700;text-align:left;padding:3mm}
td{background:#fff;padding:2.9mm 3mm;border-bottom:1px solid #EFE4CF}td:first-child{width:40%}
td i{display:inline-block;width:3mm;height:3mm;border-radius:50%;margin-right:2.5mm;vertical-align:middle}
.nota{font-size:9.5pt;color:#6E5F52;margin:2.5mm 0 6mm}
.descubrimos{background:#E9F1E4;border-left:2mm solid #5E9E44;border-radius:2mm;padding:4mm 5mm;font-size:10.5pt;line-height:1.42}
.descubrimos b{display:block;font-family:Fraunces,serif;font-size:13pt;margin-bottom:1.5mm;color:#3E7A2C}
.grandes{position:absolute;left:10mm;top:10mm;width:196mm;padding:7mm 8mm 5mm;background:rgba(255,249,234,.94);border-radius:2mm}
.grandes p{font-size:9.6pt;line-height:1.38;margin:0 0 2mm}.grandes .etiqueta{margin-bottom:3mm;background:#23304A}
"""

def escribir(nombre, titulo, S):
    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{e(titulo)}</title>
<link href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800;9..144,900&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{''.join(S)}</body></html>"""
    (RAIZ / "maqueta" / f"{nombre}.html").write_text(doc, encoding="utf-8")
    print("ok", nombre)

# Viñeta de la página 24 cuando la ilustración no deja lugar arriba para el texto
CSS += """.vineta{position:absolute;left:38mm;bottom:6mm;width:140mm;
 -webkit-mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 70%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 70%,transparent 100%)}
"""
