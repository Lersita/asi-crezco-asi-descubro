# Libro 11 · Tomi aprende a andar en bici · Ilustraciones

Un prompt por página (las dobles llevan una sola imagen panorámica). Nano Banana 2 en 2K (Nano Banana Pro fallaba en formato panorámico en el libro 10), con tres referencias: la hoja de personajes del libro 11 (`referencias/hoja-personajes-libro11.png`), la portada del libro 10 para el estilo (`libro10/p01-v1.png`) y la hoja de la plaza (`referencias/set-plaza.png`). Las dobles salen en 21:9 y se recortan a 2:1. Se generan con `MODELO=nano-banana-2 herramientas/generar_libro.py 11 URL_HOJA URL_ESTILO,URL_PLAZA`.

Reglas de `CLAUDE.md`: la IA no dibuja números, palabras, flechas de recorrido ni tapas de libros (ARRIBA, ADELANTE, ABAJO, ATRÁS, CICLO, EQUILIBRIO, el puntito de la rueda, las flechas y números de las vueltas y las 11 tapas de la colección se agregan en la maqueta); prompts sin numeración; prueba de 2 imágenes antes del lote. Siempre con casco y un adulto cerca, en la plaza sin autos.

La versión mujer queda para más adelante.

Cada prompt se arma así: **[ESTILO] + escena + [REGLAS]**.

**[ESTILO]**: archivo `ilustraciones/herramientas/style-libro11.txt`.

**[REGLAS]**
```
Only mom and dad may appear as adults, each at most once, no other people. An adult close to the boy whenever he is on the bike. Exactly one ball and exactly one bicycle in the picture unless the scene says otherwise. Rula has only a tiny small red cap on top, never a big hat-like cap. Unless the scene says the training wheels are on, the bike has NO training wheels: only its two big wheels. The boy always wears his green helmet on the bike. Keep faces and the ball away from the vertical center line. Calm plain area in the upper part for text.
```

---

## Página 1 · Portada
```
[ESTILO]. Tomi riding his small green bike happily along the round paved path of the park, pedaling, both hands on the handlebars, green helmet on, a huge smile; Rula sitting in the front basket. Dad a few steps behind, jogging gently and smiling. The big tree and the fountain in the soft background. The top 40 percent of the image is calm plain light blue sky for the title. Square 1:1.
```

## Páginas 2–3 · Doble 1
```
[ESTILO]. On the quiet sidewalk in front of the family house, with no cars: the small leaf-green bike with a front basket and the two small training wheels ON, standing on its kickstand, clearly visible in the middle of the left half. Tomi standing next to the bike, and dad crouching in front of him, buckling his green helmet strap under his chin. Rula on the ground next to the bike. Mom is not in this picture. Mom must look exactly like in the second reference image: light skin, dark chestnut-brown curly hair tied up in a bun, round glasses. Dad must look exactly like in the second reference image: light skin, short brown beard, mustard sweater. No other adults: mom at most once and dad at most once. [REGLAS]. Wide 21:9.
```

## Páginas 4–5 · Doble 2 · Con rueditas
```
[ESTILO]. The park. Tomi pedaling slowly along the round paved path on his small green bike, with the two small training wheels ON for this scene, green helmet on, Rula in the front basket, smiling. Mom sitting on the green bench, watching. [REGLAS]. Wide 21:9.
```

## Páginas 6–7 · Doble 3 · La rueda gira
```
[ESTILO]. A close view of the front of the small green bike rolling slowly on the paved path: the front wheel big in the picture, with a curved deep-navy cut-paper motion arrow around it; Tomi, with his green helmet on, looking down at the wheel from above; Rula in the basket. Dad's legs partially visible, walking beside. [REGLAS]. Wide 21:9.
```

