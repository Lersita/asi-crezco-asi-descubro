# Ilustraciones

Ilustraciones generadas con inteligencia artificial (Kie.ai, modelo Nano Banana Pro, resolución 2K) el 26 de octubre de 2026. Estilo A, papel recortado.

## Cómo se hacen

1. **Referencias fijas** (`referencias/`): la hoja de personajes de Tomi y Rula. Junto con la portada (`borradores/p01-portada-v2.png`), es la referencia de estilo de todas las páginas.
2. **Cada página** se genera pasando esas dos imágenes como referencia y el bloque de estilo de `herramientas/style2.txt`, más la escena de `libros/01-girar/ilustraciones.md`.
3. **Correcciones chicas** (por ejemplo, sacar letras) se hacen editando la imagen con Nano Banana 2, que es más barato.
4. Las dobles salen en 21:9 y la maqueta las recorta a 2:1. Las dobles 4 y 10 se recompusieron (`*-compuesta.png`) para que nada importante caiga en el pliegue.

Script: `herramientas/kie.py MODELO ASPECTO RESOLUCION SALIDA.png "PROMPT" [URL_REFERENCIA ...]`.

Costo: 18 créditos por imagen con Nano Banana Pro en 2K, y 12 créditos por edición con Nano Banana 2.

## Versión elegida por página (libro 1)

Desde el 26 de octubre de 2026, Tomi tiene la piel un par de tonos más clara, el pelo castaño claro y los ojos miel. Los cambios se hicieron editando cada imagen con Nano Banana 2. En las dobles 2 y 6, la edición también había cambiado la piel de los adultos; se arregló uniendo la zona del adulto de la versión anterior (sin gastar créditos).

| Página | Archivo |
| --- | --- |
| Hoja de personajes | `referencias/hoja-personajes-v2.png` |
| 1 Portada | `p01-portada-v2.png` |
| 2–3 | `d01-v3.png` |
| 4–5 | `d02-v4.png` |
| 6–7 | `d03-v3.png` |
| 8–9 | `d04-v3-compuesta.png` |
| 10–11 | `d05-v2.png` |
| 12–13 | `d06-v3.png` |
| 14–15 | `d07-v2.png` |
| 16–17 | `d08-v2.png` |
| 18–19 | `d09-v2.png` |
| 20–21 | `d10-v3-compuesta.png` |
| 22–23 | `exp-v2.png` |
| 24 | `p24-cuna-v2.png` |

Libro 2: hoja de personajes en `referencias/hoja-personajes-libro2.png` (Tomi de unos 7 meses).

## Pendiente para la versión final

- Subir a 4K o ampliar las imágenes elegidas: para imprimir a 300 puntos por pulgada, una doble necesita unos 5.100 píxeles de ancho.
- Revisar el pliegue en cada doble con la imprenta o con la plantilla de Amazon KDP.

## Maqueta

`maqueta/libro1.py` arma el HTML y `maqueta/pdf.js` lo pasa a PDF (`libros/01-girar/libro-1-borrador-ilustrado.pdf`). Usa las imágenes comprimidas de `maqueta/img/`.

## Libro 2 (carpeta `libro2/`)

Generado el 26 de octubre de 2026 con Nano Banana Pro en 2K, con referencias `referencias/hoja-personajes-libro2.png` (personaje) y `borradores/p01-portada-v2.png` (estilo). Bloque de estilo: `herramientas/style-libro2.txt`. Maqueta: `maqueta/libro2.py`, que usa las piezas comunes de `maqueta/comun.py`.

| Página | Archivo |
| --- | --- |
| 1 Portada | `p01-portada-v1.png` |
| 2–3 a 18–19 | `d01-v1.png` … `d09-v1.png` |
| 20–21 | `d10-compuesta.png` (a partir de `d10-v3.png`: la secuencia de la izquierda y Tomi en cuatro patas a la derecha) |
| 22–23 | `exp-v1.png` |
| 24 | `p24-v1.png` |

## Emi, versión 2 (carpeta `emi2/`, vigente)

Desde el 26 de octubre de 2026, Emi tiene el pelo muy cortito (pelusita de bebé con un mechoncito y la misma flor coral) y la misma piel que Tomi. Hoja: `referencias/hoja-personajes-emi-v2.png`. Se editaron otra vez las ilustraciones de Tomi del libro 1.

- Doble 4: viñetas 1 y 2, y viñeta 3, editadas por separado y recompuestas en `d04-compuesta.png`.
- Doble 6: se devolvió la zona de papá desde la versión original (`d06-v2.png`).
- Doble 7: se sacó una pelota que había aparecido en el borde izquierdo (`d07-v2.png`).
- Doble 8: se volvió a editar porque había cambiado a mamá (`d08-v2.png`).


