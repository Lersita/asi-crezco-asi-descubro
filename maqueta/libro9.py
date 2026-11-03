#!/usr/bin/env python3
"""Maqueta del libro 9 (versión varón; la versión mujer queda para más adelante).
Uso: python3 maqueta/libro9.py -> maqueta/libro9.html
La palabra TRAYECTORIA y las figuras de tiza (círculo, cuadrado y triángulo) se dibujan acá
(la IA no dibuja textos ni figuras). En la doble 3 se corre el encuadre para alejar a Rula del pliegue."""
from comun import B, e, palabra, texto, doble, portada, experimento, escribir

TIZA = "rgba(255,253,245,.92)"


def tiza(forma, x, y, w, h, giro=0):
    """Figura de tiza en perspectiva sobre las baldosas: caja de w × h mm con centro en x, y."""
    trazo = f'fill="none" stroke="{TIZA}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="7 1.2"'
    if forma == "circulo":
        dib = f'<ellipse cx="50" cy="50" rx="46" ry="44" {trazo}/>'
    elif forma == "cuadrado":
        dib = f'<rect x="6" y="6" width="88" height="88" {trazo}/>'
    else:
        dib = f'<path d="M50 5 L95 93 L5 93 Z" {trazo}/>'
    return (f'<svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position:absolute;left:{x - w / 2}mm;top:{y - h / 2}mm;'
            f'width:{w}mm;height:{h}mm;transform:rotate({giro}deg);filter:drop-shadow(0 0 .4mm rgba(255,255,255,.6))">{dib}</svg>')


