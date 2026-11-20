# Recuperación del proyecto · Así crezco, así descubro

Escrito el 31 de octubre de 2026, con la cuenta de GitHub suspendida. Sirve para retomar la colección desde cero en cualquier computadora o sesión nueva, **con o sin GitHub**. Si algo de acá contradice a `CLAUDE.md`, manda `CLAUDE.md` (es la fuente de verdad del día a día); este documento es el mapa para volver a empezar.

---

## 1. Lo primero: tener el proyecto a salvo

Todo el proyecto (textos, ilustraciones originales, maquetas, herramientas, historial de cambios) está en un único archivo:

- **`proyecto-completo.bundle`**: el repositorio entero con todo su historial (más de 60 cambios desde el 25/10/2026, ramas `main` y `claude/sharp-volta-3chy3b`). **No depende de GitHub.** Es el respaldo que hay que guardar en al menos dos lugares (la PC y una nube: Google Drive, OneDrive o Dropbox).
- Los respaldos anteriores (`respaldo.bundle`, `libro3-a-la-venta.bundle`) **no alcanzan solos**: solo traen los cambios nuevos y necesitan la parte que quedó en GitHub. Usar siempre el completo.

Lo que **no** está en el respaldo, porque se regenera con las herramientas: los PDF de KDP (`kdp/*.pdf`), las ilustraciones ampliadas (`maqueta/img-kdp/`) y los HTML de KDP (`maqueta/kdp-*.html`). Igual conviene guardar los PDF de KDP aparte: son los archivos que se suben a Amazon.

### Si el respaldo viene en partes

El respaldo del 31/10/2026 pesa 1,8 GB y se mandó en 6 partes (`proyecto-completo.bundle.parte0` a `parte5`). Antes de abrirlo hay que unirlas, en orden, en la carpeta donde estén:

- **Windows** (en "Símbolo del sistema"): `copy /b proyecto-completo.bundle.parte0+proyecto-completo.bundle.parte1+proyecto-completo.bundle.parte2+proyecto-completo.bundle.parte3+proyecto-completo.bundle.parte4+proyecto-completo.bundle.parte5 proyecto-completo.bundle`
- **Mac o Linux:** `cat proyecto-completo.bundle.parte? > proyecto-completo.bundle`

Para comprobar que quedó bien: `git bundle verify proyecto-completo.bundle` tiene que decir "is okay". Su código de control (SHA-256) es `e3c52c452d06f23a255f9854fc84c133afffdd22511e075580a6c5ed9321792e`.

### Cómo abrir el respaldo en una computadora

Hace falta Git (git-scm.com). En una terminal, en la carpeta donde se quiera el proyecto:

```
git clone proyecto-completo.bundle asi-crezco-asi-descubro
cd asi-crezco-asi-descubro
git checkout claude/sharp-volta-3chy3b
```

Si además hay respaldos chicos posteriores (por ejemplo `respaldo-desde-31oct.bundle`, con el libro 6), se suman después de abrir el completo, en orden de fecha, dentro de la carpeta del proyecto:

```
git pull ../respaldo-desde-31oct.bundle claude/sharp-volta-3chy3b
```

La rama `claude/sharp-volta-3chy3b` es la que tiene todo lo último (libros 3 a 5, KDP, correcciones del pelo). `main` es lo que estaba publicado en la web antes de la suspensión.

---

## 2. Opciones si no se recupera la cuenta de GitHub

