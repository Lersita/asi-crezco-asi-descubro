#!/usr/bin/env python3
"""Arma la maqueta del libro 1 en HTML (una página del PDF = una doble abierta).
Uso: python3 maqueta/libro1.py  ->  maqueta/libro1.html"""
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

def doble(img, extras, folios, pos="center"):
    return (f'<section class="spread"><div class="art" style="background-image:url({B}{img});background-position:{pos}"></div>'
            f'<div class="fold"></div>{"".join(extras)}'
            f'<div class="folio izq">{folios[0]}</div><div class="folio der">{folios[1]}</div></section>')

S = []
# Tapa interior: guarda a la izquierda, portada a la derecha
S.append(f'''<section class="spread"><div class="guarda"></div>
<div class="page-r art" style="background-image:url({B}p01-portada-emi.jpg)"></div><div class="fold"></div>
<div class="cover-t"><div class="coleccion">Así crezco, así descubro</div>
<h1>Emi aprende<br>a girar</h1><div class="badge"><span>Libro</span>1</div></div>
<div class="borrador">Borrador · ilustraciones de prueba</div></section>''')

S.append(doble("d01-emi.jpg", [texto("Me llamo Emi. Soy chiquita, muy chiquita.", 18, 16, 150),
    texto("Todavía no me siento, no gateo y no camino. Pero hoy voy a aprender algo nuevo.", 232, 14, 118)], (2, 3)))
S.append(doble("d02-v4.jpg", [texto("Estoy boca arriba.", 128, 26, 74),
    palabra("ARRIBA", 62, 116, 17, "arriba"),
    texto("Arriba veo el techo, la lámpara y la cara de mamá.", 230, 30, 84)], (4, 5)))
S.append(doble("d03-emi.jpg", [texto("Esta es Rula, mi pelota. Es redonda, blandita y de muchos colores.", 18, 14, 160),
    texto("Está ahí, al costado. ¡La quiero agarrar!", 300, 188, 116, 19)], (6, 7)))
S.append(doble("d04-emi-compuesta.jpg", [texto("Uno: estiro el brazo. No llego.", 18, 18, 180),
    texto("Dos: levanto una pierna. Tres: giro la cabeza para el costado.", 234, 18, 180),
    numero(1, 108, 70, COLS[0]), numero(2, 271, 70, COLS[2]), numero(3, 377, 70, COLS[4])], (8, 9)))
S.append(doble("d05-emi.jpg", [texto("Mi cabeza va para un lado. Después, mis hombros.", 18, 14, 150),
    texto("Y el resto de mi cuerpo los sigue. ¡Me estoy dando vuelta!", 230, 14, 105)], (10, 11)))
S.append(doble("d06-emi-v2.jpg", [texto("¡PLAF! Ahora estoy boca abajo.", 18, 16, 160),
    palabra("ABAJO", 30, 46, 22, "abajo"),
    texto("Abajo veo la manta y el piso. ¡Di media vuelta!", 232, 14, 112)], (12, 13)))
S.append(doble("d07-emi.jpg", [texto("Toco a Rula con la mano y Rula se va rodando.", 40, 12, 150),
    texto("Rula es redonda. Las cosas redondas ruedan.", 240, 12, 160)], (14, 15)))
S.append(doble("d08-emi.jpg", [texto("Al lado hay un cubo de juguete. Lo empujo y se queda quieto.", 112, 12, 92, 19),
    texto("El cubo tiene lados planos. Las cosas con lados planos no ruedan.", 228, 12, 112, 19)], (16, 17)))
S.append(doble("d09-emi.jpg", [texto("En el piso hay muchas cosas.", 18, 6, 150, 19),
    texto("¿Cuáles ruedan y cuáles no? ¿Vos qué decís?", 232, 6, 186, 19)], (18, 19)))
