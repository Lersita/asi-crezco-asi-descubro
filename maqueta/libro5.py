#!/usr/bin/env python3
"""Maqueta del libro 5 (versión varón; la versión mujer queda para más adelante).
Uso: python3 maqueta/libro5.py -> maqueta/libro5.html
Las huellitas y sus números se dibujan acá (la IA no dibuja números ni huellas)."""
from comun import B, e, palabra, texto, doble, portada, experimento, escribir

AZUL, CORAL = "#23304A", "#C4532E"


def huella(x, y, giro, n=None, color=AZUL, izq=False):
    """Huellita de pie (vista desde arriba) centrada en x, y (mm), girada `giro` grados (0 = hacia arriba)."""
    espejo = "scale(-1,1)" if izq else ""
    dedos = "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
                    for cx, cy, r in ((7.2, 4.2, 2.3), (11.4, 4.9, 1.8), (14.4, 6.6, 1.5), (16.4, 9.0, 1.3), (17.6, 11.8, 1.1)))
    num = (f'<div style="position:absolute;left:{x - 5}mm;top:{y - 4}mm;width:10mm;text-align:center;font-family:Fraunces,serif;'
           f'font-weight:800;font-size:5.6mm;line-height:8mm;color:#fff">{n}</div>' if n is not None else "")
    svg = (f'<svg viewBox="0 0 22 36" width="11mm" height="18mm" style="overflow:visible">'
           f'<g transform="translate(11 18) {espejo} translate(-11 -18)">{dedos}'
           f'<path d="M5 13 C5 9 9 8.5 13 9 C18 9.6 19 13 18.6 18 C18.2 23 17 25 16.8 29 C16.6 33 14 35 11 35 C7.5 35 5.6 32.5 5.8 28.5 C6 24 5 19 5 13 Z" fill="{color}"/></g>'
           '</svg>')
    return (f'<div style="position:absolute;left:{x - 5.5}mm;top:{y - 9}mm;width:11mm;height:18mm;'
            f'transform:rotate({giro}deg);filter:drop-shadow(.4mm .6mm 0 rgba(70,45,20,.25))">{svg}</div>{num}')


def camino(xs, y, giro, numerar=True, color=AZUL, salto=7, desde=1):
    """Una fila de huellitas que alternan pie izquierdo y derecho."""
    return "".join(huella(x, y + (salto if i % 2 else 0), giro, (desde + i) if numerar else None, color, izq=(i % 2 == 0))
                   for i, x in enumerate(xs))


