#!/usr/bin/env python3
"""Maqueta del libro 11 (versión varón; la versión mujer queda para más adelante).
Uso: python3 maqueta/libro11.py -> maqueta/libro11.html
Las palabras grandes (CICLO, EQUILIBRIO), el ciclo del pedal (arriba, adelante, abajo, atrás), el puntito de la rueda,
la vuelta a la plaza y la fila con las 11 tapas de la colección se dibujan acá (la IA no dibuja textos ni tapas)."""
from comun import B, e, texto, doble, portada, experimento, escribir
from comun import palabra as _palabra

AZUL, CORAL = "#23304A", "#C4532E"
TAPAS = ["p01-portada-v2.jpg", "l2-p01-portada-v1.jpg", "l3-p01.jpg", "l4-p01.jpg", "l5-p01.jpg", "l6-p01.jpg",
         "l7-p01.jpg", "l8-p01.jpg", "l9-p01.jpg", "l10-p01.jpg", "l11-p01.jpg"]


def palabra(*a, **k):
    """Palabra grande con un borde blanco suave, para que se lea sobre el pasto y los árboles."""
    return _palabra(*a, **k).replace('style="', 'style="text-shadow:0 0 1.2mm #fff,0 0 2.4mm #fff,0 0 3.5mm rgba(255,255,255,.9);', 1)


def rotulo(t, x, y, size=5.6):
    return (f'<div style="position:absolute;left:{x - 20}mm;top:{y - 3}mm;width:40mm;text-align:center;font-family:Fraunces,serif;'
            f'font-weight:800;font-size:{size}mm;line-height:6mm;color:{AZUL};text-shadow:0 0 1.2mm #fff,0 0 2.4mm #fff,0 0 3.5mm #fff">{e(t)}</div>')


def ciclo_pedal(cx, cy, r, palabras):
    """Círculo con flechas (sentido del pedaleo) y las cuatro posiciones del pie."""
    arco = (f'<svg style="position:absolute;left:{cx - r - 3}mm;top:{cy - r - 3}mm;overflow:visible" width="{2 * r + 6}mm" height="{2 * r + 6}mm" viewBox="0 0 {2 * r + 6} {2 * r + 6}">'
            f'<defs><marker id="pf" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" markerHeight="3" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{CORAL}"/></marker></defs>'
            f'<circle cx="{r + 3}" cy="{r + 3}" r="{r}" fill="rgba(255,253,245,.55)" stroke="{CORAL}" stroke-width="1.1" stroke-dasharray="3 1.6"/>'
            + "".join(f'<path d="M{r + 3 + r * a} {r + 3 + r * b} A{r} {r} 0 0 1 {r + 3 + r * c} {r + 3 + r * d}" fill="none" stroke="{CORAL}" stroke-width="1.1" marker-end="url(#pf)"/>'
                      for a, b, c, d in ((0.7, -0.7, 0.98, -0.2), (0.7, 0.7, 0.2, 0.98), (-0.7, 0.7, -0.98, 0.2), (-0.7, -0.7, -0.2, -0.98)))
            + "</svg>")
    arriba, adelante, abajo, atras = palabras
    return (arco + rotulo(arriba, cx, cy - r - 5) + rotulo(adelante, cx + r + 19, cy) + rotulo(abajo, cx, cy + r + 5)
            + rotulo(atras, cx - r - 15, cy))


def puntito(x, y):
    return (f'<div style="position:absolute;left:{x - 2.6}mm;top:{y - 2.6}mm;width:5.2mm;height:5.2mm;border-radius:50%;'
            f'background:{CORAL};box-shadow:0 0 0 .8mm #fff,.4mm .6mm 1mm rgba(0,0,0,.35)"></div>')


def vuelta(cx, cy, rx, ry):
    """La vuelta a la plaza: una línea punteada sobre el caminito, con flechas."""
    return (f'<svg style="position:absolute;left:0;top:0;overflow:visible" width="432mm" height="216mm" viewBox="0 0 432 216">'
            f'<defs><marker id="pv" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{CORAL}"/></marker></defs>'
            + "".join(f'<path d="M{cx + rx * a} {cy + ry * b} A{rx} {ry} 0 0 1 {cx + rx * c} {cy + ry * d}" fill="none" stroke="{CORAL}" stroke-width="1.4" stroke-dasharray="3.5 2.2" marker-end="url(#pv)" stroke-linecap="round"/>'
                      for a, b, c, d in ((-1, 0, 0, -1), (0, -1, 1, 0), (1, 0, 0, 1), (0, 1, -1, 0)))
            + "</svg>")