| Opción | Qué es | Ventajas | Contras |
| --- | --- | --- | --- |
| **A. Esperar a GitHub** (recomendada mientras dure el reclamo) | Seguir en esta sesión; subir todo cuando reactiven la cuenta | No se pierde nada ni hay que mudar la web | No depende de vos; esta sesión no es eterna |
| **B. Trabajar en la PC con Claude Code** (recomendada si GitHub dice que no) | Abrir el respaldo en la PC y trabajar con la app de escritorio de Claude (Claude Code) sobre esa carpeta, o conectar una sesión en la nube a esa carpeta con Remote Control | No necesita GitHub. Todo queda en tu PC. Funciona igual que ahora | Hay que instalar las herramientas una vez (sección 6) y hacer copias de seguridad propias |
| **C. Otro servicio de repositorios** (GitLab, Bitbucket) | Subir el respaldo a otro servicio como copia en la nube | Copia segura fuera de la PC, con historial | Las sesiones de Claude Code en la web (claude.ai/code) trabajan con GitHub; con otro servicio se trabaja desde la PC (opción B) |
| **D. Cuenta nueva de GitHub** | Abrir otra cuenta | Volver a usar todo como antes | **No recomendada mientras la suspensión esté en revisión**: las condiciones de GitHub pueden considerar que es una forma de esquivar la suspensión y suspender también la nueva. Preguntarle antes al soporte de GitHub |

**Recomendación:** A mientras GitHub responda; si la respuesta es negativa, **B + C** (trabajar en la PC y guardar copia en GitLab o en una nube).

### La web (Vercel) sin GitHub

Hoy Vercel publica la web cada vez que cambia `main` en GitHub. Sin GitHub:

1. Entrar a vercel.com y, en la configuración de la cuenta, **agregar un login con mail** (si hoy se entra "con GitHub", sin GitHub no se podría entrar).
2. Publicar desde la PC: en la carpeta `web/` del proyecto, `npx vercel --prod` (pide iniciar sesión la primera vez). Las variables (`MP_ACCESS_TOKEN`) quedan guardadas en Vercel.
3. La web está en pausa (decisión del 27/10/2026), así que esto no es urgente.

### Cuentas y claves que hay que tener a mano (no se guardan en el proyecto)

| Servicio | Para qué | Dónde está |
| --- | --- | --- |
| Kie.ai | Generar y editar ilustraciones | kie.ai → API Keys. En la PC se usa como variable `KIE_API_KEY` |
| Amazon KDP | Publicar los libros | kdp.amazon.com |
| Author Central | Página de autor "Lersa" | author.amazon.com |
| Payoneer | Cobrar las regalías de KDP | Cuenta en dólares de Estados Unidos |
| Vercel | Web | vercel.com (variable `MP_ACCESS_TOKEN`) |
| Mercado Pago | Cobros de la web (en pausa) | Credenciales de prueba y de producción |
| Claude | Escribir, revisar y producir | claude.ai |

---

## 3. Arquitectura del proyecto

El proyecto es una "fábrica" de libros: los textos y las reglas son archivos de texto; las ilustraciones se generan con IA (Kie.ai) a partir de indicaciones guardadas; unos programas arman cada libro como página web (HTML) y lo convierten a PDF para tres destinos.

```
Biblia (personajes, tono, estilo, idiomas)
        │
        ▼
Texto del libro (rioplatense) ──► traducción (español neutro, inglés)
        │
        ▼
Indicaciones de ilustración + hojas de personajes ──► Kie.ai ──► ilustraciones/
        │
        ▼
Maqueta (maqueta/libroN.py → HTML) ──► PDF de borrador (web, personalizable)
        │                         └──► KDP (kdp.py → interior a 400 dpi + tapa)
        ▼
Web (web/, Vercel + Mercado Pago, en pausa)       Amazon KDP (tapa blanda, Tommy)
```

Tres productos salen del mismo material:

1. **Borrador rioplatense personalizable** (web): Tomi o Emi, con el nombre que elija el cliente. En pausa.
2. **KDP en español neutro**: Tommy, serie "Así crezco, así descubro".
3. **KDP en inglés**: Tommy, serie "I Grow, I Discover".

---

## 4. Estructura de carpetas

