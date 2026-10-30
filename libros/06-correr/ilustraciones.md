# Libro 6 · Tomi aprende a correr · Ilustraciones

Un prompt por página (las dobles llevan una sola imagen panorámica). Nano Banana Pro en 2K, con tres referencias: la hoja de personajes del libro 6 (`referencias/hoja-personajes-libro6.png`), una página aprobada del libro 5 para el estilo (`libro5/d03-v1.png`) y la hoja del patio (`referencias/set-patio.png`). Las dobles salen en 21:9 y se recortan a 2:1. Se generan con `herramientas/generar_libro.py 6 URL_HOJA URL_ESTILO,URL_PATIO`.

Reglas de `CLAUDE.md` para pedir imágenes: la IA no dibuja números, palabras ni medidas (los lugares 1.°, 2.° y 3.° y las palabras DESPACIO, RÁPIDO y FRENAR se agregan en la maqueta); prompts sin numeración; prueba de 2 imágenes antes del lote.

La versión mujer queda para más adelante.

Cada prompt se arma así: **[ESTILO] + escena + [REGLAS]**.

**[ESTILO]**: archivo `ilustraciones/herramientas/style-libro6.txt`.

**[REGLAS]**
```
Only mom and dad may appear as adults, each at most once, no other people. An adult partially visible nearby. No small objects near the toddler. Exactly one ball in the picture unless the scene says otherwise. Show the house door and the tiled terrace ONLY if the scene mentions them; otherwise only lawn, fence, bushes, tree and sky. Keep faces and the ball away from the vertical center line. Calm plain area in the upper part for text.
```

---

## Página 1 · Portada
```
[ESTILO]. Tomi running happily across the green lawn toward the viewer, body leaning slightly forward, arms bent and swinging, a huge smile showing his little teeth. Rula rolling on the grass a little ahead of him. The tree and the fence in the soft background. The top 40 percent of the image is calm light blue sky for the title. Square 1:1.
```

## Páginas 2–3 · Doble 1
```
[ESTILO]. Left half: the open glass door of the living room and the terracotta terrace with potted plants; Tomi standing in the doorway in his new small white sneakers with green details, looking out at the yard with excitement; mom partly visible behind him inside the house. Right half: Rula rolling away across the green lawn toward the little hill. [REGLAS]. Wide 21:9.
```

## Páginas 4–5 · Doble 2 · ¡Estoy corriendo!
```
[ESTILO]. Three Tomis on the green lawn, left to right, at about 15, 35 and 75 percent of the width, nothing in the middle: walking calmly, walking faster with arms out, and running with both feet almost in the air and arms swinging, delighted. Dad partially visible at the far right, sitting on the grass. [REGLAS]. Wide 21:9.
```

## Páginas 6–7 · Doble 3 · La colina
```
[ESTILO]. Side view of the gentle grassy little hill: it is big and fills the lower middle of the image, wide and rounded, with its top in the center and a long smooth slope going down to the left and another going down to the right. No house, no door, no terrace in this picture. On the LEFT slope, at about 25 percent of the width, Rula rolling DOWN the slope toward the bottom left, with a few short deep-navy cut-paper speed lines on its upper right side, behind it. On the RIGHT slope, at about 75 percent of the width, near the top, the same ball drawn a second time, rolling UP slowly, with no speed lines. Nothing between 42 and 58 percent of the width except the grassy top of the hill. Tomi, fully visible from head to sneakers, standing on the flat grass at about 10 percent of the width at the bottom left, watching with wide eyes and an open mouth. Mom partially visible at the far left edge. Exactly two images of the ball, the same ball at two moments. [REGLAS]. Wide 21:9.
```

## Páginas 8–9 · Doble 4 · Despacio y rápido
```
[ESTILO]. The tree on the right side. Left half: Tomi walking calmly on the grass toward the tree, relaxed. Right half: Tomi running fast toward the same tree, leaning forward, with a few short deep-navy cut-paper speed lines behind him. Calm sky above each half with empty space for a big word. Dad partially visible near the tree at the far right. [REGLAS]. Wide 21:9.
```

## Páginas 10–11 · Doble 5 · ¡A frenar!
```
[ESTILO]. Left half: Tomi running fast across the grass toward the right, leaning forward, arms open, his feet still moving, a short deep-navy cut-paper motion line under his feet showing he is sliding a little. Right half: dad (short beard, mustard sweater) crouching on the grass with arms wide open, ready to catch him, smiling. [REGLAS]. Wide 21:9.
```

## Páginas 12–13 · Doble 6 · Frenar
```
[ESTILO]. Tomi on the left, standing on the grass with his hands just opened after pushing. Rula rolling across the lawn from left to right shown in three positions, each one closer to the previous one, the last one stopped on the grass, showing that it slows down little by little; short deep-navy speed lines only behind the first position. Calm sky above the middle with empty space for a big word. Mom partially visible at the far right, sitting on the grass. [REGLAS]. Wide 21:9.
```

## Páginas 14–15 · Doble 7 · ¡Carrera!
```
[ESTILO]. The tree on the right. A race toward the tree, left to right: dad walking calmly at the back on the left, smiling; Tomi running in the middle-left, leaning forward, happy; Rula rolling ahead and just touching the trunk of the tree on the right. Everyone well separated, with grass between them. [REGLAS]. Wide 21:9.
```

## Páginas 16–17 · Doble 8 · Tres flores
```
[ESTILO]. Left side: Tomi crouching on the grass, looking closely and pointing with one finger. In front of him, three single flowers in a row on the lawn, well separated from each other and from the middle of the image: first a red one, then a yellow one, then a violet one, the violet one on the right half. Rula resting on the grass at the far left behind Tomi. Mom partially visible at the far right. [REGLAS]. Wide 21:9.
```

## Páginas 18–19 · Doble 9 · ¿Tú qué dices?
```
[ESTILO]. Left half: the little grassy hill with Rula resting at the very top, ready to roll down. Right half: the tree, and Tomi sitting on the grass under it, resting and smiling, a little out of breath. Dad partially visible next to the tree. [REGLAS]. Wide 21:9.
```

## Páginas 20–21 · Doble 10 · Cierre
```
[ESTILO]. Left half: Tomi running happily across the lawn with Rula rolling beside him, a small grass stain on one knee of his gray joggers. Right half: Rula bouncing high in the air above the grass, with a curved deep-navy cut-paper motion arc, and Tomi below it looking up with his knees bent as if about to jump. Mom partially visible at the far right. The ball appears twice, once on each half. [REGLAS]. Wide 21:9.
```

## Páginas 22–23 · Experimento
```
Premium children's picture book spot illustrations in exactly the same handmade cut-paper collage style as the reference, on a plain warm cream background, each item separate with plenty of empty space around it, no frames, no text, no letters, no numbers: a tray resting on two books as a low ramp with a ball rolling down it; the same tray resting on a taller pile of books as a steep ramp with the ball rolling down faster, with short deep-navy speed lines; a ball rolling on a smooth wooden floor next to a ball stopped on a soft rug; a smiling 6-year-old child with light chestnut hair in a green shirt, kneeling at the top of a ramp and letting go of a ball, an empty cardboard paper towel tube and an empty plastic bottle at the same time.
```

## Página 24 · Para los grandes
```
[ESTILO]. Small calm vignette in the lower half of the image, light blue sky above: Tomi sitting on the grass under the tree, leaning on mom, who sits next to him, both smiling and resting after running; Rula on the grass beside them. Soft afternoon light. Square 1:1.
```