## Libro 2, versión mujer (carpeta `libro2-emi/`)

Hecho el 26 de octubre de 2026 editando las ilustraciones de Tomi del libro 2 con la hoja `referencias/hoja-personajes-emi-libro2.png` (Emi de unos 7 meses). Maqueta: `maqueta/libro2_emi.py` → `libros/02-sentarse/libro-2-emi-borrador-ilustrado.pdf`.

## Limpieza

El 27 de octubre de 2026 se borraron las versiones descartadas (pruebas, la primera Emi y las hojas de personajes reemplazadas). Siguen en el historial de Git si alguna vez hacen falta. En `borradores/`, `emi2/` y `libro2/` quedan solo las imágenes de las tablas de arriba y las originales de las dobles compuestas.

## Libro 3 (carpetas `libro3/` y `libro3-emi/`)

Generado el 27 de octubre de 2026 con Nano Banana Pro en 2K, con referencias `referencias/hoja-personajes-libro3.png` (Tomi de unos 9 meses: dos dientitos abajo y pantalón largo gris) y `libro2/p01-portada-v1.png` (estilo y living). Bloque de estilo: `herramientas/style-libro3.txt`. Se generan todas juntas con `herramientas/generar_libro3.py` (lee los prompts de `libros/03-gatear/ilustraciones.md`). Para pasar referencias locales, `herramientas/subir.py` las sube a Kie.ai y devuelve la URL.

| Página | Varón (`libro3/`) | Mujer (`libro3-emi/`) |
| --- | --- | --- |
| 1 Portada | `p01-v1.png` | `p01.png` |
| 2–3 a 10–11 | `d01-v1.png` … `d05-v1.png` | `d01.png` … `d05.png` |
| 12–13 | `d06-v2.png` (rehecha: primer plano de mano y rodilla en la alfombra) | `d06.png` |
| 14–15 | `d07-v1.png` | `d07.png` |
| 16–17 | `d08-v2.png` (se borró una mano de adulto que parecía empujar a Rula) | `d08-v2.png` (se devolvió la zona del adulto desde la de Tomi: la edición le había agregado una cara) |
| 18–19 | `d09-v1.png` | `d09.png` |
| 20–21 | `d10-v2.png` (editada con Nano Banana 2 para que mire hacia el sillón) | `d10.png` |
| 22–23 | `exp-v1.png` | `exp.png` |
| 24 | `p24-v1.png` | `p24.png` |

Versión mujer: hoja `referencias/hoja-personajes-emi-libro3.png` y `herramientas/emi_libro3.py`, que edita cada imagen de Tomi con Nano Banana 2. Maqueta: `maqueta/libro3.py` arma las dos versiones (`libro3.html` y `libro3-emi.html`). La doble 8 se muestra entera (sin recortar a 2:1) porque son dos escenitas sobre fondo crema.

Créditos usados en el libro 3: unos 470 (hojas de personajes 48, Tomi 234 más 30 de correcciones, Emi 156). Quedaron 206.

## Pelo corregido en los libros 2 y 3 (27 de octubre de 2026)

El pelo no crecía entre libros. Se aprobó la evolución que está en `biblia/personajes.md`: libro 2 con pelusa en toda la cabeza, libro 3 con pelo corto parejo, con el remolino en los dos, y Emi con el mismo pelo que Tomi, más el mechoncito y la flor coral.

- Hojas de personajes nuevas, con los mismos nombres de archivo de antes: `referencias/hoja-personajes-libro2.png`, `hoja-personajes-libro3.png`, `hoja-personajes-emi-libro2.png` y `hoja-personajes-emi-libro3.png`.
- Todas las páginas con bebé de los libros 2 y 3, en las dos versiones, se editaron con `herramientas/pelo.py` (Nano Banana 2, una edición por página). Los archivos se reemplazaron con los mismos nombres; las versiones anteriores siguen en el historial de Git. El experimento no cambió, porque en él no aparece el bebé.
- Arreglos sin gastar créditos: en `libro2/d10-compuesta.png` se devolvió el borde derecho (la edición había agregado a mamá) y en `libro3/d07-v1.png` la esquina de arriba a la izquierda (había agregado una cara).
- Se repitieron 3 ediciones: `libro2/p24-v1.png`, porque había perdido el remolino, y `libro2-emi/d04.png` y `d10-compuesta.png`, porque la edición había agregado una línea punteada y una hoja de personajes.
- Las figuras de Tomi de la web (`web/img/tomi-solito.webp` y `tomi-cuatro-patas.webp`) se recortaron de la hoja nueva del libro 2.