| Carpeta o archivo | Qué hay |
| --- | --- |
| `CLAUDE.md` | Reglas, decisiones y estado. Lo primero que hay que leer (y lo primero que lee Claude) |
| `PROJECT-RECOVERY.md` | Este documento |
| `costos.md` | Créditos de Kie.ai y dólares gastados por libro |
| `biblia/personajes.md` | Tomi, Emi, Rula, mamá y papá; evolución por libro (pelo, dientes, ropa) |
| `biblia/tono-y-lenguaje.md` | Cómo se escribe y la física que no se puede decir mal (tabla de trampas por libro) |
| `biblia/estilo-visual.md` | Estilo de ilustración, seguridad del bebé en las imágenes, formato de impresión |
| `biblia/idiomas.md` | Glosario rioplatense → neutro, reglas del inglés, títulos |
| `plantillas/libro.md` | Estructura fija de 24 páginas y lista de control |
| `libros/NN-hito/` | `texto.md` (rioplatense), `texto-es.md` (neutro), `texto-en.md` (inglés), `ilustraciones.md` (indicaciones de cada página) y los PDF de borrador |
| `ilustraciones/libroN/` | Ilustraciones originales en PNG (`-v1`, `-v2`, `-pelo2`, `-c` = corregida a mano; `-v0-*` = descartadas) |
| `ilustraciones/libroN-emi/` | Versión mujer |
| `ilustraciones/referencias/` | Hojas de personajes de cada libro (Tomi y Emi), hoja del living; `anteriores/` guarda versiones viejas |
| `ilustraciones/herramientas/` | Programas para generar y editar imágenes y los bloques de estilo (`style-libroN.txt`) |
| `ilustraciones/README.md` | Qué versión de cada imagen se usa y cómo se hizo |
| `maqueta/` | Arma los libros: `libroN.py`, `comun.py`, `pdf.js`; KDP: `kdp*.py`, `kdp*.js` |
| `maqueta/img/` | Ilustraciones comprimidas que usa la maqueta (`lN-` Tomi, `lNe-` Emi) |
| `kdp/` | `fichas.md` (datos de cada libro para KDP), `guia-libro1.md` (paso a paso en inglés), `author-central.md` (biografías) y los PDF finales (no van en Git) |
| `web/` | Web, funciones de pago (`api/`), plantillas privadas del PDF personalizado (`privado/`) |

---

## 5. Flujo completo de producción de un libro

Regla de oro: **un libro por vez** y **nada de créditos sin aprobación**.

1. **Texto** (sin créditos). Escribir `libros/NN-hito/texto.md` siguiendo `plantillas/libro.md` y la biblia. Revisar: máximo 3 frases por página, voseo, edad como rango, física verdadera (tabla de trampas), concepto de matemática más de una vez, Rula muestra la física, cierre con pregunta al lector y adelanto. Sin palabras con género (sirve para Tomi y Emi). → **aprobación**.
2. **Evolución de personajes** (sin créditos). Poner lado a lado las hojas de los libros anteriores, proponer pelo, dientes, ropa y lo que puede hacer, y preguntar lo que no esté definido. Anotar en `biblia/personajes.md`. → **aprobación**.
3. **Hojas de personajes** (unos 24 a 48 créditos). Editar la hoja del libro anterior con Nano Banana 2 (prompt de la sección 7). Emi: editar la hoja de Tomi del mismo libro. → **aprobación**.
4. **Indicaciones de ilustración** (sin créditos). `libros/NN-hito/ilustraciones.md` con una indicación por página y el bloque `herramientas/style-libroN.txt`.
5. **Prueba de 2 ilustraciones** (36 créditos) y revisión. Si el estilo se desvía, corregir la indicación antes del lote.
6. **Lote** (unos 200 créditos) con `generar_libro.py`. Revisar todas en una hoja de contactos: caras en el pliegue, objetos duplicados, letras o números dibujados, adultos cambiados, estilo plano.
7. **Correcciones**: primero gratis (pegar zonas desde la versión anterior, borrar detalles chicos), si no, una edición de 12 créditos.
8. **Maqueta** (`maqueta/libroN.py`) y PDF de borrador. Revisar las páginas enteras (que el texto no tape caras). → **aprobación**.
9. **Traducción** a español neutro e inglés (`texto-es.md`, `texto-en.md` y `maqueta/kdp_textos.py`).
10. **KDP**: ampliar ilustraciones, armar interior y tapa, revisar márgenes y páginas enteras (comandos en la sección 6), ficha en `kdp/fichas.md`.
11. **Versión mujer (Emi)**, cuando se decida: editar cada página de Tomi con la hoja de Emi (unos 156 créditos).
12. **Guardar** (copia del proyecto) y anotar créditos en `costos.md`.

