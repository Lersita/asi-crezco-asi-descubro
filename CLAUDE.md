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
- **26/10/2026:** Tomi con piel un par de tonos más clara, pelo castaño claro y ojos miel. Versión mujer: **Emi**, igual a Tomi, con pelo muy cortito, un mechón con una flor coral y la misma piel. El protagonista se personaliza: el cliente elige mujer o varón y escribe el nombre (va en la tapa, "{Nombre} aprende a girar", y en la frase de la doble 1). En la web se dice "mujer" y "varón", nunca "nena" o "nene".
- **26/10/2026:** el texto de los libros no nombra al protagonista fuera de la tapa y la doble 1 (si no, el PDF personalizado diría "Tomi"). La versión mujer cambia solo las palabras con género.
- **27/10/2026:** venta del **PDF digital** con Mercado Pago (Checkout Pro). Precios: 1 libro $18.999; 2 libros $34.199; 3 libros $48.499; colección de 11 $124.999. Hoy solo se venden 1 y 2 (hay 2 libros listos); 3 y 11 se muestran como "próximamente". El **impreso** en tapa dura (con el PDF de regalo al instante, en una sola compra) queda para cuando haya presupuesto de imprenta.

## Estado (27/10/2026)

- **Libros 1 y 2:** texto, ilustraciones (varón y mujer) y PDF de borrador listos. Libro 3 en adelante: sin empezar.
- **Web:** publicada en Vercel (https://asi-crezco-asi-descubro-web.vercel.app), carpeta `web/`. Personalizador, visor (desde la quinta doble se ve borroso), precios y packs, compra con Mercado Pago y descarga en `gracias.html`. Probado de punta a punta **en modo prueba** (credencial de un usuario vendedor de prueba en la variable `MP_ACCESS_TOKEN` de Vercel). Detalle técnico en `web/README.md`.
- **Créditos de Kie.ai:** quedaban unos 670 el 27/10/2026. Cada imagen nueva con Nano Banana Pro cuesta 18; cada edición con Nano Banana 2 en 2K, 12.

### Pendiente para vender de verdad

1. Cargar en Vercel la credencial de **producción** de la cuenta real de Mercado Pago (y volver a publicar).
2. Sacar las etiquetas "Prototipo · ilustraciones de prueba" y "Borrador".
3. Contacto para consultas (falta que el usuario lo pase).
4. Página de términos y privacidad (Ley 25.326).
5. Facturación: lo resuelve el usuario con su contador.
6. Opcional: mandar el PDF también por mail; mejorar la resolución de las ilustraciones para imprimir.

## Estructura del proyecto

- `CLAUDE.md`: este contexto y las reglas.
- `biblia/personajes.md`: Tomi en cada edad, Rula, mamá y papá. `biblia/tono-y-lenguaje.md`: cómo se escribe y la física que no se puede decir mal. `biblia/estilo-visual.md`: estilo, seguridad en las imágenes, formato de impresión.
- `plantillas/libro.md`: la estructura fija de 24 páginas.
- `libros/NN-hito/`: `texto.md`, `ilustraciones.md` (prompts) y los PDF de borrador.
- `ilustraciones/`: imágenes originales. `README.md` dice qué versión se usa en cada página y cómo se hicieron. `herramientas/kie.py` genera o edita una imagen con Kie.ai.
- `maqueta/`: arma cada libro en HTML (`libro1.py`, `libro1_emi.py`, `libro2.py`, `libro2_emi.py`, con piezas comunes en `comun.py`) y lo pasa a PDF con `pdf.js`.
- `web/`: la web y las funciones de pago. Ver `web/README.md`.

## Cómo se hace cada cosa

- **Ilustrar un libro:** hoja de personajes de la edad nueva (editando la anterior) → cada doble con Nano Banana Pro en 2K y 21:9, pasando la hoja y una portada como referencia → revisar todas juntas en una hoja de contactos → corregir. La versión mujer se hace **editando** las imágenes del varón con Nano Banana 2 y la hoja de Emi.
- **Problemas conocidos de las ediciones:** a veces cambian la piel o la cara de los adultos, o dejan una viñeta sin cambiar. Arreglo sin gastar créditos: unir la zona del adulto desde la versión anterior (las imágenes quedan alineadas). Para una viñeta, editar solo ese recorte. Las URL de Kie.ai (tempfile) vencen: guardar siempre la imagen en `ilustraciones/`.
- **Después de cambiar ilustraciones o texto:** maqueta (`python3 maqueta/libroN.py`) → PDF (`node maqueta/pdf.js maqueta/libroN.html salida.pdf`) → plantillas de la web (`node web/herramientas/plantillas.js`) → vistas previas (`python3 web/herramientas/vista.py`) → guardar en Git (Vercel publica solo).
- **Sumar un libro a la venta:** agregarlo en `web/precios.json`, en `api/_pdf.js` (título y frase de la doble 1) y en el visor de `web/index.html`.

## Cómo trabajar

- Un libro por vez. **No avanzar al libro siguiente hasta que lo pida.**
- Antes de cerrar un libro, revisarlo contra estas reglas y contra la biblia, y proponer mejoras en lugar de aplicarlas sin consultar.
- Lo que no esté definido en la biblia se propone y se marca como **(propuesta)** hasta que lo apruebe.
- Guardar en Git al cerrar cada paso, con un mensaje claro en español.
