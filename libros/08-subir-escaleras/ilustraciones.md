# Libro 8 · Tomi aprende a subir la escalera · Ilustraciones

Un prompt por página (las dobles llevan una sola imagen panorámica). Nano Banana Pro en 2K, con tres referencias: la hoja de personajes del libro 8 (`referencias/hoja-personajes-libro8.png`), la portada del libro 7 para el estilo (`libro7/p01-v1.png`; para la portada del libro 8 se usó la doble 4 del libro 8, porque con la del libro 7 salió plana) y la hoja de la escalera (`referencias/set-escalera.png`, con textura de papel, a diferencia de las hojas del living y del patio). Las dobles salen en 21:9 y se recortan a 2:1. Se generan con `herramientas/generar_libro.py 8 URL_HOJA URL_ESTILO,URL_ESCALERA`.

Reglas de `CLAUDE.md`: la IA no dibuja números, palabras ni íconos (ESFUERZO, los números de los escalones y los íconos de mano y pie se agregan en la maqueta); prompts sin numeración; prueba de 2 imágenes antes del lote. En la escalera, Tomi siempre agarrado a la baranda y con un adulto al lado; nunca pasa del descanso.

La versión mujer queda para más adelante.

Cada prompt se arma así: **[ESTILO] + escena + [REGLAS]**.

**[ESTILO]**: archivo `ilustraciones/herramientas/style-libro8.txt`.

**[REGLAS]**
```
Only mom and dad may appear as adults, each at most once, no other people. An adult right next to the boy whenever he is on the stairs. Exactly one ball in the picture unless the scene says otherwise. Exactly six steps up to the landing whenever the stairs are shown. On the stairs and on the landing, every person is always on the inner side of the banister, between the banister and the wall, with the balusters in front of them, between them and the viewer; nobody is ever on the outer side of the banister, on the outer edge of a step or on the front edge of the landing. Keep faces and the ball away from the vertical center line. Calm plain wall in the upper part for text.
```

---

## Página 1 · Portada
```
[ESTILO]. Close view of the indoor wooden stairs from the side. Tomi is big in the picture, filling most of the lower half: he stands on the third step, one hand holding the low diagonal banister, the other arm raised in joy, looking up toward the landing with a huge proud smile showing his teeth; his whole body is visible from head to socks. Dad's hands and arm partially visible at the right edge, close to Tomi's back. Rula resting up on the landing behind the horizontal banister, partly visible. The top 40 percent of the image is calm plain peach wall for the title. Square 1:1.
```

## Páginas 2–3 · Doble 1
```
[ESTILO]. Left half: the living room with the low beige sofa and the knitted rug. Center-right: the foot of the indoor wooden stairs; dad crouching and opening the small white safety gate; Tomi standing next to him on the floor, looking up at the stairs with his mouth open in wonder. Right half, up on the flat landing behind the horizontal banister: mom sitting, holding Rula on her lap, smiling down at Tomi. [REGLAS]. Wide 21:9.
```

## Páginas 4–5 · Doble 2 · ¡BONC, BONC, BONC!
```
[ESTILO]. Rula bouncing down the indoor wooden stairs, shown as a sequence of three balls on three different steps going down from the landing toward the floor, with short curved deep-navy cut-paper motion arcs between them; only these three balls are Rula in motion, no other balls. Mom up on the landing, behind the horizontal banister, with her hands open as if she has just let go. On the floor at the far left, at the foot of the stairs, Tomi standing next to dad, watching with wide eyes, not moving toward the ball. [REGLAS]. Wide 21:9.
```

## Páginas 6–7 · Doble 3 · El primer escalón
```
[ESTILO]. Close view of the bottom of the indoor wooden stairs, seen from the side as in the third reference image. The bottom step is wide and sticks out to the left, in front of the banister post. Tomi stands on the floor right in front of the left end of that bottom step, close to the wall, facing the stairs; he lifts one foot up onto the bottom step, concentrating with the tip of his tongue out, and with one hand he holds the banister post, which is just ahead of him on his right. He is in the walking path of the stairs, never on the outer side of the balusters. Dad crouching on the floor right behind him, with his hands close to Tomi, ready to help. The open white safety gate against the wall nearby. Living room floor on the left. [REGLAS]. Wide 21:9.
```