### Comandos

Desde la carpeta del proyecto:

```
# Ilustraciones (necesita KIE_API_KEY)
export KIE_API_KEY=tu_clave
python3 ilustraciones/herramientas/subir.py ilustraciones/referencias/hoja-personajes-libroN.png   # devuelve una URL temporal
python3 ilustraciones/herramientas/generar_libro.py N URL_HOJA URL_PAGINA_DE_ESTILO p01 d06            # prueba de 2
python3 ilustraciones/herramientas/generar_libro.py N URL_HOJA URL_PAGINA_DE_ESTILO                    # todas
python3 ilustraciones/herramientas/kie.py nano-banana-2 auto 2K salida.png "INDICACIÓN" URL_IMAGEN [URL_REF]  # una edición
curl -H "Authorization: Bearer $KIE_API_KEY" https://api.kie.ai/api/v1/chat/credit                  # créditos que quedan

# Maqueta y borrador
cd maqueta && python3 libroN.py && cd ..
node maqueta/pdf.js maqueta/libroN.html libros/NN-hito/libro-N-borrador-ilustrado.pdf

# KDP (N = número de libro; es o en)
python3 maqueta/kdp_ampliar.py
cd maqueta && python3 kdp.py N es && python3 kdp_tapa.py N es && cd ..
node maqueta/kdp_margenes.js maqueta/kdp-libroN-es.html          # tiene que decir OK
python3 maqueta/kdp_raster.py maqueta/kdp-libroN-es.html kdp/libroN-es-interior.pdf
node maqueta/kdp_pdf.js maqueta/kdp-tapa-libroN-es.html kdp/libroN-es-tapa.pdf 17.3063in 8.75in
python3 maqueta/kdp_medida.py kdp/libroN-es-tapa.pdf 17.3063 8.75
```

Para un libro nuevo hay que sumar su entrada en `maqueta/kdp_ampliar.py` (qué imagen usa cada página), `maqueta/kdp_textos.py` (`TITULOS`, `LIBROS` y palabras grandes) y `maqueta/kdp_tapa.py` (`CONTRATAPA`). `kdp.py` se detiene y lista lo que falte traducir.

---

## 6. Dependencias y herramientas

| Herramienta | Para qué | Instalación |
| --- | --- | --- |
| Git | Abrir el respaldo y guardar versiones | git-scm.com |
| Python 3.11 o más nuevo | Maquetas, KDP, ilustraciones | python.org |
| Pillow, pypdf | Imágenes y PDF | `pip install pillow pypdf` |
| opencv-python-headless | Solo para borrar detalles chicos a mano | `pip install opencv-python-headless` |
| Node.js 18 o más nuevo | Pasar las maquetas a PDF, web | nodejs.org |
| Playwright + Chromium | Navegador que saca los PDF y las fotos de cada página | `npm install playwright` y `npx playwright install chromium` |
| poppler (pdftoppm, pdfinfo) | Revisar PDF como imágenes | En Mac: `brew install poppler`; en Windows: se puede omitir |
| curl | Llamadas a Kie.ai | Viene con Mac, Linux y Windows 10/11 |
| Internet | Las tipografías (Andika y Fraunces) se cargan desde Google Fonts al armar las maquetas | — |
| Kie.ai | Nano Banana Pro (imagen nueva, 18 créditos en 2K) y Nano Banana 2 (edición, 12 créditos en 2K) | 1.000 créditos = USD 5 |
| Claude (app de escritorio con Claude Code) | Escribir, revisar, generar y armar todo | claude.ai/download |