def armar(nombre, I):
    S = [portada(f"{I}p01.jpg", f"{nombre} aprende<br>a tirar una pelota", 9)]

    S.append(doble(f"{I}d01.jpg", [texto(f"Soy {nombre}. Ya sé girar, sentarme, gatear, pararme, caminar, correr, saltar y subir la escalera.", 24, 12, 170),
        texto("Rula me espera en el patio. Hoy voy a aprender a tirarla bien lejos.", 226, 12, 140)], (2, 3)))
    S.append(doble(f"{I}d02.jpg", [texto("Agarro a Rula con las dos manos y la suelto… ¡PUM! Cae al lado de mis pies.", 24, 12, 160),
        texto("Así no vuela. Papá me muestra cómo: el brazo va para atrás y después para adelante.", 226, 12, 140)], (4, 5)))
    S.append(doble(f"{I}d03.jpg", [texto("Llevo el brazo para atrás, apunto… ¡y ZAS! La suelto.", 24, 12, 150),
        texto("Rula sube, sube… y después baja. ¡Hace una curva en el aire!", 312, 12, 108)], (6, 7), pos="left"))
    S.append(doble(f"{I}d04.jpg", [texto("Desde que sale de mi mano, Rula dibuja una curva.", 24, 12, 150),
        palabra("TRAYECTORIA", 118, 146, 12),
        texto("Ese camino por el aire se llama TRAYECTORIA. La gravedad tira a Rula para abajo todo el tiempo, por eso la curva baja.", 318, 10, 104, 17)], (8, 9)))
    S.append(doble(f"{I}d05.jpg", [texto("Si la tiro suave, la curva es cortita y Rula cae cerca.", 24, 12, 150),
        texto("Si la tiro fuerte, la curva es larga y Rula llega lejos. ¡Casi hasta el árbol!", 226, 12, 140)], (10, 11)))
    figuras = [tiza("circulo", 40, 192, 24, 13, -8), tiza("cuadrado", 78, 194, 22, 12, -8), tiza("triangulo", 118, 196, 24, 13, -8)]
    S.append(doble(f"{I}d06.jpg", [texto("Papá dibuja formas con tiza en las baldosas.", 24, 12, 140), *figuras,
        texto("Un CÍRCULO, bien redondo. Un CUADRADO, con cuatro lados iguales. Un TRIÁNGULO, con tres puntas.", 226, 12, 150)], (12, 13)))
    figuras7 = [tiza("triangulo", 175, 196, 30, 16, -4), tiza("circulo", 255, 180, 52, 20, -3), tiza("cuadrado", 312, 199, 28, 14, -3)]
    S.append(doble(f"{I}d07.jpg", [texto("Apunto al círculo y tiro… ¡Rula cae adentro!", 24, 12, 140), *figuras7,
        texto("Ahora, al triángulo. ¡Uy, se pasó! Cayó en el cuadrado.", 226, 12, 140)], (14, 15)))
    S.append(doble(f"{I}d08.jpg", [texto("En el patio hay formas por todos lados. La puerta es un rectángulo y cada baldosa es un cuadrado.", 24, 12, 170),
        texto("Los banderines son triángulos. ¿Y Rula? De frente, se ve como un círculo.", 226, 12, 140)], (16, 17)))
    S.append(doble(f"{I}d09.jpg", [texto("Si tiro a Rula más fuerte, ¿la curva es más larga o más corta?", 24, 12, 150),
        texto("¿Qué forma tiene una galletita? ¿Y una ventana? ¿Vos qué decís?", 226, 12, 150)], (18, 19)))
    S.append(doble(f"{I}d10.jpg", [texto("Tiro a Rula una y otra vez: curvas cortitas, curvas largas. ¡ZAS, ZAS, ZAS!", 24, 12, 160),
        texto("Hoy aprendí a tirar una pelota. ¿Vos sabés cuándo tiraste una pelota por primera vez? Hace calor… ¿y si este verano aprendo a nadar?", 226, 10, 190, 17)], (20, 21)))

    S.append(experimento("¿Qué curva<br>hace?",
        "una media enrollada o una pelota blanda, una caja o una canasta, y cinta de papel o tiza.",
        ["Con cinta, marcá en el piso una línea para pararte. Poné la caja a tres pasos.",
         "Tirá la media despacito y mirá el camino que hace en el aire.",
         "Antes de seguir, adiviná: si tirás más fuerte, ¿cae más cerca o más lejos?",
         "Tirá suave, medio y fuerte. Contá a cuántos pasos cayó cada vez.",
         "<b>Desafío:</b> con cinta, armá en el piso un círculo, un cuadrado y un triángulo. ¿En cuál embocás?"],
        f"{I}exp.jpg", ["Cómo tiro", "Yo creo que…", "Lo que pasó: ¿a cuántos pasos cayó?"],
        ["Suave", "Medio", "Fuerte", "Al círculo, al cuadrado y al triángulo"],
        "En el desafío, anotá en qué forma embocaste.",
        "Todo lo que tiramos hace una curva: sube y baja, porque la gravedad lo tira para abajo desde que sale de la mano. Cuanto más fuerte tiramos, más larga es la curva y más lejos llega."))

    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
    S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')
    return S


PARRAFOS = [
    ("El concepto.", "Cuando algo se tira, sale con una velocidad hacia adelante y hacia arriba. Desde ese momento, la gravedad lo va frenando cuando sube y lo acelera cuando baja: por eso su camino es una curva (los físicos la llaman parábola), y no una línea recta que después cae. Con más fuerza, la curva es más larga. Rula es grande y liviana, y el aire la frena bastante: una pelota chica y pesada, tirada igual, llegaría más lejos."),
    ("Las formas.", "Reconocer círculos, cuadrados, triángulos y rectángulos en las cosas de todos los días es una de las primeras ideas de la geometría. Una pelota es una esfera: de frente se ve como un círculo."),
    ("El hito.", "Muchos chicos tiran una pelota con una mano, por encima del hombro y apuntando, entre los 3 y los 4 años, más o menos. Primero la sueltan o la empujan con las dos manos; la puntería llega con la práctica. Cada chico tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Mejor con pelotas blandas, al aire libre o en un lugar despejado, lejos de ventanas, vidrios y de la calle, y nunca apuntando a la cara de otra persona. Siempre con un adulto cerca."),
    ("Para charlar después de leer:", "¿Qué cosas se pueden tirar? ¿Cuáles no se tiran nunca? ¿Qué forma tienen la mesa, un plato y la puerta de tu casa? Si tirás un bollo de papel, ¿qué camino hace en el aire?"),
]

if __name__ == "__main__":
    escribir("libro9", "Tomi aprende a tirar una pelota", armar("Tomi", "l9-"))