## Páginas 8–9 · Doble 4 · Mano, pie, pie
```
[ESTILO]. The indoor wooden stairs in side view. Tomi standing on the third step, with two steps below his feet, both feet together on the same step; his feet are at the height of dad's waist. One hand holding the low diagonal banister, smiling proudly. Dad standing on the floor right beside the stairs, one hand close to Tomi's back. The landing is empty and there is no ball in the picture. In the lower part of the image, a wide empty stretch of plain wooden floor in front of the stairs, with nothing on it. [REGLAS]. Wide 21:9.
```

## Páginas 10–11 · Doble 5 · ESFUERZO
```
[ESTILO]. The indoor wooden stairs. Tomi on the fourth step, on the inner side of the banister: the low diagonal banister and its balusters are in front of him, between him and the viewer. Both of his feet are on the steps, one foot lifting up to the next step; he leans forward with a big effort: cheeks puffed, eyebrows up, a tiny drop of sweat on his forehead; one hand holding the top rail of the banister. Dad standing on the floor right beside the stairs, close to Tomi, encouraging him with a smile. Calm plain peach wall on the left half for a big word. [REGLAS]. Wide 21:9.
```

## Páginas 12–13 · Doble 6 · ¡Llegué!
```
[ESTILO]. The indoor wooden stairs with all six steps clearly visible and empty, from the floor up to the flat landing. Up on the landing, safely behind the horizontal banister: the horizontal banister and its balusters are in front of them, between them and the viewer, so their legs are seen through the balusters. Tomi standing there with both arms up in triumph, laughing; mom kneeling next to him, hugging him. Dad standing on the floor at the foot of the stairs, looking up and smiling. [REGLAS]. Wide 21:9.
```

## Páginas 14–15 · Doble 7 · Bajar con cuidado
```
[ESTILO]. The indoor wooden stairs. Tomi coming down carefully, facing forward, on the third step, holding the low banister with both hands, stretching one foot down toward the step below, focused and calm. Dad standing on the floor at the foot of the stairs facing him, arms open and ready. Rula resting on the floor of the living room near the sofa. [REGLAS]. Wide 21:9.
```

## Páginas 16–17 · Doble 8 · Los colores de Rula
```
[ESTILO]. The living room next to the foot of the stairs. Tomi sitting on the knitted rug with Rula on his lap, pointing with one finger at one colored segment of the ball, curious and happy. Rula shows its six vertical segments clearly: red, orange, yellow, leaf green, sky blue, violet. Mom sitting on the low beige sofa in the background, smiling. The stairs in the soft background on the right, empty. [REGLAS]. Wide 21:9.
```

## Páginas 18–19 · Doble 9 · ¿Vos qué decís?
```
[ESTILO]. Left half: Tomi walking calmly across the wooden floor of the living room, relaxed and smiling, next to the knitted rug. Right half: the indoor wooden stairs, with Tomi on the second step holding the low banister, and dad right beside him. In the lower right part, a wide empty stretch of plain wooden floor in front of the stairs, with nothing on it. Exactly two Tomis in the picture. [REGLAS]. Wide 21:9.
```

## Páginas 20–21 · Doble 10 · Cierre
```
[ESTILO]. Left half: the indoor wooden stairs with six plain steps; Tomi climbing happily on the fourth step, holding the low banister, dad right beside him. Right half: the living room with the glass door to the sunny backyard; through the glass, Rula resting on the green lawn outside; a second, smaller Tomi standing inside by the door, looking out at Rula with both arms swung back as if he is about to throw something. Exactly two Tomis in the picture. [REGLAS]. Wide 21:9.
```

## Páginas 22–23 · Experimento
```
Premium children's picture book spot illustrations in exactly the same handmade cut-paper collage style as the reference, on a plain warm cream background, each item separate with plenty of empty space around it, no frames, no text, no letters, no numbers. Top left: a cloth tote bag with handles holding one book, lifted by a child's hand to knee height. Top right: the same tote bag holding three books, lifted by a child's hand to tummy height, the bag bulging. Bottom left: a row of socks on a wooden floor alternating white, green, white, green, white, with an empty space at the end of the row. Bottom right: a smiling 6-year-old child with light chestnut hair in a green shirt, lifting the tote bag with both hands with a little effort.
```

## Página 24 · Para los grandes
```
[ESTILO]. Small calm vignette in the lower half of the image, plain warm peach wall above: Tomi sitting on the knitted rug of the living room with Rula in his arms, resting and smiling; dad sitting on the rug next to him. The foot of the indoor wooden stairs in the soft background. Soft afternoon light. Square 1:1.
```