En Windows, lo más simple es usar WSL (Ubuntu dentro de Windows) para que los comandos funcionen igual.

---

## 7. Indicaciones maestras ("prompts")

### Bloque de estilo de las páginas (libro 5, `style-libro5.txt`)

Se pega al principio de cada indicación de página. Para un libro nuevo, copiarlo y cambiar solo la descripción de Tomi (edad, pelo, dientes, ropa) según `biblia/personajes.md`, y el lugar si cambia.

```
Premium children's picture book illustration in exactly the same handmade cut-paper collage style, palette, paper textures and warm lighting as the second reference image, a page of the same book series (gouache-painted papers, crisp scissor-cut edges, tiny soft shadows between paper layers, warm cream wall, warm wooden plank floor). The living room: a tall window with a white wooden frame, a low sturdy beige three-seat sofa with a backrest, armrests and two cream cushions, a large soft knitted cream-and-ochre rug with fringes, a low rectangular wooden coffee table with rounded corners, a low open cardboard toy box with big soft fabric toys (a plush bear and plain fabric blocks with no letters or symbols), a simple wooden dining table, a glass door to a sunny patio with plants, a green potted plant. The toddler Tomi must look exactly like in the character sheet: a 13-month-old toddler boy with a round toddler belly, legs a little apart when he walks, short light chestnut-brown hair lying flat and close to the scalp with no volume and no curl, honey-colored eyes, light warm peach skin, pink cheeks, four tiny white teeth on top and four on the bottom when he smiles, leaf-green short-sleeved t-shirt with a tiny colorful ball printed on the chest, short soft gray shorts, leaf-green non-slip socks, no shoes. Rula is a large soft ball, about as big as the toddler's whole torso, six vertical segments red, orange, yellow, leaf green, sky blue, violet. Adults keep light skin; mom has curly hair tied up and round glasses, dad has a short beard and a mustard sweater. The toddler always stays on the floor, never climbs on furniture; an adult partially visible nearby. No small objects near the toddler, no stairs, no kitchen, no plugs or cables, no baby walker. Full-bleed, no frame, no border, no dividing line. No text, no letters, no numbers, no footprints drawn anywhere.
```

Referencias que se pasan en cada página: **primero la hoja de personajes del libro, segundo una página ya aprobada del libro anterior** (para el estilo). La hoja del living (`referencias/set-living.png`) **no** se pasa: salió con un estilo plano y las páginas se volvían planas.

### Reglas fijas (bloque [REGLAS], al final de cada indicación)

```
Only mom and dad may appear as adults, each at most once, no other people. An adult partially visible nearby. No small objects near the toddler. Keep faces and the ball away from the vertical center line. Calm plain area in the upper part for text.
```

Formato: dobles en 21:9 (se recortan a 2:1), portada y página 24 en 1:1, experimento en 3:2.

### Hoja de personajes de un libro nuevo (edición de la hoja anterior, Nano Banana 2)

```
Edit the first image, a character sheet, with minimal changes, keeping the same layout, the same number of figures, the same cut-paper style and the same cream background. The baby boy is now about [EDAD]: the same face, same honey-colored eyes, same light warm peach skin and pink cheeks, [CAMBIOS DE CUERPO]. Hair: [PELO SEGÚN LA BIBLIA, IGUAL O MÁS QUE EL LIBRO ANTERIOR]. Teeth: [DIENTES]. Clothes in every figure: [ROPA]. [CAMBIO DE POSE DE UNA FIGURA, SI HACE FALTA]. Keep the ball exactly the same. Only one figure per pose, no extra figures, no other objects. No text, no letters, no numbers.
```

Las hojas no llevan objetos ni poses de otros libros, porque el modelo los copia en las páginas.