def coleccion(x, y, lado, paso):
    """Fila con las 11 tapas de la colección, de bebé girando a nene en bici."""
    return "".join(
        f'<div style="position:absolute;left:{x + i * paso}mm;top:{y}mm;width:{lado}mm;height:{lado}mm;border-radius:1.6mm;'
        f'background:#fff url({B}{t}) center/cover;box-shadow:0 0 0 .7mm #fff,.4mm .8mm 1.4mm rgba(70,45,20,.35)"></div>'
        for i, t in enumerate(TAPAS))


def armar(nombre, I):
    S = [portada(f"{I}p01.jpg", f"{nombre} aprende<br>a andar en bici", 11)]

    S.append(doble(f"{I}d01.jpg", [texto(f"Soy {nombre}. Ya sé girar, sentarme, gatear, pararme, caminar, correr, saltar, subir la escalera, tirar una pelota y nadar.", 24, 8, 180, 16),
        texto("Papá me trajo una bici verde y un casco. Hoy voy a aprender a andar en bici.", 236, 12, 140)], (2, 3)))
    S.append(doble(f"{I}d02.jpg", [texto("En la plaza, pongo a Rula en el canasto. Me siento y apoyo los pies en los pedales.", 24, 12, 150),
        texto("Con las rueditas al costado, pedaleo despacito. ¡No me caigo!", 226, 12, 130)], (4, 5)))
    S.append(doble(f"{I}d03.jpg", [texto("Miro la rueda de adelante. Gira y gira, como Rula cuando rueda.", 24, 12, 150),
        puntito(296, 138),
        texto("Una vuelta, dos vueltas, tres vueltas… Con cada vuelta, la bici avanza.", 226, 12, 92)], (6, 7)))
    S.append(doble(f"{I}d04.jpg", [texto("Mi pie va arriba, adelante, abajo, atrás… y otra vez arriba.", 116, 12, 86),
        ciclo_pedal(300, 160, 21, ("ARRIBA", "ADELANTE", "ABAJO", "ATRÁS")),
        palabra("CICLO", 300, 56, 12),
        texto("Los pedales hacen siempre el mismo camino, una y otra vez. Eso es un CICLO.", 226, 12, 140)], (8, 9)))
    S.append(doble(f"{I}d05.jpg", [texto("Papá saca las rueditas. Me subo y me quedo quieto… ¡uy, me caigo para un costado!", 24, 12, 160),
        texto("Papá me sostiene. Con la bici quieta, es muy difícil mantener el equilibrio.", 226, 12, 140)], (10, 11)))
    S.append(doble(f"{I}d06.jpg", [texto("Ahora papá me empuja del asiento y yo pedaleo. Avanzo, avanzo…", 24, 12, 150),
        palabra("EQUILIBRIO", 30, 60, 13),
        texto("¡Cuando la bici avanza, es más fácil mantener el EQUILIBRIO! Si freno del todo, apoyo un pie en el piso.", 226, 12, 140)], (12, 13)))
    S.append(doble(f"{I}d07.jpg", [texto("Papá me suelta despacito. Yo no me doy cuenta y sigo pedaleando.", 70, 12, 140),
        texto("Miro para atrás… ¡papá está lejos! ¡Voy solo!", 226, 12, 120)], (14, 15)))
    S.append(doble(f"{I}d08.jpg", [texto("Doy una vuelta a la plaza: paso por el árbol, la fuente, el banco… ¡y otra vez el árbol!", 24, 12, 130, 17),
        vuelta(213, 110, 118, 86),
        texto("Siempre vuelvo al principio: es otro ciclo. ¡Ya di tres vueltas!", 340, 12, 80, 17)], (16, 17)))
    S.append(doble(f"{I}d09.jpg", [texto("¿Cuándo es más fácil no caerse: con la bici quieta o andando?", 24, 12, 150),
        texto("Si doy dos vueltas a la plaza, ¿cuántas veces paso por la fuente? ¿Vos qué decís?", 226, 12, 140)], (18, 19)))
    S.append(doble(f"{I}d10.jpg", [texto("Ando en bici por la plaza con mi casco y con Rula en el canasto. ¡Ya casi no me caigo!", 24, 12, 160),
        texto("Hoy aprendí a andar en bici. ¿Vos sabés cuándo anduviste en bici por primera vez? Aprendí un montón de cosas… ¿y vos, qué vas a aprender ahora?", 226, 10, 136, 16),
        coleccion(232, 184, 15, 17.6)], (20, 21)))

    S.append(experimento("¿Cuánto avanza<br>una vuelta?",
        "dos tapas redondas de distinto tamaño (de un frasco grande y de uno chico), un sticker o cinta de colores, un lápiz y cinta de papel.",
        ["Pegá el sticker en el borde de la tapa grande. Apoyala de canto en el piso, con el sticker tocando el piso, y marcá ese lugar con cinta.",
         "Hacé rodar la tapa despacito hasta que el sticker vuelva a tocar el piso: ¡dio una vuelta! Marcá ese lugar.",
         "Antes de seguir, adiviná: con la tapa chica, ¿una vuelta avanza más o menos?",
         "Probalo y medí las dos con tus manos: ¿cuántas manos avanzó cada una?",
         "<b>Desafío:</b> hacé rodar la tapa grande de canto, con un empujoncito. ¿Se mantiene parada mientras rueda? ¿Y cuando frena?"],
        f"{I}exp.jpg", ["Qué pruebo", "Yo creo que…", "Lo que pasó"],
        ["Tapa grande: una vuelta, ¿cuántas manos?", "Tapa chica: una vuelta, ¿cuántas manos?", "La tapa rodando: ¿se cae?", "La tapa quieta de canto: ¿se cae?"],
        "En el desafío, anotá qué pasa cuando la tapa frena.",
        "En cada vuelta, una rueda avanza lo que mide su borde: por eso la tapa grande avanza más en una vuelta que la chica. Y mientras rueda, la tapa se mantiene parada; cuando frena, se cae, igual que la bici."))

    ps = "".join(f"<p><b>{e(t)}</b> {e(c)}</p>" for t, c in PARRAFOS)
    S.append(f'''<section class="spread papel"><img class="vineta" src="{B}{I}p24.jpg"><div class="guarda der"></div><div class="fold"></div>
<div class="grandes"><div class="etiqueta">Para los grandes</div>{ps}</div><div class="folio izq">24</div></section>''')
    return S


