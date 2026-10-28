# Libro 5 · Tomi aprende a caminar · Ilustraciones

Un prompt por página (las dobles llevan una sola imagen panorámica). Nano Banana Pro en 2K, con tres referencias: la hoja de personajes del libro 5 (`referencias/hoja-personajes-libro5.png`), una página del libro 4 con el pelo corregido para el estilo (`libro4/d10-pelo2-c.png`) y la hoja del living (`referencias/set-living.png`). Las dobles salen en 21:9 y se recortan a 2:1. Se generan con `herramientas/generar_libro.py 5 URL_HOJA URL_ESTILO,URL_SET`.

Reglas de `CLAUDE.md` para pedir imágenes: la IA no dibuja números, huellitas ni líneas de medida (se agregan en la maqueta: dejar piso libre); prompts sin numeración; prueba de 2 imágenes antes del lote.

La versión mujer queda para más adelante (decidido el 28/10/2026).

Cada prompt se arma así: **[ESTILO] + escena + [REGLAS]**.

**[ESTILO]**: archivo `ilustraciones/herramientas/style-libro5.txt`.

**[REGLAS]**
```
Only mom and dad may appear as adults, each at most once, no other people. An adult partially visible nearby. No small objects near the toddler. Keep faces and the ball away from the vertical center line. Calm plain area in the upper part for text.
```

---

## Página 1 · Portada
```
[ESTILO]. Tomi taking a wobbly first step on the knitted rug toward the viewer, legs a little apart, both arms raised to the sides for balance, a huge proud smile showing his little teeth. Rula on the rug a little ahead of him. Mom's hands partially visible at the far right edge, ready to catch him. The top 40 percent of the image is calm plain cream wall for the title. Square 1:1.
```

## Páginas 2–3 · Doble 1
```
[ESTILO]. Left half: Tomi standing on the knitted rug, holding the front edge of the low beige sofa with one hand, looking toward the right. Right half: mom crouching on the floor a few steps away, arms wide open, smiling and waiting for him. Rula resting on the rug near the sofa. [REGLAS]. Wide 21:9.
```

## Páginas 4–5 · Doble 2 · ¡PLAF!
```
[ESTILO]. A sequence of three Tomis on the knitted rug, all three in the LEFT 40 percent and the RIGHT 40 percent of the image, nothing in the middle: on the far left, letting go of the low beige sofa with arms raised; at about 30 percent of the width, taking a wobbly step forward with arms out for balance; at about 70 percent of the width, sitting down suddenly on his bottom on the soft rug, surprised and laughing. The middle of the image, between 40 and 60 percent of the width, shows only empty rug and wall, no figure and no face. Mom partially visible at the far right, crouching, smiling. [REGLAS]. Wide 21:9.
```

## Páginas 6–7 · Doble 3 · ¡Llegué!
```
[ESTILO]. Left half: Tomi walking across the knitted rug toward the right with both arms raised for balance, determined smile. Right half: mom crouching on the floor with her arms open, about to hug him. A long stretch of empty rug floor between them, clear and plain, with no marks. [REGLAS]. Wide 21:9.
```

## Páginas 8–9 · Doble 4 · Empujar
```
[ESTILO]. Left half: Tomi standing on the knitted rug, one foot forward as if he has just nudged the ball with his foot, delighted face; there is NO ball near his feet. Right half: Rula, the only ball in the image, rolling away across the rug and the wooden floor, with a few short deep-navy cut-paper motion lines behind her. Upper area of the left half: calm wall with empty space for a big word. Dad partially visible at the far right, sitting on the floor. There is exactly one ball in the whole picture. [REGLAS]. Wide 21:9.
```

## Páginas 10–11 · Doble 5 · Tirar
```
[ESTILO]. Left half: Tomi sitting on the wooden floor at the edge of the rug, pulling the corner of a small soft blanket toward himself with both hands, concentrating with the tip of his tongue out. Right half: the small blanket stretched on the floor with Rula sitting on top of it, sliding toward Tomi, with one thick deep-navy cut-paper arrow pointing toward Tomi. Mom partially visible at the far right edge. [REGLAS]. Wide 21:9.
```

## Páginas 12–13 · Doble 6 · Pesa mucho
```
[ESTILO]. Right half: Tomi standing on the rug, leaning forward and pushing with both hands against the low open cardboard toy box, which is full to the top of big soft fabric toys (a plush bear and plain fabric blocks with no letters); his face shows a big effort, cheeks puffed. The box has not moved. Left half: calm room with the low beige sofa. Dad partially visible at the far left, sitting on the floor. [REGLAS]. Wide 21:9.
```

## Páginas 14–15 · Doble 7 · Pesa poquito
```
[ESTILO]. The big soft fabric toys (a plush bear and plain fabric blocks with no letters) scattered on the rug on the left. Tomi walking behind the now empty low cardboard box on the right half, pushing it easily across the wooden floor with both hands, happy face. Dad sitting on the low beige sofa in the background, watching and smiling. [REGLAS]. Wide 21:9.
```

## Páginas 16–17 · Doble 8 · Cerca y lejos
```
[ESTILO]. Tomi standing in the middle of the knitted rug, slightly left of center, arms a little out. On his left, close to him, the low wooden coffee table. Far away on the right side, dad crouching on the floor near the glass patio door, waving. Long empty stretches of plain floor between Tomi and the coffee table and between Tomi and dad, with no marks. [REGLAS]. Wide 21:9.
```

## Páginas 18–19 · Doble 9 · ¿Vos qué decís?
```
[ESTILO]. On the left side of the image, from left to right: the low cardboard toy box full to the top of big soft fabric toys at about 15 percent of the width; Rula on the floor at about 30 percent; Tomi standing right next to Rula at about 40 percent, proud, one hand resting on her, as if he has just arrived walking from the right. The whole right half is a long empty stretch of plain wooden floor and rug with no marks, with mom partially visible at the far right edge, sitting on the floor. [REGLAS]. Wide 21:9.
```

## Páginas 20–21 · Doble 10 · Cierre
```
[ESTILO]. Left half: Tomi walking confidently across the living room with his arms lower and relaxed, Rula rolling beside him on the rug. Right half: the open glass door to a sunny patio with plants; Rula rolling fast toward the door and Tomi behind her, leaning forward, now wearing small white sneakers with green details. Dad partially visible at the far right, standing by the door. [REGLAS]. Wide 21:9.
```

## Páginas 22–23 · Experimento
```
Premium children's picture book spot illustrations in exactly the same handmade cut-paper collage style as the reference, on a plain warm cream background, each item separate with plenty of empty space around it, no frames, no text, no letters, no numbers: an empty shoebox on a wooden floor being pushed by a single child's finger; the same shoebox full of books, with two child's hands pushing it; the same full shoebox sitting on a striped kitchen towel, with a child's hand pulling the corner of the towel; a smiling 6-year-old child with light chestnut hair in a green shirt, kneeling and gently pushing a colorful ball along the floor, with a short deep-navy arrow in front of the ball.
```

## Página 24 · Para los grandes
```
[ESTILO]. Small calm vignette in the lower half of the image, plain warm cream wall above: Tomi walking on the knitted rug toward dad, who is sitting on the floor with open arms, Rula on the rug nearby. Soft afternoon light. Square 1:1.
```