### Emi: hoja y páginas (edición sobre Tomi, Nano Banana 2)

```
Edit this character sheet with very small changes: every figure becomes the same toddler as a GIRL. In every figure add a small coral-pink flower hair clip on one side of the head just above the ear, and tiny eyelashes. Keep the hair EXACTLY as it is now (same short length, same shape, same color, do not make it longer, no ponytail, no tuft, no bow). Keep everything else exactly identical. No extra figures, no text.
```

Para las páginas, el mismo pedido con la página de Tomi como primera imagen y la hoja de Emi como segunda ("the second image is ONLY a character reference: never copy its layout"). Problema conocido: a veces alarga el pelo de algunas figuras o cambia a los adultos; se arregla pegando la zona desde la imagen de Tomi.

### Corregir algo puntual (edición)

```
Edit this image with minimal changes: [UN SOLO CAMBIO, CONCRETO]. Keep everything else exactly identical: [LISTA DE LO QUE NO SE TOCA: personajes, adultos, Rula, muebles, colores, estilo de papel recortado]. No text.
```

### Para retomar con Claude en una sesión nueva

```
Estoy retomando mi colección de libros infantiles "Así crezco, así descubro". Leé CLAUDE.md y PROJECT-RECOVERY.md antes de hacer nada. Seguimos las reglas de "Cómo trabajar": un libro por vez, nada de créditos sin mi aprobación y revisión de la evolución de los personajes antes de ilustrar. El próximo paso es: [LO QUE QUIERAS HACER].
```

---

## 8. Decisiones creativas y visuales

- **Colección:** 11 libros, un hito motor por libro; 1 concepto de física y 1 de matemática. Lectores de 4 a 7 años, leído en voz alta por un adulto.
- **Narrador:** Tomi en primera persona (Tommy en KDP). Rula, la pelota de seis gajos (rojo, naranja, amarillo, verde, celeste, violeta) sin cara, muestra la física. Mamá (pelo enrulado atado, anteojos redondos) y papá (barba corta, buzo mostaza) de fondo.
- **Estilo:** papel recortado con gouache, fondo crema cálido, piso de madera, living fijo (sillón beige con respaldo, alfombra tejida, mesita, mesa, ventana, puerta al patio).
- **Formato:** cuadrado de 21,6 cm (8,5 × 8,5 in), 24 páginas: portada, 10 dobles, experimento en doble y "Para los grandes".
- **Escritura:** rioplatense con voseo para la web; español neutro con tuteo y en inglés para KDP. Máximo 3 frases por página. Una onomatopeya por libro. Edad del hito siempre como rango. Física simplificada pero nunca falsa.
- **Seguridad en las imágenes:** bebé en el piso, nunca solo en lugares altos, siempre un adulto cerca, nada chico cerca de la boca, sin andador.
- **La IA no dibuja textos, números ni medidas:** huellitas, líneas de altura, números y palabras grandes (ARRIBA, GRAVEDAD, EMPUJAR…) se agregan en la maqueta.
- **Personalización (web):** mujer o varón y nombre; el nombre va solo en la tapa y en la doble 1; el texto no tiene palabras con género.
- **Evolución del pelo (corregida el 28/10/2026):** libro 1 casi pelado con remolino; 2 pelusa fina; 3 pelusa un poco más tupida con remolino; 4 pelo cortito y fino sin remolino; 5 pelo corto pegado sin volumen; desde el 6, pelo de nene. Nunca menos que en el libro anterior. Emi: igual que Tomi, con mechoncito y flor (libros 1 a 3) y ganchito con flor coral arriba de la oreja (desde el 4).
- **Ropa de Tomi:** body verde (1 a 3), remera verde con la pelotita y pañal (4), remera verde, short gris y medias verdes antideslizantes (5; zapatillas recién en la última página).
- **KDP:** tapa blanda, sin personalizar, Tommy, autor **"Lersa"** (la tapa dice "by LERSA" por diseño), USD 12,99, Premium Color, sangrado, mate, sin distribución ampliada.

