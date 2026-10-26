# Así crezco, así descubro · colección de libros infantiles

> Este repositorio es solo de la colección. Se mudó acá desde el repositorio de Ofertaller el 26 de octubre de 2026.

## Qué es

Una colección de 11 libros infantiles de física y matemática. Proyecto personal, con posible venta más adelante (PDF imprimible, Amazon KDP, imprenta local). Nombre de la colección: "Así crezco, así descubro" (provisorio).

## Concepto

- **Lectores:** chicos de 5 a 7 años. El libro lo lee un adulto en voz alta.
- **Hilo de la colección:** cada libro es un hito motor del desarrollo de un bebé.
- **Narrador:** Tomi, en primera persona. Crece de libro en libro: es bebé en el libro 1 y anda en bici en el 11.
- **Compañera fija:** Rula, su pelota grande, blanda y de colores. Aparece en los 11 libros y muestra el concepto físico de cada uno.
- **Mamá y papá** acompañan de fondo; Tomi descubre solo.
- Cada libro enseña **1 concepto de física y 1 de matemática**.

## Los 11 libros

Las edades son siempre un rango aproximado.

| # | Carpeta | Hito | Edad aproximada | Física | Matemática |
| --- | --- | --- | --- | --- | --- |
| 1 | `01-girar` | Girar | 4–6 meses | Rotación: lo redondo rueda | Arriba/abajo, contar del 1 al 3 |
| 2 | `02-sentarse` | Sentarse | 6–8 meses | Equilibrio | Alto/bajo, cerca/lejos |
| 3 | `03-gatear` | Gatear | 7–10 meses | Fricción | Contar manos y rodillas |
| 4 | `04-pararse` | Pararse | 9–12 meses | Gravedad: las cosas caen | Comparar alturas |
| 5 | `05-caminar` | Caminar | 12–15 meses | Fuerza: empujar y tirar | Contar pasos, distancias |
| 6 | `06-correr` | Correr | 18–24 meses | Velocidad: rápido/lento, frenar | Ordinales |
| 7 | `07-saltar` | Saltar | 2–3 años | Gravedad: subir y bajar | Medir alturas |
| 8 | `08-subir-escaleras` | Subir escaleras | 2–3 años | Altura y esfuerzo | Secuencias |
| 9 | `09-tirar-una-pelota` | Tirar una pelota | 3–4 años | Trayectoria | Formas |
| 10 | `10-nadar` | Nadar | 4–5 años | Flotar y hundirse | Lleno/vacío, volumen |
| 11 | `11-andar-en-bici` | Andar en bici | 5–6 años | Ruedas, equilibrio en movimiento | Vueltas y ciclos |

## Reglas

- Castellano rioplatense (voseo), frases cortas, **máximo 3 frases por página** (cada página de la doble cuenta por separado).
- Estructura fija de 24 páginas: portada, 10 dobles de historia, experimento casero (en doble) y página "Para los grandes". El detalle está en `plantillas/libro.md`.
- Las edades del hito van como rango ("más o menos, cada bebé tiene su ritmo"), **nunca como fecha fija**.
- La física se simplifica, pero **nunca se dice algo falso**.
- Cada libro cierra con una **pregunta al lector** sobre cuando era bebé y un **adelanto del hito siguiente**.
- Experimentos con materiales de la casa y sin riesgo.
- Las ilustraciones respetan la seguridad del bebé: en el piso, nunca solo en lugares altos, dormir boca arriba. Detalle en `biblia/estilo-visual.md`.
- El aspecto de Tomi evoluciona con su edad en cada libro (tabla en `biblia/personajes.md`).

## Decisiones tomadas

- **25/10/2026:** estilo de ilustración A, papel recortado. Personajes de Tomi y Rula aprobados. Formato cuadrado de 21,6 cm. Experimento en doble (páginas 22–23). Máximo 3 frases por página, repartiendo el texto de cada doble.

## Estructura del proyecto

- `CLAUDE.md`: este contexto y las reglas.
- `biblia/personajes.md`: Tomi en cada edad, Rula, mamá y papá.
- `biblia/tono-y-lenguaje.md`: cómo se escribe, y la física que no se puede decir mal.
- `biblia/estilo-visual.md`: dirección de ilustración, paleta, seguridad en las imágenes, formato de impresión.
- `plantillas/libro.md`: la estructura fija de 24 páginas.
- `libros/01-girar/` … `libros/11-andar-en-bici/`: cada uno con `texto.md` e `ilustraciones.md` (un prompt de ilustración por página).

## Cómo trabajar

- Un libro por vez. **No avanzar al libro siguiente hasta que lo pida.**
- Antes de cerrar un libro, revisarlo contra estas reglas y contra la biblia, y proponer mejoras en lugar de aplicarlas sin consultar.
- Lo que no esté definido en la biblia se propone y se marca como **(propuesta)** hasta que lo apruebe.
- Guardar en Git al cerrar cada paso, con un mensaje claro en español.
