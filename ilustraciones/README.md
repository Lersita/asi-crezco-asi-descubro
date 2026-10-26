# Ilustraciones

Borradores generados con inteligencia artificial (Kie.ai, modelo Nano Banana Pro, resolución 2K) el 26 de octubre de 2026. Estilo A, papel recortado.

## Cómo se hacen

1. **Referencias fijas** (`referencias/`): la hoja de personajes de Tomi y Rula. Junto con la portada (`borradores/p01-portada-v1.png`), es la referencia de estilo de todas las páginas.
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

## Versión nena: Emi (carpeta `emi/`)

Emi se hizo el 26 de octubre de 2026 editando las imágenes de Tomi del libro 1 con Nano Banana 2 y la hoja `referencias/hoja-personajes-emi.png`: piel un tono más clara, pelo castaño claro con un mechón atado con una flor coral, pestañas un poco más largas, mismo body verde.

- Doble 4: la tercera viñeta seguía siendo Tomi; se corrigió editando solo el recorte de las viñetas 2 y 3 (`d04-emi-v3.png` → `d04-emi-compuesta.png`).
- Doble 6: la edición oscureció la piel de papá; se devolvió la zona del adulto desde la versión original (`d06-emi-v2.png`).
- Doble 10: la secuencia de la izquierda se rearmó con las figuritas recortadas de la hoja de Emi (`d10-emi-compuesta.png`).
- Doble 2 (solo se ven las manos) usa la misma imagen que Tomi.

Maqueta: `maqueta/libro1_emi.py` → `libros/01-girar/libro-1-emi-borrador-ilustrado.pdf`.
