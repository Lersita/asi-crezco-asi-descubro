# Libro 10 · Tomi aprende a nadar · Ilustraciones

Un prompt por página (las dobles llevan una sola imagen panorámica). Nano Banana Pro en 2K, con tres referencias: la hoja de personajes del libro 10 (`referencias/hoja-personajes-libro10.png`, solo las dos figuras de 5 años), la portada del libro 9 para el estilo (`libro9/p01-v1.png`) y la hoja de la pileta (`referencias/set-pileta.png`). Las dobles salen en 21:9 y se recortan a 2:1. Se generan con `herramientas/generar_libro.py 10 URL_HOJA URL_ESTILO,URL_PILETA`.

Reglas de `CLAUDE.md`: la IA no dibuja números, palabras ni vasitos para contar (FLOTA, SE HUNDE, LLENO, VACÍO y los diez vasos se agregan en la maqueta); prompts sin numeración; prueba de 2 imágenes antes del lote. Siempre un adulto dentro del agua, al lado de Tomi, en la parte baja.

La versión mujer queda para más adelante.

Cada prompt se arma así: **[ESTILO] + escena + [REGLAS]**.

**[ESTILO]**: archivo `ilustraciones/herramientas/style-libro10.txt`.

**[REGLAS]**
```
Only mom and dad may appear as adults, each at most once, no other people. An adult in the water right next to the boy whenever he is in the water. Exactly one ball in the picture unless the scene says otherwise. Keep faces and the ball away from the vertical center line. Calm plain area in the upper part for text.
```

---

## Página 1 · Portada
```
[ESTILO]. Tomi in the turquoise water of the shallow end, lying on his tummy holding a blue swim kickboard in front of him with both hands, his face out of the water with a huge happy smile, blue goggles on his forehead, kicking his legs with small white splashes behind him. Rula floating on the water next to him. Dad in the water right beside him, smiling, one hand close to the kickboard. The top 40 percent of the image is calm plain light blue sky for the title. Square 1:1.
```

## Páginas 2–3 · Doble 1
```
[ESTILO]. Left half: Tomi standing on the beige stone edge of the pool, wearing a leaf-green t-shirt with wide white stripes over his green swim shorts, blue goggles on his forehead, holding Rula in his arms, looking at the water with excitement. Mom next to him on the edge, holding a colorful beach bag. Right half: the calm turquoise pool; dad standing in the shallow water, waving. [REGLAS]. Wide 21:9.
```

## Páginas 4–5 · Doble 2 · ¡Qué fría!
```
[ESTILO]. The shallow end of the pool with the white metal ladder. Tomi going down the ladder slowly, holding both handrails, his feet just touching the water, making a funny face because the water is cold, shoulders up. Dad standing in the water right next to the ladder, arms open, smiling. Rula on the stone edge. [REGLAS]. Wide 21:9.
```

## Páginas 6–7 · Doble 3 · Flota
```
[ESTILO]. Rula floating on the calm turquoise water on the right, with soft rings of water around it. Tomi standing in the shallow water on the left, the water up to his waist, looking at Rula with surprise. Dad in the water right next to Tomi. Calm sky above with space for a big word. [REGLAS]. Wide 21:9.
```

## Páginas 8–9 · Doble 4 · Se hunde
```
[ESTILO]. A split view of the shallow end, half above and half under the water, with a wavy water line across the middle of the height. Above the water: Tomi bending forward with his face in the water and blue goggles on, dad standing right beside him with one hand on his back, Rula floating on the surface. Under the water: Tomi's goggled face looking down, and on the pale blue tiles of the bottom, one colorful plastic diving ring. [REGLAS]. Wide 21:9.
```

## Páginas 10–11 · Doble 5 · Floto como Rula
```
[ESTILO]. Tomi floating on his back on the turquoise water, relaxed, arms spread wide, eyes looking up at the sky, a calm smile. Dad standing in the water beside him with both hands gently under Tomi's back. Rula floating next to Tomi. The striped umbrella and the sky above. [REGLAS]. Wide 21:9.
```

## Páginas 12–13 · Doble 6 · ¡Chap, chap!
```
[ESTILO]. Tomi on his tummy in the water holding a blue swim kickboard with both hands, face out of the water, kicking his legs straight with white splashes behind him, moving to the right. Mom standing in the shallow water a few steps ahead on the right, arms open. Dad in the water just behind Tomi on the left. [REGLAS]. Wide 21:9.
```

## Páginas 14–15 · Doble 7 · Lleno y vacío
```
[ESTILO]. Tomi sitting on the beige stone edge of the shallow end with his feet in the water, turning over a small colorful plastic bucket so that the water pours out with a big splash. Mom standing in the water right in front of him, laughing. Calm sky above with space for big words. [REGLAS]. Wide 21:9.
```

## Páginas 16–17 · Doble 8 · ¿Cuántos vasos?
```
[ESTILO]. Tomi sitting on the beige stone edge of the shallow end with his feet in the water, carefully pouring water from a small plastic cup into a colorful bucket; the bucket is about half full. Dad in the water right next to him. A wide plain area of stone edge to the right of the bucket, with nothing on it. [REGLAS]. Wide 21:9.
```

## Páginas 18–19 · Doble 9 · ¿Vos qué decís?
```
[ESTILO]. Left half: a close view of the calm turquoise water: Rula floating, one green leaf floating, and one colorful diving ring lying on the pale blue tiles at the bottom, clearly visible through the clear water. Right half: on the beige stone edge, a colorful plastic bucket about half full of water, and mom's hands resting next to it. No children in the picture. [REGLAS]. Wide 21:9.
```

## Páginas 20–21 · Doble 10 · Cierre
```
[ESTILO]. Left half: the pool; Tomi kicking happily with his blue kickboard toward dad, who is standing in the shallow water with his arms open; Rula floating nearby. Right half: on a quiet sunny sidewalk in front of the family house, a small green children's bicycle with a green helmet hanging from the handlebar; Tomi, a second time, standing next to it with a towel over his shoulders, dry hair, looking at the bike with shining eyes. Exactly two Tomis in the picture. [REGLAS]. Wide 21:9.
```

## Páginas 22–23 · Experimento
```
Premium children's picture book spot illustrations in exactly the same handmade cut-paper collage style as the reference, on a plain warm cream background, each item separate with plenty of empty space around it, no frames, no text, no letters, no numbers. Top left: a big plastic bowl of water with a cork and a small empty plastic bottle floating, and a metal spoon and a small stone on the bottom. Top right: an orange with its peel floating in a bowl of water, and next to it a peeled orange at the bottom of another bowl. Bottom left: a cup pouring water into a small plastic bottle. Bottom right: a smiling 6-year-old child with light chestnut hair in a green shirt, kneeling next to a bowl of water and dropping a cork into it.
```

## Página 24 · Para los grandes
```
[ESTILO]. Small calm vignette in the lower half of the image, plain light blue sky above: Tomi wrapped in a striped towel, sitting on a lounge chair by the pool next to mom, both smiling, Rula on the stone edge. Soft afternoon light. Square 1:1.
```