## Páginas 8–9 · Doble 4 · Arriba, adelante, abajo, atrás
```
[ESTILO]. A clear, close side view of Tomi riding the small green bike along the paved path, filling most of the left half; his right foot on the pedal and the pedal crank big and clearly visible, low in the picture. No circles, no insets, no magnifying glass, no close-up bubbles: one single continuous scene. Calm plain paving and lawn around the pedal for words. Mom partially visible at the far right, walking. Mom must look exactly like in the second reference image: light skin, dark chestnut-brown curly hair tied up in a bun, round glasses. Dad must look exactly like in the second reference image: light skin, short brown beard, mustard sweater. No other adults: mom at most once and dad at most once. [REGLAS]. Wide 21:9.
```

## Páginas 10–11 · Doble 5 · Sin rueditas
```
[ESTILO]. Tomi sitting on the small green bike with no training wheels, the bike standing still and tipping to one side; Tomi leaning, a little scared, green helmet on; dad right beside him, holding his shoulder and the seat to keep him up. The two small training wheels lying on the path next to them. [REGLAS]. Wide 21:9.
```

## Páginas 12–13 · Doble 6 · Equilibrio
```
[ESTILO]. Tomi pedaling the small green bike with no training wheels along the path, concentrating, green helmet on, Rula in the basket; dad jogging right beside him, one hand holding the back of the seat. Calm plain sky above with space for a big word. [REGLAS]. Wide 21:9.
```

## Páginas 14–15 · Doble 7 · ¡Solo!
```
[ESTILO]. Tomi pedaling on his own along the round path on the small green bike, happy and surprised, green helmet on, Rula in the basket, on the right side of the picture. On the left, dad a few steps behind, both arms up, cheering. [REGLAS]. Wide 21:9.
```

## Páginas 16–17 · Doble 8 · Vueltas a la plaza
```
[ESTILO]. A bird's-eye view straight from above, like a picture map: the round paved path seen as a full ring around the lawn, the big tree crown seen from above in the middle, the small round fountain on one side of the ring and the green bench on the other side, bushes and flowers around. Tomi riding the small green bike all by himself on the ring, seen from above, with his green helmet and Rula in the basket. Nobody else in the picture. Plain paving around the ring with space for arrows. [REGLAS]. Wide 21:9.
```

## Páginas 18–19 · Doble 9 · ¿Vos qué decís?
```
[ESTILO]. Left half: the small green bike standing still on its kickstand on the path, with Rula in the basket and the green helmet hanging from the handlebar. Right half: a wide view of the round path with the fountain and the tree, empty, so a finger can follow the loop. No people in the picture. [REGLAS]. Wide 21:9.
```

## Páginas 20–21 · Doble 10 · Cierre
```
[ESTILO]. Left half: Tomi riding happily along the path on the small green bike, green helmet on, Rula in the basket; behind him, mom and dad sitting together on the green bench, waving. Right half: Tomi, a second time, stopped with one foot on the ground next to his bike, turning toward the viewer and waving goodbye with a big smile, Rula in the basket; nobody else on the right half. The bottom 25 percent of the right half is plain empty paving, with no pictures, no photos, no frames and no objects on it. Exactly two Tomis, one mom and one dad in the whole picture. Mom must look exactly like in the second reference image: light skin, dark chestnut-brown curly hair tied up in a bun, round glasses. Dad must look exactly like in the second reference image: light skin, short brown beard, mustard sweater. No other adults: mom at most once and dad at most once. [REGLAS]. Wide 21:9.
```

## Páginas 22–23 · Experimento
```
Premium children's picture book spot illustrations in exactly the same handmade cut-paper collage style as the reference, on a plain warm cream background, each item separate with plenty of empty space around it, no frames, no text, no letters, no numbers. Top left: a big round jar lid standing on its edge on a wooden floor, with a small colorful sticker on its rim and a strip of masking tape on the floor. Top right: a big lid and a small lid side by side on the floor. Bottom left: a lid rolling on its edge across the floor, with a short curved deep-navy motion line. Bottom right: a smiling 6-year-old child with light chestnut hair in a green shirt, kneeling and gently pushing a lid so it rolls.
```

## Página 24 · Para los grandes
```
[ESTILO]. Small calm vignette in the lower half of the image, plain light blue sky above: Tomi sitting on the green bench in the park next to dad, his green helmet in his lap, the small green bike parked beside them with Rula in the basket. Soft afternoon light. Square 1:1.
```
