# Libro 9 · Tomi aprende a tirar una pelota · Ilustraciones

Un prompt por página (las dobles llevan una sola imagen panorámica). Nano Banana Pro en 2K, con tres referencias: la hoja de personajes del libro 9 (`referencias/hoja-personajes-libro9.png`), la portada del libro 7 para el estilo y el patio (`libro7/p01-v1.png`) y la doble 1 del libro 7 (`libro7/d01-v1.png`). La hoja del patio no se pasa: aplana el estilo. Las dobles salen en 21:9 y se recortan a 2:1. Se generan con `herramientas/generar_libro.py 9 URL_HOJA URL_ESTILO,URL_PAGINA`.

Reglas de `CLAUDE.md`: la IA no dibuja números, palabras ni figuras de tiza (TRAYECTORIA y el círculo, el cuadrado y el triángulo de tiza se agregan en la maqueta: dejar baldosas lisas); prompts sin numeración; prueba de 2 imágenes antes del lote. Tomi tira solo pelotas blandas, nunca hacia una persona, una ventana o la casa.

La versión mujer queda para más adelante.

Cada prompt se arma así: **[ESTILO] + escena + [REGLAS]**.

**[ESTILO]**: archivo `ilustraciones/herramientas/style-libro9.txt`.

**[REGLAS]**
```
Only mom and dad may appear as adults, each at most once, no other people. An adult partially visible nearby. Exactly one ball in the picture unless the scene says otherwise. Show the house door and the tiled terrace ONLY if the scene mentions them. Keep faces and the ball away from the vertical center line. Calm plain area in the upper part for text.
```

---

## Página 1 · Portada
```
[ESTILO]. Tomi standing on the green lawn, seen from the side, one arm stretched forward and up, his hand just open after throwing; Rula flying high in the air ahead of him along a big curved deep-navy cut-paper motion line that rises from his hand and starts to come down. A huge happy smile. The tree and the fence in the soft background. Exactly one ball. The top 40 percent of the image is calm light blue sky for the title. Square 1:1.
```

## Páginas 2–3 · Doble 1
```
[ESTILO]. Left half: the open glass door of the living room and the small tiled terrace; Tomi stepping out of the door onto the terrace, looking at the lawn with a big smile. Right half: Rula resting on the green lawn, waiting. Dad partially visible at the far right, sitting on the grass near the tree. [REGLAS]. Wide 21:9.
```

## Páginas 4–5 · Doble 2 · El primer intento
```
[ESTILO]. Left half: Tomi standing on the lawn looking down, a little surprised, at Rula, which lies on the grass right next to his feet; his two hands are still open low in front of him, as if he has just dropped it. Right half: dad standing on the lawn, showing the throwing movement with no ball: one arm swung back behind his shoulder, smiling and encouraging. [REGLAS]. Wide 21:9.
```

## Páginas 6–7 · Doble 3 · ¡ZAS!
```
[ESTILO]. Left part: Tomi on the lawn, seen from the side, his throwing arm stretched forward, his hand just open after throwing, his other arm back for balance. From his hand, one smooth curved deep-navy cut-paper motion line rises to the right, reaches a high point and comes down toward the grass. Along this curve, Rula appears three times, as a sequence: going up, at the top of the curve, and coming down near the grass; these three are the same ball in motion, no other balls. Dad partially visible at the far right edge. [REGLAS]. Wide 21:9.
```

## Páginas 8–9 · Doble 4 · Trayectoria
```
[ESTILO]. Tomi on the lawn at the left, arm stretched forward after throwing. Rula, only once, at the very top of a big curve; a dotted deep-navy cut-paper line shows the whole path, from Tomi's hand up to Rula and down to a spot on the grass far to the right. Calm sky above the curve with space for a big word. Mom partially visible at the far left. [REGLAS]. Wide 21:9.
```

## Páginas 10–11 · Doble 5 · Suave y fuerte
```
[ESTILO]. Tomi on the lawn at the left, arm forward after throwing. Two curved deep-navy cut-paper motion lines start from his hand: a short, low one that ends on the grass close to him, and a long, high one that ends far away near the tree. Rula only once, landing at the end of the long curve near the tree. Dad partially visible at the far right. [REGLAS]. Wide 21:9.
```

## Páginas 12–13 · Doble 6 · Figuras de tiza
```
[ESTILO]. The small terrace of big plain terracotta tiles next to the peach wall of the house, with the open glass door at the far left. A wide area of plain, empty tiles in the middle and the right, with nothing drawn on them. Dad crouching at the left holding a piece of white chalk; Tomi standing next to him, holding Rula in both arms, watching. [REGLAS]. Wide 21:9.
```

## Páginas 14–15 · Doble 7 · ¡Adentro!
```
[ESTILO]. The same terrace of big plain terracotta tiles. Tomi standing at the far left on the lawn edge, arm forward after an underhand-to-overhand throw; Rula only once, landing on the empty tiles on the right, with a short curved deep-navy motion line. A wide area of plain empty tiles around where Rula lands, with nothing drawn on them. Mom partially visible at the open glass door. [REGLAS]. Wide 21:9.
```

## Páginas 16–17 · Doble 8 · Figuras por todos lados
```
[ESTILO]. The backyard with the open glass door of the house (a tall rectangle), the terrace of square terracotta tiles, and a garland of small colorful triangular paper flags hanging across the yard from the house to the tree. Tomi standing on the lawn, pointing up at the triangular flags, smiling; Rula on the grass next to him. [REGLAS]. Wide 21:9.
```

## Páginas 18–19 · Doble 9 · ¿Vos qué decís?
```
[ESTILO]. Left half: Tomi on the lawn, his throwing arm swung back behind his shoulder, holding Rula in that hand, ready to throw, concentrating. Right half: on a calm cream paper background, a big simple round cookie and a simple window with four square panes, drawn large like stickers, with empty space around them. [REGLAS]. Wide 21:9.
```

## Páginas 20–21 · Doble 10 · Cierre
```
[ESTILO]. Left half: Tomi on the lawn throwing Rula, happy, with one curved deep-navy motion line; Rula only once, in the air. Right half: the open glass door of the house; mom stepping out onto the terrace carrying a colorful beach bag, a small swimsuit and kids' swim goggles; Tomi, a second time, standing by the terrace looking at the goggles with shining eyes. Exactly two Tomis in the picture. [REGLAS]. Wide 21:9.
```

## Páginas 22–23 · Experimento
```
Premium children's picture book spot illustrations in exactly the same handmade cut-paper collage style as the reference, on a plain warm cream background, each item separate with plenty of empty space around it, no frames, no text, no letters, no numbers. Top left: a rolled-up sock flying through the air in a small curved arc, with a short dotted deep-navy curve. Top right: an open cardboard box on the floor with a rolled-up sock landing inside it. Bottom left: a roll of masking tape and a line of tape on a wooden floor. Bottom right: a smiling 6-year-old child with light chestnut hair in a green shirt, gently tossing a soft ball underhand toward a box.
```

## Página 24 · Para los grandes
```
[ESTILO]. Small calm vignette in the lower half of the image, plain light blue sky above: Tomi and dad sitting on the lawn, rolling Rula back and forth between them, smiling. Soft afternoon light. Square 1:1.
```
