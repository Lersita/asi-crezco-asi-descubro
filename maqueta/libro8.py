#!/usr/bin/env python3
"""Maqueta del libro 8 (versión varón; la versión mujer queda para más adelante).
Uso: python3 maqueta/libro8.py -> maqueta/libro8.html
La palabra ESFUERZO y los íconos de la secuencia "mano, pie, pie" se dibujan acá (la IA no dibuja textos ni íconos).
En algunas dobles se corre el encuadre (pos) para alejar caras y a Rula del pliegue."""
from comun import B, e, palabra, texto, doble, portada, experimento, escribir
from libro5 import huella

AZUL, CORAL = "#23304A", "#C4532E"


def mano(x, y, color=CORAL):
    """Manito abierta (palma con cuatro dedos y pulgar), centrada en x, y (mm)."""
    svg = (f'<svg viewBox="0 0 30 34" width="14mm" height="16mm" style="overflow:visible">'
           f'<rect x="6" y="14" width="18" height="17" rx="7" fill="{color}"/>'
           + "".join(f'<rect x="{dx}" y="{dy}" width="4.4" height="14" rx="2.2" fill="{color}"/>' for dx, dy in ((6.5, 3), (11, 0.5), (15.5, 1.5), (20, 5)))
           + f'<rect x="0" y="15" width="4.4" height="12" rx="2.2" transform="rotate(-35 2 21)" fill="{color}"/></svg>')
    return (f'<div style="position:absolute;left:{x - 7}mm;top:{y - 8}mm;width:14mm;height:16mm;'
            f'filter:drop-shadow(.4mm .6mm 0 rgba(70,45,20,.25))">{svg}</div>')


def pregunta(x, y):
    """Círculo punteado con un signo de pregunta: el lugar del que sigue."""
    return (f'<div style="position:absolute;left:{x - 8}mm;top:{y - 8}mm;width:16mm;height:16mm;border-radius:50%;'
            f'border:.7mm dashed {AZUL};color:{AZUL};font-family:Fraunces,serif;font-weight:800;font-size:9mm;'
            f'display:flex;align-items:center;justify-content:center;background:rgba(255,250,240,.6)">?</div>')


def secuencia(x0, y, n, paso=22, final=False):
    """Fila mano, pie, pie, mano, pie, pie… empezando en x0 (mm)."""
    out = []
    for i in range(n):
        x = x0 + i * paso
        out.append(mano(x, y) if i % 3 == 0 else huella(x, y, 0, izq=(i % 3 == 1)))
    if final:
        out.append(pregunta(x0 + n * paso, y))
    return "".join(out)