---

## 9. Estado de los 11 libros (31/10/2026)

| # | Libro | Texto | Ilustraciones Tomi | Emi | Maqueta y borrador | KDP (archivos) | KDP (Amazon) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Girar | Aprobado | Listas | Listas | Listo | Listos | **Publicado** en inglés (B0HPS5H68W) y español (B0HPS5LPS9) |
| 2 | Sentarse | Aprobado | Listas | Listas | Listo | Listos | Sin cargar (próximo, por el límite semanal) |
| 3 | Gatear | Aprobado | Listas (pelo corregido el 28/10) | Con el pelo viejo: rehacer | Listo | Listos | Sin cargar |
| 4 | Pararse | Aprobado | Listas (pelo corregido el 28/10) | Falta | Listo (solo Tomi) | Listos | Sin cargar |
| 5 | Caminar | Aprobado | Listas | Falta (hoja lista) | Listo (solo Tomi) | Listos | Sin cargar |
| 6 | Correr | Aprobado | Listas | Falta | Listo (solo Tomi) | Listos | Sin cargar |
| 7 | Saltar | Aprobado | Listas | Falta | Listo (solo Tomi) | Listos | Sin cargar |
| 8 | Subir escaleras | Aprobado | Listas | Falta | Listo (solo Tomi) | Listos | Sin cargar |
| 9 | Tirar una pelota | Aprobado | Listas | Falta | Listo (solo Tomi) | Listos | Sin cargar |
| 10 | Nadar | Aprobado | Listas | Falta | Listo (solo Tomi) | Listos | Sin cargar |
| 11 | Andar en bici | Aprobado | Listas | Falta | Listo (solo Tomi) | Listos | Sin cargar |

Lo que ya está definido para los libros 6 a 11 (en `CLAUDE.md`, `biblia/personajes.md` y `biblia/tono-y-lenguaje.md`): edad, concepto de física y de matemática, qué hace Rula, ropa de Tomi y la trampa de física a evitar. Antes de ilustrar el 9 al 11 hay que armar hojas de lugares nuevos (plaza, pileta, vereda) y pensar la ropa.

**Créditos de Kie.ai** gastados hasta hoy: unos 3.600 en total, unos USD 18 (detalle en `costos.md`). Un libro nuevo, solo Tomi, cuesta unos 300 a 450 créditos (USD 1,50 a 2,25); la versión de Emi, unos 156 más.

---

## 10. Próximos pasos para continuar

1. **Guardar el respaldo completo** (`proyecto-completo.bundle`) en la PC y en una nube. Guardar también los PDF de KDP.
2. **KDP:** cargar un libro por semana en los dos idiomas (límite de cuentas nuevas): libro 2, después 3 a 8, con autor "Lersa" y los archivos y fichas actuales. Pedir una copia de autor del libro 1.
3. **Author Central:** cargar las biografías (`kdp/author-central.md`), la foto cuando lo permita y el link de autor (por ejemplo `lersabooks`).
4. **Revisar los textos traducidos** (español neutro e inglés) de los libros 2 a 8 antes de publicarlos.
5. **Los 11 libros están terminados (versión varón).** Siguientes pasos posibles: recopilatorios 5 a 8 y 9 a 11, contenido A+ de los libros 4 a 11, versión Emi y, cuando se retome, la web. texto → evolución → hojas → prueba → lote → maqueta → traducción → KDP.
6. **Versión de Emi** de los libros 3 (rehacer con el pelo nuevo), 4 y 5, cuando se retome la web.
7. **Si GitHub no vuelve:** instalar las herramientas en la PC (sección 6), abrir el respaldo y seguir con Claude Code ahí; guardar copias semanales del proyecto.
8. **Contenido A+ en KDP** (imágenes debajo de la descripción): se puede armar con las páginas que ya existen, sin créditos.
