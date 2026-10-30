#!/usr/bin/env python3
"""Tapa completa para Amazon KDP (contratapa + lomo + frente, con sangrado), tapa blanda 8,5 × 8,5 pulgadas.
Lomo para 24 páginas a color premium: 24 × 0,002347 = 0,0563 pulgadas (sin texto: KDP pide 79 páginas o más).
Uso: python3 maqueta/kdp_tapa.py N es|en → maqueta/kdp-tapa-libroN-es.html
     (después: node maqueta/kdp_pdf.js maqueta/kdp-tapa-libroN-es.html salida.pdf 17.3063in 8.75in)
Necesita antes maqueta/kdp-libroN-<lang>.html (de kdp.py), de donde toma la ilustración de tapa."""
import re, sys, html
from pathlib import Path
from kdp_textos import TITULOS

AQUI = Path(__file__).resolve().parent
SANGRADO, REFILE, PAGINAS = 0.125, 8.5, 24
LOMO = PAGINAS * 0.002347
ANCHO = 2 * SANGRADO + 2 * REFILE + LOMO
ALTO = REFILE + 2 * SANGRADO

COLECCION = {"es": "Así crezco, así descubro", "en": "I Grow, I Discover"}
LIBRO = {"es": "Libro", "en": "Book"}

CONTRATAPA = {
    "es": {
        1: "Tommy es muy chiquito: todavía no se sienta, no gatea y no camina. Pero hoy, con la ayuda de Rula, su pelota grande y de colores, va a aprender algo nuevo: ¡a girar! Y de paso descubre por qué las cosas redondas ruedan y las que tienen lados planos no.",
        2: "Tommy ya sabe girar, pero quiere ver todo desde más arriba. Hoy va a aprender a sentarse… aunque al principio se cae para un lado. Con Rula descubre el secreto del equilibrio: una base ancha no se cae. Y aprende qué es alto, bajo, cerca y lejos.",
        3: "Rula siempre se le escapa. Por eso Tommy va a aprender a gatear: se balancea, va hacia atrás, resbala en el piso liso… hasta que descubre la fricción, lo que no deja que sus manos y rodillas resbalen. Y cuenta: una mano, dos manos, una rodilla, dos rodillas. ¡Cuatro!",
        4: "Rula está encima del sofá y Tommy quiere alcanzarla. Hoy va a aprender a pararse: se agarra, empuja, ¡PUM!, y vuelve a intentar. Así descubre la gravedad, la fuerza que atrae todo hacia el piso, y compara alturas: la mesita, el sofá, su cabeza y la de papá.",
        5: "Mamá espera a Tommy con los brazos abiertos. Hoy va a aprender a caminar: da un paso, dos, tres… ¡PLAF! Y vuelve a intentar. Con Rula descubre la fuerza: empujar y jalar hace que las cosas se muevan, y lo pesado necesita más fuerza. Y cuenta sus pasos: lo que está cerca, lo que está lejos.",
        6: "Rula se escapa rodando al patio, y Tommy va a aprender a correr. Despacio, rápido, más rápido… ¡y frenar no es tan fácil! Con Rula descubre la velocidad: en la bajada va cada vez más rápido y nada frena de golpe. Y en una carrera hasta el árbol aprende quién llega en primer, segundo y tercer lugar.",
        7: "Rula rebota muy alto en el pasto, y Tommy va a aprender a saltar. Dobla las rodillas, empuja el piso y… ¡HOP! Con Rula descubre la gravedad: todo lo que sube vuelve a bajar. Y se mide con cubos y con papelitos en la pared: ¿quién es más alto, Tommy o Rula?",
        8: "Mamá suelta a Rula desde el descanso y baja rebotando: ¡BONC, BONC, BONC! Ahora le toca a Tommy subir la escalera, agarrado del barandal y con papá al lado. Descubre que subir cuesta esfuerzo, porque las piernas levantan todo el cuerpo. Y aprende las secuencias: mano, pie, pie… ¿qué sigue?",
    },
    "en": {
        1: "Tommy is very little: he can't sit up, crawl, or walk yet. But today, with help from Rula, his big colorful ball, he's going to learn something new: how to roll over! Along the way, he discovers why round things roll and things with flat sides don't.",
        2: "Tommy can already roll over, but he wants to see everything from higher up. Today he's going to learn to sit up… even if he tips over at first. With Rula, he discovers the secret of balance: a wide base doesn't fall. And he learns what's tall, short, near, and far.",
        3: "Rula always gets away from him. So Tommy is going to learn to crawl: he rocks, goes backward, slips on the smooth floor… until he discovers friction, the thing that keeps his hands and knees from slipping. And he counts: one hand, two hands, one knee, two knees. Four!",
        4: "Rula is up on the couch, and Tommy wants to reach it. Today he's going to learn to stand up: he grabs on, pushes, BUMP!, and tries again. That's how he discovers gravity, the force that pulls everything toward the floor, and compares heights: the coffee table, the couch, his head, and Dad's.",
        5: "Mom is waiting for Tommy with open arms. Today he's going to learn to walk: one step, two, three… FLOP! And he tries again. With Rula, he discovers force: pushing and pulling make things move, and heavy things need more force. And he counts his steps: what's near, what's far.",
        6: "Rula rolls out into the backyard, and Tommy is going to learn to run. Slow, fast, faster… and stopping isn't so easy! With Rula, he discovers speed: going downhill gets faster and faster, and nothing stops all at once. And in a race to the tree, he learns who comes in first, second, and third.",
        7: "Rula bounces way up high on the grass, and Tommy is going to learn to jump. He bends his knees, pushes the ground, and… HOP! With Rula, he discovers gravity: everything that goes up comes back down. And he measures himself with blocks and paper squares on the wall: who is taller, Tommy or Rula?",
        8: "Mom lets go of Rula from the landing, and it bounces down: BONK, BONK, BONK! Now it's Tommy's turn to climb the stairs, holding the railing with Dad right beside him. He discovers that climbing takes effort, because his legs lift his whole body. And he learns about sequences: hand, foot, foot… what comes next?",
    },
}
SERIE = {
    "es": "Una colección que sigue los primeros logros de un bebé, de girar a andar en bicicleta, y en cada libro enseña un concepto de física y uno de matemática. Para leer en voz alta con niños de 4 a 7 años.",
    "en": "A series that follows a baby's first big milestones, from rolling over to riding a bike, with one physics idea and one math idea in every book. For reading aloud with kids ages 4 to 7.",
}
ADENTRO = {
    "es": ["Una historia para leer en voz alta", "Un experimento con cosas de la casa", "Una página para los grandes"],
    "en": ["A story to read aloud", "A hands-on experiment with things from home", "A page for grown-ups"],
}
ADENTRO_TIT = {"es": "Adentro", "en": "Inside"}


