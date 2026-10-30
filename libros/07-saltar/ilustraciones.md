# Libro 7 · Tomi aprende a saltar · Ilustraciones

Un prompt por página (las dobles llevan una sola imagen panorámica). Nano Banana Pro en 2K, con tres referencias: la hoja de personajes del libro 7 (`referencias/hoja-personajes-libro7.png`), la portada del libro 6 para el estilo y el patio (`libro6/p01-v1.png`) y la doble 1 del libro 6 (`libro6/d01-v1.png`). La hoja del patio no se pasa: aplana el estilo. Las dobles salen en 21:9 y se recortan a 2:1. Se generan con `herramientas/generar_libro.py 7 URL_HOJA URL_ESTILO,URL_PAGINA`.

Reglas de `CLAUDE.md`: la IA no dibuja números, palabras ni líneas de medida (GRAVEDAD, SUBE, BAJA, las líneas punteadas de altura y los números de los cubos se agregan en la maqueta); prompts sin numeración; prueba de 2 imágenes antes del lote. Tomi salta siempre en el piso, nunca desde muebles ni lugares altos.

La versión mujer queda para más adelante.

Cada prompt se arma así: **[ESTILO] + escena + [REGLAS]**.

**[ESTILO]**: archivo `ilustraciones/herramientas/style-libro7.txt`.

**[REGLAS]**
```
Only mom and dad may appear as adults, each at most once, no other people. An adult partially visible nearby. No small objects near the boy. Exactly one ball in the picture unless the scene says otherwise. Show the house door and the tiled terrace ONLY if the scene mentions them. Keep faces and the ball away from the vertical center line. Calm plain area in the upper part for text.
```

---

## Página 1 · Portada
```
[ESTILO]. Tomi jumping happily on the green lawn, both feet together in the air, knees slightly bent, both arms up, a huge smile showing his teeth. Rula bouncing in the air next to him at the same height, with a small curved deep-navy cut-paper motion line under it. The tree and the fence in the soft background. The top 40 percent of the image is calm light blue sky for the title. Square 1:1.
```

## Páginas 2–3 · Doble 1
```
[ESTILO]. Left half: Tomi standing on the green lawn, looking up with his mouth open in wonder. Right half: Rula high up in the air at the top of a big bounce, with a curved deep-navy cut-paper motion arc going up from the grass to the ball. Dad partially visible at the far right, standing near the tree. [REGLAS]. Wide 21:9.
```

## Páginas 4–5 · Doble 2 · ¡HOP!
```
[ESTILO]. Three Tomis on the lawn, at about 15, 35 and 75 percent of the width, nothing in the middle: crouching with knees bent and arms back, ready to jump; in the air with both feet together and arms up; landing again on the grass with knees bent, smiling. Mom partially visible at the far right, sitting on the grass. [REGLAS]. Wide 21:9.
```

## Páginas 6–7 · Doble 3 · Gravedad
```
[ESTILO]. Right half: Tomi high in the air at the top of a big jump, both feet together, arms up, determined. Next to him, one thick deep-navy cut-paper arrow pointing up and another pointing down. Left half: calm sky and lawn with empty space for a big word. Dad partially visible at the far right edge. [REGLAS]. Wide 21:9.
```

## Páginas 8–9 · Doble 4 · Rula rebota
```
[ESTILO]. Tomi on the left, at about 12 percent of the width, standing with both arms up, having just let go of the ball above his head. Rula shown four times bouncing toward the right across the lawn, each bounce arc lower than the last, connected by thin curved deep-navy cut-paper motion arcs: high at about 30 percent, lower at about 62 percent, lower still at about 78 percent, and finally resting still on the grass at about 90 percent. Nothing between 44 and 56 percent of the width except the motion arc. Mom partially visible at the far left edge. [REGLAS]. Wide 21:9.
```