PARRAFOS = [
    ("El concepto.", "En cada vuelta, una rueda avanza lo que mide su borde (su circunferencia): por eso una rueda grande llega más lejos por vuelta que una chica. Una bici quieta se cae porque sus dos ruedas apoyan en una línea finita; cuando avanza, el que maneja corrige el manubrio todo el tiempo, casi sin darse cuenta, y la bici \"vuelve a ponerse debajo\" del cuerpo. Por eso es más fácil mantener el equilibrio andando que quieto. No son las ruedas las que sostienen: es el movimiento y esas pequeñas correcciones."),
    ("Vueltas y ciclos.", "Un ciclo es algo que se repite y vuelve al principio: el pedal que va arriba, adelante, abajo y atrás; una vuelta a la plaza; los días de la semana. Contar vueltas es una de las primeras formas de medir."),
    ("El hito.", "Muchos chicos aprenden a andar en bici sin rueditas entre los 5 y los 6 años, más o menos; las bicis sin pedales (de equilibrio) ayudan a que llegue antes. Cada chico tiene su ritmo; ante cualquier duda, lo mejor es consultar al pediatra."),
    ("Seguridad.", "Siempre con casco bien ajustado, aunque sea un ratito. En plazas, parques o veredas sin autos, nunca en la calle, y con un adulto cerca. Zapatillas cerradas, y la bici del tamaño justo: con los pies apoyados en el piso estando sentados."),
    ("Para charlar después de leer:", "¿Qué otras cosas tienen ruedas? ¿Cuántas ruedas tiene cada una? ¿Por qué es más fácil no caerse andando que con la bici quieta? ¿Qué cosas se repiten todos los días, como un ciclo?"),
]

if __name__ == "__main__":
    escribir("libro11", "Tomi aprende a andar en bici", armar("Tomi", "l11-"))