def armar(n, lang):
    interior = (AQUI / f"kdp-libro{n}-{lang}.html").read_text(encoding="utf-8")
    tapa_img = re.search(r'class="page-r art" style="background-image:url\(([^)]+)\)', interior).group(1)
    i = 0 if lang == "es" else 1
    t1, t2 = TITULOS[n][i]
    e = html.escape
    lista = "".join(f"<li>{e(x)}</li>" for x in ADENTRO[lang])
    frente_x = SANGRADO + REFILE + LOMO
    doc = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{e(t1)} {e(t2)} · tapa</title>
<link href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800;9..144,900&display=swap" rel="stylesheet">
<style>
@page{{size:{ANCHO}in {ALTO}in;margin:0}}*{{box-sizing:border-box}}
body{{margin:0;font-family:Andika,sans-serif;color:#23304A}}
.tapa{{position:relative;width:{ANCHO}in;height:{ALTO}in;overflow:hidden;background:#FFF9E7}}
.contra{{position:absolute;left:0;top:0;width:{SANGRADO + REFILE + LOMO / 2}in;height:100%;background:#FFF9E7}}
.frente{{position:absolute;left:{frente_x - LOMO / 2}in;top:0;width:{REFILE + SANGRADO + LOMO / 2}in;height:100%;background-size:cover;background-position:center;background-image:url({tapa_img})}}
.titulo{{position:absolute;left:{frente_x + 0.6}in;top:{SANGRADO + 0.6}in;width:7in}}
.coleccion{{font-family:Fraunces,serif;font-weight:600;font-size:12pt;letter-spacing:.22em;text-transform:uppercase;color:#C4532E}}
h1{{font-family:Fraunces,serif;font-weight:800;font-size:60pt;line-height:1;margin:4mm 0 0;letter-spacing:-.01em}}
.autor{{display:inline-block;font-family:Fraunces,serif;font-weight:700;font-size:13pt;letter-spacing:.12em;color:#C4532E;margin-top:3mm;padding:1.2mm 3.5mm;background:#FFF8E8;border-radius:1.5mm;box-shadow:0 .5mm 1mm rgba(70,45,20,.2)}}
.badge{{position:absolute;left:{frente_x + REFILE - 0.6 - 0.87}in;top:{SANGRADO + 0.6}in;width:.87in;height:.87in;border-radius:50%;background:conic-gradient(#D9452B 0 60deg,#EE8A2A 0 120deg,#E9B21C 0 180deg,#5E9E44 0 240deg,#4FA3D9 0 300deg,#8A5CB8 0 360deg);display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:900;font-size:13mm;color:#fff;text-shadow:0 .5mm 1mm rgba(0,0,0,.35);line-height:.9}}
.badge span{{font-size:3mm;letter-spacing:.15em;text-transform:uppercase}}
.texto{{position:absolute;left:{SANGRADO + 0.7}in;top:{SANGRADO + 0.7}in;width:{REFILE - 1.4}in}}
.texto .coleccion{{margin-bottom:3mm}}
.texto h2{{font-family:Fraunces,serif;font-weight:800;font-size:24pt;line-height:1.05;margin:0 0 5mm}}
.texto p{{font-size:12.5pt;line-height:1.45;margin:0 0 4mm}}
.texto .serie{{font-size:10.5pt;color:#6E5F52}}
.adentro{{margin-top:5mm;background:#FFF3DC;border-radius:3mm;padding:4mm 6mm}}
.adentro b{{font-family:Fraunces,serif;font-size:12pt;color:#C4532E}}
.adentro ul{{margin:2mm 0 0;padding-left:6mm;font-size:11pt;line-height:1.5}}
.rula{{position:absolute;left:{SANGRADO + 0.7}in;bottom:{SANGRADO + 0.55}in;width:1.5in}}
.firma{{position:absolute;left:{SANGRADO + 2.45}in;bottom:{SANGRADO + 0.75}in;font-family:Fraunces,serif;font-weight:700;font-size:12pt;letter-spacing:.12em;color:#C4532E}}
</style></head><body><div class="tapa">
<div class="contra"></div><div class="frente"></div>
<div class="titulo"><div class="coleccion">{e(COLECCION[lang])}</div><h1>{e(t1)}<br>{e(t2)}</h1><div class="autor">by LERSA</div></div>
<div class="badge"><span>{e(LIBRO[lang])}</span>{n}</div>
<div class="texto"><div class="coleccion">{e(COLECCION[lang])} · {e(LIBRO[lang])} {n}</div>
<h2>{e(t1)} {e(t2)}</h2><p>{e(CONTRATAPA[lang][n])}</p><p class="serie">{e(SERIE[lang])}</p>
<div class="adentro"><b>{e(ADENTRO_TIT[lang])}</b><ul>{lista}</ul></div></div>
<img class="rula" src="../web/img/rula.webp" alt=""><div class="firma">by LERSA</div>
</div></body></html>"""
    salida = AQUI / f"kdp-tapa-libro{n}-{lang}.html"
    salida.write_text(doc, encoding="utf-8")
    print("ok", salida.name, f"{ANCHO:.4f} x {ALTO} in")


if __name__ == "__main__":
    armar(int(sys.argv[1]), sys.argv[2])
