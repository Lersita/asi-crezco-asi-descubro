#!/usr/bin/env python3
"""Maqueta del libro 4, versión varón y versión mujer (el texto es el mismo; cambian el nombre y las imágenes).
Uso: python3 maqueta/libro4.py -> maqueta/libro4.html y maqueta/libro4-emi.html"""
from comun import B, COLS, e, palabra, texto, doble, portada, experimento, escribir


def armar(nombre, I):
    """nombre: el del protagonista. I: prefijo de las imágenes comprimidas en maqueta/img/."""
    S = [portada(f"{I}p01.jpg", f"{nombre} aprende<br>a pararse", 4)]

    S.append(doble(f"{I}d01.jpg", [texto(f"Soy {nombre}. Ya sé girar, sentarme y gatear.", 24, 12, 150),
        texto("Pero Rula está arriba del sillón. Hoy voy a aprender a pararme.", 226, 12, 150)], (2, 3)))
    S.append(doble(f"{I}d02.jpg", [texto("Desde el piso, el sillón es más alto que yo.", 24, 12, 150),
        texto("Mi cabeza no llega hasta arriba. ¿Cómo hago para ver a Rula?", 338, 150, 82, 19)], (4, 5)))
    S.append(doble(f"{I}d03.jpg", [texto("Me agarro fuerte del sillón. Empujo con las piernas.", 24, 12, 150),
        texto("Arriba, arriba, arriba… ¡Estoy de pie!", 226, 12, 130)], (6, 7)))
    S.append(doble(f"{I}d04.jpg", [texto("Pero mis piernas se cansan…", 70, 12, 120),
        texto("¡PUM! Me siento de cola en el piso. Algo me tiró para abajo.", 226, 12, 150)], (8, 9)))
    S.append(doble(f"{I}d05.jpg", [texto("Me paro otra vez y agarro a Rula. La suelto…", 40, 12, 150),
        palabra("ABAJO", 70, 100, 22, "abajo"),
        texto("¡Rula cae al piso! Todo lo que suelto cae para abajo.", 226, 12, 140)], (10, 11)))
    S.append(doble(f"{I}d06.jpg", [texto("Suelto mi media: ¡cae! Suelto mi cubo de tela: ¡cae!", 40, 12, 150),
        palabra("GRAVEDAD", 40, 110, 22),
        texto("Eso que tira las cosas hacia el piso se llama GRAVEDAD.", 226, 12, 120)], (12, 13)))
    S.append(doble(f"{I}d07.jpg", [texto("De pie, mi cabeza llega más arriba que la mesita.", 24, 12, 130),
        texto("Todavía no llega a la mesa. ¡Y la cabeza de papá llega altísimo!", 226, 12, 110)], (14, 15)))
    S.append(doble(f"{I}d08.jpg", [texto("Me agarro del sillón y doy pasitos de costado.", 24, 12, 150),
        texto("Un pasito, otro pasito. ¡Llego a la otra punta del sillón!", 226, 12, 150)], (16, 17)))
    S.append(doble(f"{I}d09.jpg", [texto("¿Qué llega más arriba: el sillón, la mesita o mi cabeza?", 24, 12, 165),
        texto("Y si suelto a Rula, ¿para dónde va? ¿Vos qué decís?", 226, 12, 130)], (18, 19)))
    S.append(doble(f"{I}d10.jpg", [texto("Me suelto del sillón… ¡y me quedo de pie sin agarrarme! Mi cabeza llega más arriba que nunca.", 24, 12, 170),
        texto("Hoy aprendí a pararme. ¿Vos sabés cuándo te paraste por primera vez? Mamá me espera con los brazos abiertos… ¿y si doy un paso?", 226, 12, 150, 19)], (20, 21)))

    S.append(experimento("¿Todo cae<br>igual?",
        "una pelota, una media enrollada, un cubo o juguete blando y dos hojas de papel iguales.",
        ["Parate y estirá el brazo. Soltá cada cosa desde la misma altura. ¿Para dónde cae? Anotalo.",
         "Tomá las dos hojas. Arrugá una hasta hacer una pelotita y dejá la otra lisa.",
         "Antes de probar, adiviná: si las soltás juntas, ¿cuál llega primero al piso?",
         "Soltalas juntas desde la misma altura y mirá bien.",
         "<b>Desafío con tu cuerpo:</b> soltá la pelota desde tu rodilla, desde tu cintura y desde arriba de tu cabeza. ¿Desde dónde tarda más en llegar al piso?"],
        f"{I}exp.jpg", ["Qué suelto", "¿Para dónde cae?", "Lo que pasó"],
        ["Pelota", "Media", "Cubo blando", "Hoja lisa y hoja arrugada"],
        "Con las hojas, anotá cuál llegó primero. En el desafío, desde dónde tardó más.",
        "Todo lo que soltamos cae hacia el piso: la gravedad lo tira para abajo. La hoja lisa cae más despacio que la arrugada, aunque pesan lo mismo: es el aire el que la frena. Y desde más arriba, la pelota tarda más en llegar."))

    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
    S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')
    return S


PARRAFOS = [
    ("El concepto.", "La gravedad es la fuerza con la que la Tierra atrae todo hacia ella. Por eso lo que soltamos cae y por eso nosotros quedamos sobre el piso. Si no hubiera aire, todas las cosas caerían igual de rápido, pesen lo que pesen; en casa, el aire frena más a lo liviano y ancho, como una hoja abierta o una pelota grande y blanda. Pararse es aprender a sostener el cuerpo contra esa fuerza: cuando las piernas se cansan, la gravedad gana y el bebé se sienta de golpe."),
    ("El hito.", "Muchos bebés empiezan a pararse agarrados a un mueble entre los 9 y los 12 meses, más o menos. Primero se paran y no saben bajar; después dan pasitos de costado agarrados al mueble y, un poco más adelante, se quedan unos segundos de pie sin apoyo. Cada bebé tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Al pararse llega a lugares nuevos: conviene fijar a la pared los muebles que podrían volcarse, sacar manteles que pueda tironear y alejar de los bordes lo pesado o lo caliente. Las caídas sentado son normales; mejor que practique descalzo, sobre una alfombra y con un adulto cerca."),
    ("Para charlar después de leer:", "¿Qué cosas de tu casa llegan más arriba que tu cabeza? ¿Y cuáles más abajo? Si soltás una pluma y una pelota, ¿cuál llega primero? ¿Por qué? ¿Se te ocurre algo que, al soltarlo, no caiga enseguida al piso? (Pista: un globo con gas, un barrilete.)"),
]

if __name__ == "__main__":
    escribir("libro4", "Tomi aprende a pararse", armar("Tomi", "l4-"))
    escribir("libro4-emi", "Emi aprende a pararse", armar("Emi", "l4e-"))