## Páginas 10–11 · Doble 5 · Sube y baja
```
[ESTILO]. Tomi on the left half and Rula on the right half, both up in the air at the same height, Tomi jumping with both feet together and arms up, Rula bouncing. A thick deep-navy cut-paper arrow pointing up beside Tomi and one pointing down beside Rula. Calm sky above each of them with empty space for big words. Dad partially visible at the far right. [REGLAS]. Wide 21:9.
```

## Páginas 12–13 · Doble 6 · Tres papelitos
```
[ESTILO]. The terracotta tiled terrace next to the peach outside wall of the house, the open glass door at the far left. On the plain wall, three plain colored paper squares taped at three clearly different heights: a red one low, at the height of Tomi's raised hand when he jumps a little; a yellow one in the middle, a bit higher; a blue one high up, at the height of dad's head. The squares are plain, with nothing written or drawn on them. Tomi on the tiles, jumping with both feet and touching the red square with one hand, happy. Dad standing next to the wall, smiling, having just taped the squares. All the squares and faces away from the middle of the image. [REGLAS]. Wide 21:9.
```

## Páginas 14–15 · Doble 7 · Más alto
```
[ESTILO]. The same peach outside wall of the house with the same three plain colored paper squares at three heights: red low, yellow in the middle, blue high. Tomi in the air at the top of his best jump, both feet together, stretching one arm and touching the yellow square; the blue square is clearly far above his hand. Mom partially visible at the far left, sitting on the terrace. Empty plain wall around each square for dotted lines that will be added later. [REGLAS]. Wide 21:9.
```

## Páginas 16–17 · Doble 8 · ¿Cuánto mido?
```
[ESTILO]. On the terracotta tiled terrace in front of the peach wall of the house. At about 18 percent of the width: Tomi standing straight in side view, and right next to him a neat tower of EXACTLY EIGHT big soft fabric cubes stacked one on top of the other, the top of the tower exactly level with the top of Tomi's head, not higher. At about 75 percent of the width: Rula standing on the tiles next to a tower of EXACTLY THREE of the same cubes, the top of that tower level with the top of Rula. The cubes are plain solid colors with nothing written or drawn on them, all the same size. Nothing between 40 and 60 percent of the width except tiles and wall. Dad partially visible at the far right, crouching. [REGLAS]. Wide 21:9.
```

## Páginas 18–19 · Doble 9 · ¿Tú qué dices?
```
[ESTILO]. Left half: on the lawn, Tomi and Rula both in the air, jumping and bouncing side by side, Rula a little higher. Right half: the peach outside wall of the house with the three plain colored paper squares at three heights, red low, yellow in the middle, blue high, with nobody in front of it. Mom partially visible at the far left edge. [REGLAS]. Wide 21:9.
```

## Páginas 20–21 · Doble 10 · Cierre
```
[ESTILO]. Left half: Tomi hopping happily across the lawn, shown in three small jumps in a row, with Rula bouncing beside him. Right half: through the open glass door of the house, inside, the bottom of an indoor staircase with a wooden handrail; dad standing at the foot of the stairs, holding out his hand to Tomi, who looks at the stairs with curiosity from the doorway. [REGLAS]. Wide 21:9.
```

## Páginas 22–23 · Experimento
```
Premium children's picture book spot illustrations in exactly the same handmade cut-paper collage style as the reference, on a plain warm cream background, each item separate with plenty of empty space around it, no frames, no text, no letters, no numbers. Top left: a long strip of paper taped to a wall from top to bottom, with short plain lines drawn across it at regular steps and nothing written. Top right: a big ball, a small ball and a rolled-up sock falling side by side from the same height, with a short deep-navy arrow pointing down under each. Bottom left: the big ball bouncing back up high, the small ball bouncing a little, and the sock flat on the floor, not bouncing. Bottom right: a smiling 6-year-old child with light chestnut hair in a green shirt jumping with both feet on the floor next to the paper strip on the wall, one hand reaching up toward it.
```

## Página 24 · Para los grandes
```
[ESTILO]. Small calm vignette in the lower half of the image, light blue sky above: Tomi and dad jumping together on the lawn, holding hands, both smiling, Rula bouncing next to them. Soft afternoon light. Square 1:1.
```