def armar(nombre, I):
    S = [portada(f"{I}p01.jpg", f"{nombre} aprende<br>a caminar", 5)]

    S.append(doble(f"{I}d01.jpg", [texto(f"Soy {nombre}. Ya sé girar, sentarme, gatear y pararme.", 24, 12, 150),
        texto("Mamá me espera con los brazos abiertos. Hoy voy a aprender a caminar.", 226, 12, 140)], (2, 3)))
    S.append(doble(f"{I}d02.jpg", [texto("Me suelto del sillón. Levanto un pie…", 24, 12, 130),
        texto("Un paso, dos pasos, tres pasos… ¡PLAF! Me siento de cola en la alfombra.", 226, 12, 150)], (4, 5)))
    S.append(doble(f"{I}d03.jpg", [texto("Me paro otra vez. Abro los brazos para no caerme.", 24, 12, 150),
        texto("Uno, dos, tres, cuatro, cinco… ¡Llego a los brazos de mamá! Mamá estaba a cinco pasos.", 226, 12, 140),
        camino([165, 210, 255, 300, 345], 199, 90)], (6, 7)))
    S.append(doble(f"{I}d04.jpg", [texto("Ahora quiero jugar con Rula. Le doy un empujoncito con el pie.", 24, 12, 150),
        palabra("EMPUJAR", 228, 52, 16),
        texto("¡Rula se va rodando lejos! Cuando empujo, hago FUERZA.", 226, 12, 150)], (8, 9)))
    S.append(doble(f"{I}d05.jpg", [texto("Rula está arriba de su mantita. Tiro de la punta…", 24, 12, 150),
        palabra("TIRAR", 250, 50, 20),
        texto("¡Rula viene hacia mí! Tirar también es hacer fuerza.", 226, 12, 150)], (10, 11)))
    S.append(doble(f"{I}d06.jpg", [texto("Empujo la caja de los juguetes. ¡No se mueve! Está llena y pesa mucho.", 24, 12, 150),
        texto("Empujo más fuerte… ¡se mueve un poquito! Lo pesado necesita más fuerza.", 226, 12, 150)], (12, 13)))
    S.append(doble(f"{I}d07.jpg", [texto("Saco los juguetes de la caja. Ahora pesa poquito.", 24, 12, 150),
        texto("La empujo y camino detrás de ella. ¡Diez pasos sin caerme!", 226, 12, 140)], (14, 15)))
    S.append(doble(f"{I}d08.jpg", [texto("Hasta la mesita: cuatro pasos. Está cerca.", 24, 12, 140),
        texto("Hasta papá: ¡ocho pasos! Papá está más lejos.", 226, 12, 130),
        camino([122, 96, 70, 44], 201, -90, color=CORAL),
        camino([192, 217, 242, 267, 292, 317, 342, 367], 199, 90)], (16, 17)))
    S.append(doble(f"{I}d09.jpg", [texto("¿Qué necesita más fuerza: empujar a Rula o la caja llena?", 24, 12, 160),
        texto("Contá mis huellitas hasta Rula. ¿Cuántos pasos di?", 226, 12, 140),
        camino([350, 315, 280, 245, 210, 178], 180, -90, numerar=False, salto=9)], (18, 19)))
    S.append(doble(f"{I}d10.jpg", [texto("Camino por todo el living con Rula. Ya no puedo contar mis pasos: ¡son muchísimos!", 24, 12, 160),
        texto("Hoy aprendí a caminar. ¿Vos sabés cuándo diste tu primer paso? ¿Y si ahora voy más rápido que Rula?", 226, 12, 150, 19)], (20, 21)))

    S.append(experimento("¿Cuánta fuerza<br>hace falta?",
        "una caja de zapatos, libros o juguetes para llenarla, un repasador y una pelota.",
        ["Poné la caja vacía en el piso. Empujala con un solo dedo.",
         "Llenala con libros. Antes de probar, adiviná: ¿se va a mover con un dedo?",
         "Probá con un dedo, después con una mano y después con las dos.",
         "Poné la caja llena arriba del repasador. Tirá de la punta: ¿viene hacia vos?",
         "<b>Desafío:</b> empujá la pelota suave y después fuerte. ¿Hasta cuántos pasos llega cada vez?"],
        f"{I}exp.jpg", ["Qué muevo y cómo", "Yo creo que…", "Lo que pasó"],
        ["Caja vacía, con un dedo", "Caja llena, con un dedo", "Caja llena, con las dos manos",
         "Caja llena, tirando del repasador", "Pelota suave y fuerte: ¿cuántos pasos?"],
        "En el desafío, anotá hasta cuántos pasos llegó la pelota cada vez.",
        "Empujar y tirar son fuerzas: hacen que las cosas se muevan. Lo pesado necesita más fuerza: a veces un dedo no alcanza. Y cuanto más fuerte empujamos la pelota, más lejos llega."))

    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
    S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')
    return S


PARRAFOS = [
    ("El concepto.", "Una fuerza es un empujón o un tirón. Mover algo pesado cuesta más porque hay que hacer más fuerza para ponerlo en marcha, y porque se apoya más contra el piso, que lo frena: es la fricción del libro 3. Caminar también es una cuestión de fuerzas: en cada paso el pie empuja el piso hacia atrás, y el piso empuja el cuerpo hacia adelante."),
    ("El hito.", "Muchos bebés dan sus primeros pasos sin agarrarse entre los 12 y los 15 meses, más o menos; algunos antes y otros un poco después. Al principio caminan con las piernas abiertas y los brazos en alto, y se caen sentados seguido: es parte de aprender. Cada bebé tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Al caminar llega más lejos y más rápido: conviene poner rejas en las escaleras, proteger las esquinas de los muebles y fijar a la pared lo que pueda volcarse. En casa, descalzo o con medias antideslizantes; afuera, con zapatillas flexibles. Los pediatras recomiendan no usar andadores con ruedas: los juguetes para empujar, firmes y estables, son una mejor opción."),
    ("Para charlar después de leer:", "¿Cuántos pasos hay de tu cama a la puerta de tu cuarto? ¿Y hasta la cocina? ¿Qué cosas de tu casa podés mover empujando? ¿Cuáles no se mueven aunque empujes fuerte? Cuando caminás, ¿quién empuja a quién: tu pie al piso o el piso a vos? (Los dos.)"),
]

if __name__ == "__main__":
    escribir("libro5", "Tomi aprende a caminar", armar("Tomi", "l5-"))
