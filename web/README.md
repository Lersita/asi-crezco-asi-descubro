# Web de la colección

Página de un solo archivo (`index.html`) con un personalizador: elegís mujer o varón, escribís el nombre y hojeás el libro 1, 2 o 3 (desde la quinta doble, la vista previa se ve borrosa).

**Venta:** el cliente elige los libros, paga con Mercado Pago (Checkout Pro) y descarga el PDF en `gracias.html`. Los precios están en `precios.json`, que usan la web (para mostrarlos) y el servidor (para cobrar).

## Funciones del servidor (`api/`)

- `crear-pago.js`: valida el pedido, toma el precio de `precios.json` y crea la preferencia en Mercado Pago. El pedido (libros, versión, nombre y una clave al azar) viaja en `external_reference`, así que no hace falta base de datos.
- `pedido.js`: le pregunta a Mercado Pago cómo está el pago y confirma que la clave coincide.
- `descargar.js`: si el pago está aprobado, arma el PDF con `_pdf.js` y lo entrega.
- Variable de entorno en Vercel: `MP_ACCESS_TOKEN` (credencial de prueba o de producción de Mercado Pago).

`privado/` (plantillas nítidas y tipografías) solo lo lee el servidor; la dirección `/privado/...` redirige al inicio.

## Cómo se arma el PDF

1. `privado/plantillas/<libro>-<genero>/dNN.jpg`: una imagen por doble, sacada de la maqueta (`maqueta/*.html`) sin el título de tapa ni el texto con el nombre. `medidas.json` guarda dónde iban esos dos textos.
2. `api/_pdf.js` toma esas imágenes, escribe el título y la etiqueta con el nombre (tipografías en `privado/fuentes/`) y arma 24 páginas cuadradas de 21,6 cm.

Cuando cambian las ilustraciones o el texto de un libro: regenerá la maqueta (`maqueta/libro1.py`, `libro1_emi.py`, `libro2.py`) y después las plantillas y las vistas previas con `node web/herramientas/plantillas.js` y `python3 web/herramientas/vista.py` (desde la raíz del repositorio).

Libros disponibles hoy: libros 1, 2 y 3, en mujer y varón. Se eligen tildando los libros; el precio depende de cuántos (1, 2 o 3).

## Publicar en Vercel

1. En vercel.com: **Add New → Project → Import** el repositorio `Lersita/asi-crezco-asi-descubro`. Si no aparece, dale acceso a la aplicación de Vercel en GitHub para ese repositorio.
2. **Root Directory:** `web`. **Framework Preset:** Other. Sin comando de build.
3. **Deploy.** Cada vez que se guarda un cambio en `main`, Vercel publica solo.

## Versión para Claude (Artifact)

`python3 web/herramientas/artifact.py` genera `_artifact.html`: la misma página sin la envoltura del documento y sin la descarga (dentro del Artifact no se pueden bajar archivos).
