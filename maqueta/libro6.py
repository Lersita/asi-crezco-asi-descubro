#!/usr/bin/env python3
"""Maqueta del libro 6 (versión varón; la versión mujer queda para más adelante).
Uso: python3 maqueta/libro6.py -> maqueta/libro6.html
Los lugares de la carrera (1.°, 2.°, 3.°) y las palabras grandes se dibujan acá (la IA no dibuja textos)."""
from comun import B, COLS, e, palabra, texto, doble, portada, experimento, escribir


def lugar(t, x, y, color):
    """Insignia redonda con un lugar de la carrera, centrada en x, y (mm)."""
    return (f'<div style="position:absolute;left:{x - 8}mm;top:{y - 8}mm;width:16mm;height:16mm;border-radius:50%;background:{color};'
            f'color:#fff;font-family:Fraunces,serif;font-weight:800;font-size:6.6mm;display:flex;align-items:center;justify-content:center;'
            f'box-shadow:.5mm .8mm 0 rgba(70,45,20,.25)">{e(t)}</div>')


def armar(nombre, I):
    S = [portada(f"{I}p01.jpg", f"{nombre} aprende<br>a correr", 6)]

    S.append(doble(f"{I}d01.jpg", [texto(f"Soy {nombre}. Ya sé girar, sentarme, gatear, pararme y caminar.", 24, 12, 160),
        texto("Rula se escapa rodando al patio. Hoy voy a aprender a correr.", 226, 12, 140)], (2, 3)))
    S.append(doble(f"{I}d02.jpg", [texto("Camino despacito: un pie, otro pie.", 24, 12, 130),
        texto("Ahora más rápido, más rápido… ¡estoy corriendo!", 226, 12, 140)], (4, 5)))
    S.append(doble(f"{I}d03.jpg", [texto("Rula baja por la lomita. ¡ZUUUM! Va cada vez más rápido.", 70, 12, 140),
        texto("Del otro lado, la lomita sube. Rula va cada vez más despacio… hasta que se queda quieta.", 226, 12, 150)], (6, 7)))
    S.append(doble(f"{I}d04.jpg", [texto("Caminando, llego al árbol despacio.", 24, 12, 130),
        palabra("DESPACIO", 40, 55, 15),
        texto("Corriendo, ¡llego mucho más rápido!", 226, 12, 130),
        palabra("RÁPIDO", 236, 55, 16)], (8, 9)))
    S.append(doble(f"{I}d05.jpg", [texto("Corro rápido hacia papá. ¡Quiero frenar!", 70, 12, 130),
        texto("Mis pies siguen un poquito más… ¡y llego a sus brazos! Para frenar hace falta un ratito.", 226, 12, 140)], (10, 11)))
    S.append(doble(f"{I}d06.jpg", [texto("Empujo a Rula y sale rodando rápido por el pasto. No frena de golpe.", 24, 12, 150),
        texto("Va más despacio, más despacio… y se queda quieta. El pasto la frena de a poco.", 226, 12, 150),
        palabra("FRENAR", 318, 52, 15)], (12, 13)))
    S.append(doble(f"{I}d07.jpg", [texto("¡Carrera hasta el árbol! Rula, papá y yo.", 24, 12, 130),
        texto("Rula llega en primer lugar. Yo, en segundo. ¡Papá llega en tercer lugar, caminando!", 226, 12, 140),
        lugar("1.°", 366, 128, COLS[0]), lugar("2.°", 250, 84, COLS[4]), lugar("3.°", 150, 68, COLS[5])], (14, 15)))
    S.append(doble(f"{I}d08.jpg", [texto("En el pasto hay tres flores. La primera es roja. La segunda es amarilla.", 24, 12, 150),
        texto("¿Y la tercera? ¡Es violeta, como un gajo de Rula!", 226, 12, 140)], (16, 17)))
    S.append(doble(f"{I}d09.jpg", [texto("¿Cuándo va más rápido Rula: en la bajada o en la subida?", 24, 12, 150),
        texto("Y en la carrera, ¿quién llegó en primer lugar? ¿Vos qué decís?", 226, 12, 140)], (18, 19)))
    S.append(doble(f"{I}d10.jpg", [texto("Corro por todo el patio con Rula. A veces me caigo… ¡pero me levanto y sigo!", 24, 12, 160),
        texto("Hoy aprendí a correr. ¿Vos sabés cuándo corriste por primera vez? Rula rebota bien alto… ¿y si ahora salto?", 226, 12, 104, 18)], (20, 21)))

    S.append(experimento("¿Rápido o<br>despacio?",
        "una bandeja o una tabla, libros, una pelota, un rollo de papel de cocina vacío y una botella de plástico vacía con tapa.",
        ["Apoyá una punta de la bandeja sobre dos libros: es una rampa baja. Soltá la pelota arriba, sin empujarla.",
         "Mirá hasta dónde llega antes de frenar.",
         "Antes de probar, adiviná: si ponés más libros, ¿la pelota va a ir más rápido o más despacio?",
         "Probalo. Después soltala en el piso liso y en una alfombra: ¿dónde frena antes?",
         "<b>Desafío:</b> soltá la pelota, el rollo y la botella juntos. ¿Cuál llega en primer lugar? ¿Cuál en segundo y cuál en tercero?"],
        f"{I}exp.jpg", ["Qué pruebo", "Yo creo que…", "Lo que pasó"],
        ["Rampa baja", "Rampa alta", "Piso liso o alfombra: ¿dónde frena antes?", "Carrera: 1.°, 2.° y 3.°"],
        "En la carrera, anotá cuál llegó en primer, segundo y tercer lugar.",
        "En la rampa más alta, la pelota llega abajo más rápido. Nada frena de golpe: necesita un ratito y lugar para quedarse quieto. En la alfombra frena antes que en el piso liso."))

    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
    S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')
    return S


PARRAFOS = [
    ("El concepto.", "La velocidad dice cuánto camino se hace en un rato: rápido es mucho camino en poco tiempo. En una bajada, la gravedad hace que una pelota vaya cada vez más rápido; en una subida, la va frenando. Para frenar hay que quitarle velocidad al cuerpo, y eso lleva un tiempo y un espacio: los pies y el roce con el piso van frenando de a poco. Por eso un chico que corre no puede pararse de golpe."),
    ("El hito.", "Muchos chicos empiezan a correr entre los 18 y los 24 meses, más o menos: primero es un trote con las piernas abiertas y los brazos para equilibrarse, y se caen sentados seguido. Frenar a tiempo y doblar mientras corren llega un poco después. Cada bebé tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Al correr llegan lejos en segundos: conviene que corran en lugares despejados, sin escalones ni muebles con esquinas, y lejos de la calle, de la pileta y de las escaleras, siempre con un adulto cerca. Mejor con zapatillas cómodas y sin nada en la boca mientras corren."),
    ("Para charlar después de leer:", "¿Qué cosas de tu casa van rápido? ¿Y cuáles van despacio? Cuando corrés, ¿podés frenar de golpe? ¿Qué pasa con tus pies? Si corren tres chicos, ¿cuántos lugares hay? ¿Quién llega en tercer lugar?"),
]

if __name__ == "__main__":
    escribir("libro6", "Tomi aprende a correr", armar("Tomi", "l6-"))
