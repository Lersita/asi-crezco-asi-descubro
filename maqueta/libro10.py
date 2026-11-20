#!/usr/bin/env python3
"""Maqueta del libro 10 (versión varón; la versión mujer queda para más adelante).
Uso: python3 maqueta/libro10.py -> maqueta/libro10.html
Las palabras grandes (FLOTA, SE HUNDE, LLENO, VACÍO) y los diez vasitos de la doble 8 se dibujan acá
(la IA no dibuja textos ni cosas para contar). En algunas dobles se corre el encuadre para alejar caras del pliegue."""
from comun import B, e, texto, doble, portada, experimento, escribir
from comun import palabra as _palabra


def palabra(*a, **k):
    """Palabra grande con un borde blanco suave, para que se lea sobre el agua y los árboles."""
    return _palabra(*a, **k).replace('style="', 'style="text-shadow:0 0 1.2mm #fff,0 0 2.4mm #fff,0 0 3.5mm rgba(255,255,255,.9);', 1)

AGUA, AZUL = "#4FA3D9", "#23304A"


def vaso(x, y, n):
    """Vasito con agua y su número, centrado en x, y (mm)."""
    svg = (f'<svg viewBox="0 0 20 24" width="11mm" height="13mm"><path d="M2 2 H18 L15.5 22 H4.5 Z" fill="#fffdf8" stroke="{AZUL}" stroke-width="1.4" stroke-linejoin="round"/>'
           f'<path d="M3.3 9 H16.7 L15.5 22 H4.5 Z" fill="{AGUA}" opacity=".85"/></svg>')
    num = (f'<div style="font-family:Fraunces,serif;font-weight:800;font-size:4.6mm;line-height:5mm;color:{AZUL};'
           f'text-align:center;margin-top:.6mm;text-shadow:0 0 1.5mm #fff,0 0 1.5mm #fff">{n}</div>')
    return (f'<div style="position:absolute;left:{x - 5.5}mm;top:{y - 6.5}mm;width:11mm;'
            f'filter:drop-shadow(.3mm .5mm 0 rgba(70,45,20,.25))">{svg}{num}</div>')