def armar(nombre, I):
    S = [portada(f"{I}p01.jpg", f"{nombre} aprende<br>a subir la escalera", 8)]

    S.append(doble(f"{I}d01.jpg", [texto(f"Soy {nombre}. Ya sé girar, sentarme, gatear, pararme, caminar, correr y saltar.", 24, 12, 160),
        texto("Papá abre la rejita de la escalera. Hoy voy a aprender a subirla.", 226, 12, 140)], (2, 3), pos="right"))
    S.append(doble(f"{I}d02.jpg", [texto("Mamá suelta a Rula arriba, en el descanso. ¡BONC, BONC, BONC!", 24, 12, 150),
        texto("Rula baja rebotando, escalón por escalón. La gravedad la tira para abajo… ¿y para subir?", 278, 12, 140)], (4, 5), pos="right"))
    S.append(doble(f"{I}d03.jpg", [texto("Ahora subo yo. Me agarro de la baranda y levanto un pie… ¡qué alto es el escalón!", 24, 12, 160),
        texto("Empujo con la pierna y subo todo mi cuerpo. ¡Uno!", 226, 12, 130)], (6, 7), pos="left"))
    S.append(doble(f"{I}d04.jpg", [texto("Mano en la baranda, un pie, el otro pie. ¡Dos!", 24, 12, 130),
        secuencia(34, 62, 6),
        texto("Mano, pie, pie. ¡Tres! Siempre lo mismo, en el mismo orden: es una secuencia.", 226, 12, 150)], (8, 9)))
    S.append(doble(f"{I}d05.jpg", [texto("¡Uf! Para subir, mis piernas levantan todo mi cuerpo.", 24, 12, 140),
        palabra("ESFUERZO", 30, 62, 16),
        texto("Eso cuesta ESFUERZO. Caminar por el piso es más fácil que subir.", 226, 12, 130)], (10, 11), pos="left"))
    S.append(doble(f"{I}d06.jpg", [texto("¡Cuatro! ¡Cinco! Mis piernas están cansadas.", 24, 12, 130),
        texto("Cuanto más alto subo, más esfuerzo hago. ¡Seis! ¡Llegué al descanso!", 226, 12, 100)], (12, 13)))
    S.append(doble(f"{I}d07.jpg", [texto("Para bajar, me agarro fuerte de la baranda. Bajo despacito, escalón por escalón.", 24, 12, 160),
        texto("Seis, cinco, cuatro, tres, dos, uno… ¡abajo! Bajar también se hace con cuidado.", 226, 12, 150)], (14, 15), pos="left"))
    S.append(doble(f"{I}d08.jpg", [texto("Los gajos de Rula van siempre en el mismo orden: rojo, naranja, amarillo, verde, celeste y violeta.", 24, 12, 170),
        texto("Y después del violeta, ¿qué viene? ¡El rojo otra vez! Es una secuencia que se repite.", 226, 12, 150)], (16, 17)))
    S.append(doble(f"{I}d09.jpg", [texto("¿Qué cuesta más esfuerzo: caminar por el piso o subir la escalera?", 24, 12, 160),
        texto("Mano, pie, pie, mano… ¿qué sigue? ¿Vos qué decís?", 226, 12, 130),
        secuencia(40, 64, 4, final=True)], (18, 19)))
    S.append(doble(f"{I}d10.jpg", [texto("Subo otra vez con papá: ¡uno, dos, tres, cuatro, cinco, seis! Ya no me canso tanto.", 24, 12, 160),
        texto("Hoy aprendí a subir la escalera. ¿Vos sabés cuándo subiste una escalera por primera vez? Rula me espera en el patio… ¿y si ahora la tiro bien lejos?", 226, 12, 150, 18)], (20, 21)))

    S.append(experimento("¿Qué cuesta<br>más?",
        "una bolsa de tela con manijas, tres libros y medias de dos colores.",
        ["Poné un libro en la bolsa. Levantala desde el piso hasta tu rodilla y después hasta tu panza.",
         "Antes de seguir, adiviná: con tres libros, ¿va a costar más o menos?",
         "Poné los tres libros y levantala otra vez hasta las dos alturas.",
         "Anotá cuánto costó cada vez: poquito, más o mucho.",
         "<b>Desafío:</b> con un adulto, armá una fila de medias en el piso: blanca, de color, blanca, de color… ¿Cuál sigue?"],
        f"{I}exp.jpg", ["Qué levanto", "Yo creo que…", "Lo que pasó: ¿poquito, más o mucho?"],
        ["Un libro hasta la rodilla", "Un libro hasta la panza", "Tres libros hasta la rodilla", "Tres libros hasta la panza"],
        "En el desafío, seguí la fila de medias hasta que se terminen.",
        "Levantar algo más alto cuesta más esfuerzo, y levantar algo más pesado, también. Por eso subir la escalera cansa: en cada escalón levantamos todo nuestro cuerpo. Y una secuencia siempre se repite en el mismo orden."))

    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
    S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')
    return S


PARRAFOS = [
    ("El concepto.", "Para subir hay que levantar el propio cuerpo contra la gravedad, que siempre tira para abajo: cuanto más alto se sube, y cuanto más pesa lo que se levanta, más esfuerzo hace falta (los físicos lo llaman trabajo). Al bajar, la gravedad ayuda, pero los músculos frenan el cuerpo en cada escalón para que no caiga de golpe: por eso bajar también pide fuerza y cuidado."),
    ("Las secuencias.", "Una secuencia es algo que sigue un orden: contar los escalones del 1 al 6 y al revés, \"mano, pie, pie\", los colores de Rula. Reconocer un patrón y adivinar qué sigue es una de las primeras bases de la matemática."),
    ("El hito.", "Muchos chicos suben la escalera agarrados a la baranda o de la mano entre los 2 y los 3 años, más o menos: primero apoyan los dos pies en cada escalón y, más adelante, alternan un pie en cada uno. Bajar suele llegar después que subir. Cada chico tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Conviene poner rejas arriba y abajo de la escalera hasta que suban y bajen con seguridad, y no dejar juguetes en los escalones. Siempre con un adulto al lado, con buena luz, descalzos o con medias antideslizantes."),
    ("Para charlar después de leer:", "¿Cuántos escalones hay en tu casa o en la escuela? ¿Los contamos? ¿Qué te cansa más: caminar o subir? ¿Por qué? Inventá una secuencia con aplausos y saltitos: aplauso, aplauso, saltito… ¿qué sigue?"),
]

if __name__ == "__main__":
    escribir("libro8", "Tomi aprende a subir la escalera", armar("Tomi", "l8-"))
