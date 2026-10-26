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

| Página | Archivo |
| --- | --- |
| 1 Portada | `p01-portada-v1.png` |
| 2–3 | `d01-v2.png` |
| 4–5 | `d02-v2.png` |
| 6–7 | `d03-v2.png` |
| 8–9 | `d04-v1-compuesta.png` |
| 10–11 | `d05-v1.png` |
| 12–13 | `d06-v1.png` |
| 14–15 | `d07-v1.png` |
| 16–17 | `d08-v1.png` |
| 18–19 | `d09-v1.png` |
| 20–21 | `d10-v2-compuesta.png` |
| 22–23 | `exp-v1.png` |
| 24 | `p24-cuna-v1.png` |

## Pendiente para la versión final

- Subir a 4K o ampliar las imágenes elegidas: para imprimir a 300 puntos por pulgada, una doble necesita unos 5.100 píxeles de ancho.
- Revisar el pliegue en cada doble con la imprenta o con la plantilla de Amazon KDP.

## Maqueta

`maqueta/libro1.py` arma el HTML y `maqueta/pdf.js` lo pasa a PDF (`libros/01-girar/libro-1-borrador-ilustrado.pdf`). Usa las imágenes comprimidas de `maqueta/img/`.