def armar(nombre, I):
    S = [portada(f"{I}p01.jpg", f"{nombre} aprende<br>a nadar", 10)]

    S.append(doble(f"{I}d01.jpg", [texto(f"Soy {nombre}. Ya sé girar, sentarme, gatear, pararme, caminar, correr, saltar, subir la escalera y tirar una pelota.", 24, 8, 180, 16),
        texto("Hoy vamos a la pileta con mamá y papá. ¡Hoy voy a aprender a nadar!", 226, 12, 130)], (2, 3)))
    S.append(doble(f"{I}d02.jpg", [texto("Bajo por la escalera, despacito. ¡Uy, qué fría está el agua!", 24, 12, 150),
        texto("Papá me espera adentro. Con él, me animo.", 226, 12, 120)], (4, 5)))
    S.append(doble(f"{I}d03.jpg", [texto("Suelto a Rula en el agua. ¿Se va a hundir?", 24, 12, 140),
        palabra("FLOTA", 236, 128, 14),
        texto("¡No! Rula FLOTA. Es grande, pero adentro está llena de aire.", 226, 12, 130)], (6, 7)))
    S.append(doble(f"{I}d04.jpg", [texto("Papá tira un aro de colores al agua. ¡PLUF!", 24, 12, 140),
        palabra("SE HUNDE", 40, 184, 11),
        texto("El aro SE HUNDE hasta el fondo. Pongo la cara con las antiparras… ¡y lo veo allá abajo!", 226, 12, 140)], (8, 9)))
    S.append(doble(f"{I}d05.jpg", [texto("Papá me pone las manos en la espalda. Me acuesto boca arriba, miro el cielo y lleno de aire los pulmones…", 24, 12, 170),
        texto("¡Floto! Con mucho aire adentro, floto como Rula.", 226, 12, 120)], (10, 11)))
    S.append(doble(f"{I}d06.jpg", [texto("Mamá me da una tabla. Me agarro fuerte y pateo con las piernas estiradas.", 24, 12, 160),
        texto("¡CHAP, CHAP, CHAP! Avanzo hasta los brazos de mamá.", 226, 12, 130)], (12, 13), pos="right"))
    S.append(doble(f"{I}d07.jpg", [texto("En el borde hay un balde. Lo lleno de agua: está LLENO.", 24, 12, 150),
        palabra("LLENO", 96, 82, 11),
        texto("Lo doy vuelta y… ¡SPLASH! Ahora está VACÍO.", 226, 12, 120),
        palabra("VACÍO", 140, 158, 12)], (14, 15), pos="right"))
    vasos = [vaso(238 + i * 17.5, 62, i + 1) for i in range(10)]
    S.append(doble(f"{I}d08.jpg", [texto("Con un vaso, voy echando agua en el balde. Uno, dos, tres…", 24, 12, 150),
        texto("¡Diez vasos! Ahora el balde está lleno. Con cinco vasos, estaba por la mitad.", 226, 12, 150), *vasos], (16, 17)))
    S.append(doble(f"{I}d09.jpg", [texto("¿Qué flota y qué se hunde: Rula, el aro o una hoja?", 24, 12, 150),
        texto("Y el balde, ¿está lleno, vacío o por la mitad? ¿Vos qué decís?", 226, 12, 120)], (18, 19)))
    S.append(doble(f"{I}d10.jpg", [texto("Floto boca arriba, pateo con la tabla y llego hasta papá. ¡CHAP, CHAP, CHAP!", 24, 12, 160),
        texto("Hoy aprendí a nadar. ¿Vos sabés cuándo te metiste en el agua por primera vez? Papá trajo algo con dos ruedas… ¿y si mañana aprendo a andar en bici?", 226, 10, 190, 17)], (20, 21), pos="right"))

    S.append(experimento("¿Flota o<br>se hunde?",
        "una palangana con agua, una naranja, una botella de plástico chica vacía con tapa, un corcho, una cuchara de metal, una piedrita y un vaso.",
        ["Antes de probar, adiviná: ¿cuáles van a flotar y cuáles se van a hundir?",
         "Poné cada cosa en el agua, de a una, y mirá qué pasa.",
         "Pelá la naranja con un adulto y volvé a ponerla en el agua. ¿Qué pasó ahora?",
         "Con el vaso, llená la botella hasta la mitad y probala otra vez. ¿Flota más alto o más bajo?",
         "<b>Desafío:</b> ¿cuántos vasos de agua entran en la palangana hasta llenarla?"],
        f"{I}exp.jpg", ["Qué pongo en el agua", "Yo creo que…", "Lo que pasó: ¿flota o se hunde?"],
        ["Naranja con cáscara", "Naranja pelada", "Botella vacía con tapa", "Corcho", "Cuchara de metal", "Piedrita"],
        "En el desafío, anotá cuántos vasos entraron.",
        "Algunas cosas flotan y otras se hunden. Las que tienen mucho aire adentro, como el corcho, la botella vacía o la cáscara de la naranja, suelen flotar. Si le sacamos la cáscara a la naranja, se hunde. Y si le ponemos agua a la botella, flota más bajo."))

    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
    S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')
    return S


PARRAFOS = [
    ("El concepto.", "Que algo flote o se hunda no depende de si es grande o chico, ni solo de si es liviano: depende de cuánto pesa para su tamaño, comparado con el agua. Las cosas que tienen mucho aire adentro (una pelota inflada, un corcho, la cáscara de la naranja) pesan poco para el lugar que ocupan, y el agua las sostiene. Por eso un tronco enorme flota y una moneda chiquita se hunde. Con los pulmones llenos de aire, nuestro cuerpo flota mejor."),
    ("Lleno, vacío y volumen.", "Lleno, vacío y \"por la mitad\" son las primeras ideas de volumen: cuánto lugar hay adentro de algo. Contar cuántos vasos entran en un balde es medir ese lugar."),
    ("El hito.", "Muchos chicos empiezan a flotar con ayuda, patear con una tabla y meter la cara en el agua entre los 4 y los 5 años, más o menos, sobre todo si tienen clases. Nadar solos llega más tarde. Cada chico tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Un adulto siempre dentro del agua y a un brazo de distancia, aunque el chico sepa flotar o use flotadores: los flotadores no reemplazan a un adulto. Nada de correr por el borde. Las piletas de la casa, con cerco y puerta con traba. Y en el experimento, solo una palangana: un chico pequeño puede ahogarse en muy poca agua."),
    ("Para charlar después de leer:", "¿Qué cosas de la bañadera flotan? ¿Cuáles se hunden? ¿Por qué Rula flota, si es tan grande? Si llenás un vaso hasta la mitad, ¿cuántos vasos por la mitad hacen uno lleno?"),
]

if __name__ == "__main__":
    escribir("libro10", "Tomi aprende a nadar", armar("Tomi", "l10-"))
