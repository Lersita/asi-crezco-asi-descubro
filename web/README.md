# Web de la colección

Página de un solo archivo (`index.html`) con un personalizador: elegís mujer o varón, escribís el nombre, hojeás el libro 1 y descargás el PDF personalizado. El PDF se arma **en el navegador** (con `pdf-lib`), así que no hace falta servidor ni base de datos.

## Cómo se arma el PDF

1. `plantillas/<libro>-<genero>/dNN.jpg`: una imagen por doble, sacada de la maqueta (`maqueta/*.html`) sin el título de tapa ni el texto con el nombre. `medidas.json` guarda dónde iban esos dos textos.
2. `js/libro-pdf.js` toma esas imágenes, escribe el título y la etiqueta con el nombre (tipografías en `fuentes/`) y arma 24 páginas cuadradas de 21,6 cm.

Cuando cambian las ilustraciones o el texto de un libro: regenerá la maqueta (`maqueta/libro1.py`, `libro1_emi.py`, `libro2.py`) y después las plantillas con `node web/herramientas/plantillas.js` (desde la raíz del repositorio).

Libros disponibles hoy: libro 1 (mujer y varón) y libro 2 (solo varón).

## Publicar en Vercel

1. En vercel.com: **Add New → Project → Import** el repositorio `Lersita/asi-crezco-asi-descubro`. Si no aparece, dale acceso a la aplicación de Vercel en GitHub para ese repositorio.
2. **Root Directory:** `web`. **Framework Preset:** Other. Sin comando de build.
3. **Deploy.** Cada vez que se guarda un cambio en `main`, Vercel publica solo.

## Versión para Claude (Artifact)

`python3 web/herramientas/artifact.py` genera `_artifact.html`: la misma página sin la envoltura del documento y sin la descarga (dentro del Artifact no se pueden bajar archivos).
