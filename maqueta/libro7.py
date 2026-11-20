#!/usr/bin/env python3
"""Maqueta del libro 7 (versión varón; la versión mujer queda para más adelante).
Uso: python3 maqueta/libro7.py -> maqueta/libro7.html
Las palabras grandes y los números de los cubos se dibujan acá (la IA no dibuja textos ni números).
En algunas dobles se corre el encuadre (pos) para alejar caras y a Rula del pliegue."""
from comun import B, e, palabra, texto, doble, portada, experimento, escribir


def cubo(n, x, y):
    """Número blanco sobre un cubo, centrado en x, y (mm)."""
    return (f'<div style="position:absolute;left:{x - 6}mm;top:{y - 5.5}mm;width:12mm;height:11mm;text-align:center;'
            f'font-family:Fraunces,serif;font-weight:800;font-size:8mm;line-height:11mm;color:#fff;'
            f'text-shadow:.4mm .5mm 0 rgba(40,30,20,.55)">{n}</div>')


def armar(nombre, I):
    S = [portada(f"{I}p01.jpg", f"{nombre} aprende<br>a saltar", 7)]

    S.append(doble(f"{I}d01.jpg", [texto(f"Soy {nombre}. Ya sé girar, sentarme, gatear, pararme, caminar y correr.", 24, 12, 160),
        texto("Rula rebota bien alto en el pasto. Hoy voy a aprender a saltar.", 296, 12, 124)], (2, 3)))
    S.append(doble(f"{I}d02.jpg", [texto("Doblo las rodillas. Empujo el piso con los pies…", 24, 12, 130),
        texto("¡HOP! Mis pies se despegan del pasto. Y enseguida vuelvo a bajar.", 226, 12, 140)], (4, 5), pos="right"))
    S.append(doble(f"{I}d03.jpg", [texto("Salto otra vez, más fuerte. Subo un poquito más…", 24, 12, 150),
        palabra("GRAVEDAD", 36, 62, 18),
        texto("Pero siempre vuelvo al piso. La GRAVEDAD me tira para abajo, todo el tiempo.", 226, 12, 150)], (6, 7)))
    S.append(doble(f"{I}d04.jpg", [texto("Suelto a Rula desde arriba de mi cabeza. Baja, toca el piso…", 24, 12, 150),
        texto("¡Y rebota para arriba! Cada rebote es un poco más bajito, hasta que Rula se queda quieta.", 226, 12, 150)], (8, 9), pos="12%"))
    S.append(doble(f"{I}d05.jpg", [texto("Rula sube y baja. Yo subo y bajo.", 24, 12, 130),
        palabra("SUBE", 18, 64, 12),
        texto("¿Qué nos hace bajar a los dos? ¡La gravedad!", 226, 12, 130),
        palabra("BAJA", 342, 64, 15)], (10, 11)))
    S.append(doble(f"{I}d06.jpg", [texto("Papá pega tres papelitos de colores en la pared: uno bajo, uno en el medio y uno alto.", 24, 12, 150),
        texto("Salto y toco el papelito bajo. ¡Lo alcanzo!", 226, 12, 130)], (12, 13), pos="37%"))
    S.append(doble(f"{I}d07.jpg", [texto("Salto con todas mis fuerzas… ¡toco el del medio!", 132, 12, 76),
        texto("El papelito alto todavía está muy arriba. ¡Cuando sea más grande voy a llegar!", 226, 12, 150)], (14, 15)))
    torre = [cubo(n, 113, y) for n, y in zip(range(1, 6), (169, 152, 135, 117, 99))]
    rula = [cubo(n, 294.5, y) for n, y in zip(range(1, 4), (183, 162, 141))]
    S.append(doble(f"{I}d08.jpg", [texto("Pongo mis cubos uno arriba del otro, al lado mío. ¡Mido cinco cubos!", 24, 12, 150),
        texto("Rula mide casi tres cubos. ¡Yo mido más que Rula!", 226, 12, 130), *torre, *rula], (16, 17)))
    S.append(doble(f"{I}d09.jpg", [texto("¿Quién rebota más alto: Rula o yo?", 24, 12, 130),
        texto("Y vos, saltando, ¿hasta qué papelito llegarías? ¿Vos qué decís?", 228, 12, 120)], (18, 19), pos="right"))
    S.append(doble(f"{I}d10.jpg", [texto("Salto en el pasto, salto en las baldosas, salto con Rula. ¡Hop, hop, hop!", 24, 12, 160),
        texto("Hoy aprendí a saltar. ¿Vos sabés cuándo saltaste por primera vez? Adentro de casa hay una escalera… ¿y si la subo con papá?", 226, 12, 104, 18)], (20, 21), pos="63%"))

    S.append(experimento("¿Qué rebota<br>más alto?",
        "una tira larga de papel, cinta para pegarla en la pared, un lápiz, una pelota grande, una pelota chica y una media enrollada.",
        ["Pegá la tira de papel en la pared, de arriba abajo. Con un adulto, marcá una rayita cada una de tus manos, apoyadas una arriba de la otra.",
         "Antes de probar, adiviná: ¿cuál va a rebotar más alto?",
         "Soltá cada cosa desde la altura de tu cintura, sin tirarla.",
         "Mirá hasta qué rayita sube después de tocar el piso. Anotalo.",
         "<b>Desafío:</b> parate al lado de la tira y saltá con los dos pies. ¿Hasta qué rayita llegan tus manos?"],
        f"{I}exp.jpg", ["Qué suelto", "Yo creo que…", "Lo que pasó: ¿cuántas manos subió?"],
        ["Pelota grande", "Pelota chica", "Media enrollada", "Yo saltando"],
        "En el desafío, anotá hasta qué rayita llegaron tus manos.",
        "Todo lo que sube vuelve a bajar: la gravedad tira para abajo siempre. Algunas cosas rebotan mucho y otras casi nada. Y ninguna rebota más alto que el lugar desde donde la soltamos."))

    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
    S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')
    return S


PARRAFOS = [
    ("El concepto.", "La gravedad atrae todo hacia la Tierra, siempre, aunque estemos en el aire. Al saltar, las piernas empujan el piso y el cuerpo sube, pero la gravedad lo va frenando hasta que baja otra vez. Una pelota rebota porque se aplasta un poquito al tocar el piso y vuelve a su forma; en cada rebote pierde algo de impulso, por eso sube cada vez menos y nunca más alto que desde donde se la soltó."),
    ("El hito.", "Muchos chicos empiezan a saltar con los dos pies juntos entre los 2 y los 3 años, más o menos: primero saltitos en el lugar, después hacia adelante y, más adelante, desde un escalón bajo. Cada chico tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Mejor que salten en el piso, sobre pasto o una alfombra, y no desde camas, sillones ni lugares altos. Los pediatras recomiendan evitar las camas elásticas en casa a esta edad. Siempre con un adulto cerca y con espacio libre alrededor."),
    ("Para charlar después de leer:", "¿Qué cosas de tu casa rebotan? ¿Cuáles no rebotan nada? ¿Podés saltar y quedarte en el aire? ¿Por qué no? ¿Cuántas manos medís? ¿Y cuántas mide un adulto?"),
]

if __name__ == "__main__":
    escribir("libro7", "Tomi aprende a saltar", armar("Tomi", "l7-"))