S.append(doble("d10-emi-compuesta.jpg", [texto("Quiero llegar a Rula. Giro una vez, giro dos veces, giro tres veces. ¡La alcancé!", 18, 16, 182),
    numero(1, 37, 98, COLS[0]), numero(2, 107, 98, COLS[2]), numero(3, 177, 98, COLS[4]),
    texto("Hoy aprendí a girar. ¿Vos también girabas así cuando eras bebé? Ahora quiero ver todo desde más arriba… ¿qué voy a aprender?", 226, 160, 190, 19)], (20, 21)))

filas = "".join(f'<tr><td><i style="background:{COLS[i % 6]}"></i>{o}</td><td></td><td></td></tr>' for i, o in enumerate(
    ["Pelota", "Naranja", "Rollo acostado", "Rollo parado", "Tapa de canto", "Tapa acostada", "Caja", "Botella acostada"]))
S.append(f'''<section class="spread papel">
<div class="exp-izq"><div class="etiqueta">Experimento · para hacer con un adulto</div><h2>¿Qué rueda<br>y qué no?</h2>
<p><b>Necesitás:</b> un libro grande apoyado sobre uno o dos libros (una rampa bajita), una pelota, una naranja, un rollo de papel higiénico vacío, una tapa de frasco, una caja chica y una botella de plástico vacía y tapada.</p>
<ol><li>Armá la rampa con un adulto. Que quede bajita.</li><li>Antes de soltar cada cosa, adiviná: ¿rueda, se desliza o se queda quieta? Anotalo en la tabla.</li>
<li>Soltá cada cosa arriba de la rampa, sin empujarla.</li><li>Anotá lo que pasó.</li>
<li><b>Desafío:</b> probá el rollo acostado y después parado. Hacé lo mismo con la tapa. ¿Qué cambia?</li></ol>
<img src="{B}exp-emi.jpg"></div>
<div class="exp-der"><table><tr><th>Objeto</th><th>Yo creo que…</th><th>Lo que pasó</th></tr>{filas}</table>
<p class="nota">En cada casillero escribí o dibujá: rueda, se desliza o se queda quieta.</p>
<div class="descubrimos"><b>Qué descubrimos</b>Las cosas redondas tocan el piso en un puntito o en una rayita finita, y ruedan con poquito. Las que tienen lados planos se apoyan en una cara entera: se quedan quietas o, si la rampa es empinada, se deslizan sin rodar. El rollo y la tapa son redondos de un lado y planos del otro: ruedan según cómo los apoyes.</div></div>
<div class="fold"></div><div class="folio izq">22</div><div class="folio der">23</div></section>''')

S.append(f'''<section class="spread"><div class="page-l art" style="background-image:url({B}p24-emi.jpg)"></div><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>
<p><b>El concepto.</b> Rodar es girar alrededor de un eje. Una pelota toca el piso en un solo punto, y el menor empujón la hace girar. Un cubo apoya una cara entera: para darlo vuelta hay que levantarlo por encima de un borde. El bebé hace lo mismo que la pelota: gira alrededor de una línea imaginaria que va de la cabeza a los pies. Cuando lleva la cabeza y el hombro más allá de su base de apoyo, su propio peso termina el giro.</p>
<p><b>El hito.</b> Muchos bebés empiezan a girar entre los 4 y los 6 meses, más o menos. Muchas veces aparece primero de boca abajo a boca arriba, pero no siempre. Cada bebé tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra.</p>
<p><b>Seguridad.</b> Cuando un bebé empieza a girar, ya no se lo deja solo en la cama, el cambiador o el sillón. El lugar más seguro para jugar es el piso. Para dormir, siempre boca arriba.</p>
<p><b>Para charlar después de leer:</b> ¿Qué otras cosas redondas hay en casa? ¿Por qué las ruedas de los autos son redondas y no cuadradas? ¿Cómo eras vos de bebé? Busquen juntos una foto.</p></div>
<div class="folio izq">24</div></section>''')

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
doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Emi aprende a girar</title>
<link href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800;9..144,900&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{''.join(S)}</body></html>"""
(RAIZ / "maqueta" / "libro1-emi.html").write_text(doc, encoding="utf-8")
print("ok")