## Libro 4 (carpetas `libro4/` y `libro4-emi/`)

Generado el 27 de octubre de 2026 con Nano Banana Pro en 2K, con referencias `referencias/hoja-personajes-libro4.png` (Tomi de unos 11 meses: pelo más largo y despeinado sin remolino, cuatro dientes, remera verde y pañal) y `libro3/d10-v2.png` (estilo y living). Bloque de estilo: `herramientas/style-libro4.txt`. Se genera con `herramientas/generar_libro.py 4`, que sirve para cualquier libro.

- La hoja de Tomi se editó para que no cargue la caja ni camine, y se borró a mano una figura que seguía cargándola.
- La tapa y las dobles 1 a 5 salieron con un banco sin respaldo; se editaron (`*-v2.png`) para que el sillón sea el mismo con respaldo de las demás páginas.
- La doble 7 se rehízo (`d07-v2.png`) porque la línea de la cabeza de Tomi quedaba a la altura de la mesa.
- En el experimento se borraron a mano unos números "(1) (2) (3)" que había escrito la IA.
- Doble 5: en el borde derecho aparece otro papá, pero queda afuera al recortar la doble a 2:1.

| Página | Varón (`libro4/`) |
| --- | --- |
| 1 Portada | `p01-v2.png` |
| 2–3 a 10–11 | `d01-v2.png` … `d05-v2.png` |
| 12–13 | `d06-v1.png` |
| 14–15 | `d07-v2.png` |
| 16–17 a 20–21 | `d08-v1.png` … `d10-v1.png` |
| 22–23 | `exp-v1.png` |
| 24 | `p24-v1.png` |

Las versiones `-v1` de la tapa y de las dobles 1 a 5 quedan como originales de las editadas.

## Segunda corrección del pelo (28 de octubre de 2026)

La curva del pelo se bajó desde el libro 3 (ver `biblia/personajes.md`). Hojas nuevas en `referencias/` (las anteriores, en `referencias/anteriores/`). Las páginas de Tomi de los libros 3 y 4 se editaron con `herramientas/pelo2.py` (Nano Banana 2) y quedaron como `libroN/<página>-pelo2.png`. Arreglos a mano, pegando la zona desde la imagen anterior: libro 3 página 24 (cara de papá) y libro 4 dobles 3 (línea punteada de más), 4 (mamá había quedado pelada) y 10 (una segunda pelota); se guardaron como `-pelo2-c.png`. El experimento no se tocó (muestra al lector, no a Tomi). La versión de Emi de los libros 3 y 4 todavía usa las imágenes anteriores: se rehace más adelante.

## Libro 5 · Caminar (28 de octubre de 2026)

Nano Banana Pro en 2K con `herramientas/generar_libro.py 5`, pasando la hoja `referencias/hoja-personajes-libro5.png` y `libro4/d10-pelo2-c.png` para el estilo. Bloque de estilo: `herramientas/style-libro5.txt`, que describe el living con palabras. La hoja del living (`referencias/set-living.png`) **no se pasa**: tiene un estilo plano y las páginas salían planas (se probó también pasarla a papel recortado, sin éxito). Todas las páginas son `-v1`. Correcciones: doble 2 rehecha (una cara en el pliegue), doble 4 editada desde una versión con dos pelotas, doble 5 editada (la manta estaba cortada), doble 9 rehecha (estilo plano) y en la doble 8 se borró a mano una letra de un cubito. Las descartadas quedan como `-v0-*`. Las huellitas y sus números se dibujan en la maqueta (`maqueta/libro5.py`). Solo versión varón por ahora.

## Libro 6 · Correr (31 de octubre de 2026)

Nano Banana Pro en 2K con `herramientas/generar_libro.py 6`, pasando la hoja `referencias/hoja-personajes-libro6.png`, la portada del libro 6 (`libro6/p01-v1.png`) para el estilo y `libro5/d03-v1.png`. Bloque de estilo: `herramientas/style-libro6.txt`. La hoja del patio (`referencias/set-patio.png`) se usó en la portada y la primera prueba; en las páginas sin la puerta de la casa empujaba a un estilo plano, así que el lote se hizo sin ella. Correcciones: doble 3 rehecha dos veces y con mamá agregada en un recorte pegado (`d03-v2.png`); doble 8 rehecha (flores en el pliegue); mamá agregada en la doble 10 (edición); experimento rehecho (el chico estaba arrodillado arriba de los libros). Las descartadas quedan como `-v0-*`. Solo versión varón por ahora.
