#!/usr/bin/env python3
"""Maqueta del libro 3, versión varón y versión mujer (el texto es el mismo; cambian el nombre y las imágenes).
Uso: python3 maqueta/libro3.py -> maqueta/libro3.html y maqueta/libro3-emi.html"""
from comun import B, COLS, e, palabra, numero, texto, doble, portada, experimento, escribir


def armar(nombre, I):
    """nombre: el del protagonista. I: prefijo de las imágenes comprimidas en maqueta/img/."""
    S = [portada(f"{I}p01.jpg", f"{nombre} aprende<br>a gatear", 3)]

    S.append(doble(f"{I}d01.jpg", [texto(f"Soy {nombre}. Ya sé girar y ya sé sentarme.", 24, 12, 150),
        texto("Pero Rula siempre se me escapa. Hoy voy a aprender a gatear.", 226, 12, 150)], (2, 3), pos="80% center"))
    S.append(doble(f"{I}d02.jpg", [texto("Me pongo en cuatro patas. ¿Cuántas cosas me sostienen?", 24, 12, 150),
        texto("Una mano, dos manos. Una rodilla, dos rodillas. ¡Cuatro!", 226, 12, 150)] + NUMS_D02, (4, 5)))
    S.append(doble(f"{I}d03.jpg", [texto("Me hamaco para adelante y para atrás.", 24, 12, 150),
        texto("Adelante, atrás. Adelante, atrás. ¡Pero no avanzo nada!", 226, 12, 150)], (6, 7)))
    S.append(doble(f"{I}d04.jpg", [texto("Empujo fuerte con las manos…", 24, 12, 120),
        texto("¡Y voy para atrás! Rula queda más lejos que antes.", 226, 12, 150)], (8, 9)))
    S.append(doble(f"{I}d05.jpg", [texto("Pruebo en el piso del pasillo. Es liso y brillante.", 24, 12, 150),
        texto("Mis rodillas resbalan, resbalan… ¡FIUUU! Termino con la panza en el piso.", 226, 12, 160)], (10, 11)))
    S.append(doble(f"{I}d06.jpg", [texto("Vuelvo a la alfombra. Tiene muchos pelitos.", 24, 12, 150),
        palabra("FRICCIÓN", 30, 120, 22),
        texto("Acá mis manos y mis rodillas no resbalan. Eso que me ayuda a no resbalar se llama FRICCIÓN.", 226, 12, 170)], (12, 13)))
    S.append(doble(f"{I}d07.jpg", [texto("Mano, rodilla. Mano, rodilla.", 24, 12, 120),
        texto("¡Avanzo! ¡Estoy gateando!", 226, 12, 120)], (14, 15)))
    S.append(doble(f"{I}d08.jpg", [texto("Empujo a Rula en el piso liso. ¡Rueda lejos, lejos!", 24, 12, 160),
        texto("Ahora la empujo en la alfombra. ¡Frena enseguida! La alfombra la frena más que el piso liso.", 226, 12, 175)], (16, 17), ajuste="contain"))
    S.append(doble(f"{I}d09.jpg", [texto("¿Dónde rueda más lejos Rula: en el piso liso o en la alfombra?", 24, 12, 165),
        texto("¿Cuántas manos y cuántas rodillas tengo en el piso? ¡Contalas conmigo!", 226, 12, 165)], (18, 19)))
    S.append(doble(f"{I}d10.jpg", [texto("Una mano, otra mano, una rodilla, otra rodilla. ¡Llegué hasta Rula! ¡La alcancé!", 24, 12, 165),
        texto("Hoy aprendí a gatear. ¿Vos sabés cómo te movías cuando eras bebé? Ahora miro el sillón… ¿qué habrá allá arriba?", 226, 12, 175)], (20, 21)))

    S.append(experimento("¿Dónde llega más lejos<br>la pelota?",
        "una pelota mediana (no chiquita), un libro grande de tapa dura, dos o tres libros más y una toalla.",
        ["Armá una rampa en el piso: apoyá una punta del libro grande arriba de los otros libros.",
         "Poné la pelota arriba de la rampa y soltala, sin empujarla.",
         "Medí con tus manos hasta dónde llegó: una mano, dos manos, tres manos… Anotalo.",
         "Ahora estirá la toalla en el piso, al final de la rampa. Soltá la pelota otra vez, medí y anotá.",
         "<b>Desafío:</b> gateá despacito en el piso liso y en la alfombra. ¿Dónde se te resbalan más las rodillas?"],
        f"{I}exp.jpg", ["Dónde rueda", "Yo creo que llega…", "Lo que pasó"],
        ["Piso liso", "Toalla", "Alfombra (si tenés)"],
        "En «Yo creo que llega…» escribí cerca o lejos. En «Lo que pasó», cuántas manos midió.",
        "En el piso liso, la pelota llega lejos. En la toalla frena antes, porque la toalla la frena más. Esa fricción que frena a la pelota es la misma que no deja que tus manos y tus rodillas resbalen cuando gateás."))

    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
    S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')
    return S


# Números 1 a 4 al lado de cada mano y rodilla en la doble 2 (posiciones en mm sobre la doble de 432 × 216).
NUMS_D02 = [numero(1, 336, 180, COLS[0]), numero(2, 384, 172, COLS[1]),
            numero(3, 246, 172, COLS[3]), numero(4, 274, 180, COLS[4])]

PARRAFOS = [
    ("El concepto.", "La fricción aparece cuando dos superficies se tocan y una se mueve, o intenta moverse, sobre la otra. No solo frena: también es lo que permite agarrarse y empujar. Al gatear, el bebé empuja el piso hacia atrás con las manos y las rodillas, y gracias a la fricción avanza; en un piso muy liso, resbala. Con la pelota pasa algo parecido: cuando rueda sobre la alfombra, la alfombra se hunde un poco y le va quitando energía, por eso frena antes (los físicos lo llaman resistencia a la rodadura)."),
    ("El hito.", "Muchos bebés empiezan a gatear entre los 7 y los 10 meses, más o menos. Antes suelen hamacarse en cuatro patas, y es común que al principio vayan para atrás. Algunos se arrastran, otros se desplazan sentados y algunos casi no gatean y pasan directo a pararse. Cada bebé tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Cuando empieza a moverse, la casa cambia: conviene revisar el piso a su altura. Nada chico a su alcance (si pasa por adentro de un rollo de papel higiénico, es peligroso), tapas en los enchufes, cables fuera de alcance, muebles fijados a la pared y una puerta o reja en las escaleras. En pisos muy lisos, mejor con los pies descalzos o con medias antideslizantes. Y siempre, un adulto cerca."),
    ("Para charlar después de leer:", "¿Qué zapatillas resbalan menos: las de suela lisa o las que tienen dibujitos abajo? ¿Dónde te resbalás más: en el piso mojado o en el piso seco? ¿Cuántas patas usa un perro para caminar? ¿Y vos, cuántas usabas para gatear?"),
]

if __name__ == "__main__":
    escribir("libro3", "Tomi aprende a gatear", armar("Tomi", "l3-"))
    escribir("libro3-emi", "Emi aprende a gatear", armar("Emi", "l3e-"))
