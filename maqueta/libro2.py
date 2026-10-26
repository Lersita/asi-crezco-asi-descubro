#!/usr/bin/env python3
"""Maqueta del libro 2. Uso: python3 maqueta/libro2.py -> maqueta/libro2.html"""
from comun import B, COLS, e, palabra, numero, texto, doble, portada, experimento, escribir

I = "l2-"  # prefijo de las imágenes comprimidas del libro 2 en maqueta/img/
S = [portada(f"{I}p01-portada-v1.jpg", "Tomi aprende<br>a sentarse", 2)]

S.append(doble(f"{I}d01-v1.jpg", [texto("Soy Tomi. Ya sé girar: boca arriba, boca abajo.", 40, 12, 150),
    texto("Pero quiero ver todo desde más arriba. Hoy voy a aprender a sentarme.", 222, 10, 118)], (2, 3)))
S.append(doble(f"{I}d02-v1.jpg", [texto("Desde el piso, todo es alto.", 88, 12, 112),
    palabra("ALTO", 96, 44, 15, "arriba"), palabra("BAJO", 150, 64, 12, "abajo"),
    texto("La planta es alta. Mamá es altísima. Yo soy bajito, bajito.", 222, 8, 108)], (4, 5)))
S.append(doble(f"{I}d03-v1.jpg", [texto("Papá me sienta en la manta.", 110, 14, 92),
    texto("Me voy para un costado… ¡PLAF! Caigo sobre el almohadón.", 226, 12, 118)], (6, 7)))
S.append(doble(f"{I}d04-v1.jpg", [texto("Pruebo otra vez. Abro bien las piernas y apoyo las manos adelante.", 18, 12, 180),
    texto("¡Ahora no me caigo! Parezco una mesita de tres patas.", 224, 10, 120)], (8, 9)))
S.append(doble(f"{I}d05-v1.jpg", [texto("Pongo mi cubo arriba de Rula. ¡Se cae!", 148, 12, 60, 19),
    texto("Arriba de Rula no hay lugar plano. El cubo necesita una base ancha para quedarse quieto.", 222, 12, 84, 19)], (10, 11)))
S.append(doble(f"{I}d06-v1.jpg", [texto("Despacito, levanto una mano. Después, la otra.", 96, 14, 104),
    texto("Me bamboleo un poquito… ¡pero me quedo sentado! ¡Estoy sentado solito!", 222, 12, 160)], (12, 13)))
S.append(doble(f"{I}d07-v1.jpg", [texto("Sentado, veo todo distinto.", 88, 14, 112),
    texto("Rula está cerca. La toco sin estirarme.", 222, 12, 84),
    palabra("CERCA", 228, 62, 13)], (14, 15)))
S.append(doble(f"{I}d08-v1.jpg", [texto("Empujo a Rula y se va rodando lejos, lejos.", 20, 10, 175),
    texto("Ahora Rula está lejos. ¡No la alcanzo!", 222, 10, 150),
    palabra("LEJOS", 244, 46, 15)], (16, 17)))
S.append(doble(f"{I}d09-v1.jpg", [texto("¿Qué está cerca de mí y qué está lejos?", 20, 12, 150),
    texto("¿Qué es alto y qué es bajo? ¿Vos qué decís?", 222, 12, 66, 19)], (18, 19), pos="30% center"))
S.append(doble(f"{I}d10-compuesta.jpg", [texto("Me inclino hacia Rula, un poco más… ¡PLAF! Quedé en cuatro patas.", 18, 14, 182),
    texto("Hoy aprendí a sentarme. ¿Vos sabés cuándo te sentaste solo por primera vez? Ahora quiero llegar hasta Rula… ¿cómo voy a hacer?", 222, 8, 122, 19)], (20, 21)))

S.append(experimento("¿Qué se cae<br>y qué no?",
    "un vaso de plástico, un rollo de papel higiénico vacío, una caja chica, una pelota, una naranja y un libro finito.",
    ["Hacé todo en el piso.", "Poné cada cosa en el piso y soltala. ¿Se queda quieta o se mueve? Anotalo.",
     "Ahora apoyá el libro arriba de cada una. ¿Aguanta o se cae?",
     "Probá el vaso boca arriba y boca abajo. Y el rollo parado y acostado. ¿Qué cambia?",
     "<b>Desafío con tu cuerpo:</b> sentate en el piso con las piernas juntas y los brazos arriba. Después abrí las piernas y apoyá las manos. ¿Cómo te sentís más firme?"],
    f"{I}exp-v1.jpg", ["Objeto", "¿Se queda quieto?", "¿Aguanta el libro?"],
    ["Vaso boca arriba", "Vaso boca abajo", "Rollo parado", "Rollo acostado", "Caja", "Pelota", "Naranja"],
    "En cada casillero escribí o dibujá: sí o no.",
    "Las cosas con una base ancha y plana se quedan quietas y aguantan peso arriba. Las redondas tocan el piso en un puntito: se mueven con poco y lo que ponés arriba se cae. Tomi hizo lo mismo que la caja: con las piernas abiertas y las manos en el piso, su base se hizo más ancha."))

PARRAFOS = [
    ("El concepto.", "Un objeto se mantiene en equilibrio cuando su peso cae dentro de su base de apoyo. Cuanto más ancha es la base y más bajo está el peso, más difícil es que se vuelque. Al sentarse, el bebé abre las piernas y apoya las manos adelante: arma una base ancha, como un trípode. Con la práctica, sus músculos aprenden a corregir el bamboleo y ya no necesita las manos."),
    ("El hito.", "Muchos bebés empiezan a sentarse apoyando las manos entre los 6 y los 8 meses, más o menos, y un poco después lo logran sin ayuda. Cada bebé tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Al principio se cae seguido: conviene practicar en el piso, sobre una manta, con almohadones alrededor y un adulto cerca. Nunca se lo deja sentado solo en un lugar alto, como la cama, la mesa o el sillón."),
    ("Para charlar después de leer:", "¿Qué cosas de tu casa son altas y cuáles son bajas? ¿Por qué las sillas y las mesas tienen cuatro patas? ¿Qué está cerca y qué está lejos de donde estás sentado ahora?"),
]
ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24-v1.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')

escribir("libro2", "Tomi aprende a sentarse", S)
