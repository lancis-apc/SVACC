Lizmap-QGIS
###########

Guía de usuario de Lizmap-QGIS
******************************

1 Introducción
**************

1.1 ¿Por qué es necesario Lizmap?
=================================

2 Organización del manual 
*************************

Este manual tiene el propósito de mostrar cómo publicar proyectos mediante el complemento de QGIS Lizmap: mediante (1) la explicación de cómo preparar un proyecto QGIS para publicarlo en la web y (2) la descripción del complemento Lizmap.

3 Preparar un proyecto QGIS para publicarlo en la Web
******************************************************

3.1 Crear un proyecto
=====================

Crear un proyecto en QGIS y agregar los datos necesarios estos pueden ser de diferente tipo, por ejemplo:
 
 - Archivos vectoriales de datos geográficos

    - ESRI Shapefilec
    - MapInfo TAB and MIF/MID
    - GeoJSON
    
 - Archivos de datos geográficos RASTER

    - GeoTIFF
    - Arc/Info ASCII Grid
    - netCDF
   
 - Bases de datos geográficas

    - PostgreSQL / PostGIS
    - MSSQL spatial
    - Oracle locator / spatial
    
Organizar y manipular las capas en la leyenda

Para organizar las capas en la leyenda se puede hacer uso de cualquiera de las siguientes instrucciones:

 - Agregar grupos dando clic derecho en la sección vacía de la leyenda y seleccionar añadir grupo 
 - Mover las capas y los grupos arrastrándolos y soltándandolos
 - Cambiar el nombre de las capas y grupos con la tecla F2 o en la ventana de propiedades de la capa
 - Manipular el orden de representación de las capas:

    - modificar el orden de las capas de la leyenda: las capas superiores se visualizan sobre las demás
    - especificar el orden de las capas desde menú Ver ‣ Paneles ‣ Orden de capas

Agregar un título al proyecto y guardarlo en formato .qgs en el directorio de trabajo.

3.2 Configurar el proyecto para la web
=======================================

Configurar el sistema de referencia de coordenadas, CRS, del proyecto:

Seleccionar el CRS del mapa web, por ejemplo:

 - EPSG:32616 - WGS 84 / UTM zone 16N - Proyectado
 - EPSG:4326 - WGS 84
 - etc

.. imagen:: /imagenes/fi_imagen1.png 

Configurar los parámetros de la Web de Servicios Geográficos (Web Map Services (WMS)) con la pestaña del servidor de QGIS (acceder a ella desde el menú Proyecto ‣ Propiedades del proyecto ‣ Servidor de QGIS):

 - Establecer el título de los servicios geograficos de la WMS
 - Agregar información como el nombre de la organización, el propietario de la publicación, el resumen, etc.
 - Establecer la extensión máxima del servicio WMS
 - Restringir la lista de CRS del servicio WMS:

    - al menos seleccionar el de la proyección utilizada en el proyecto
    - se puede usar el botón "Usado" para obtener todos los CRS de las capas y la del proyecto

 - Excluir composiciones y capas si los datos no se pueden publicar en WMS
 - Habilitar las capas que desea publicar WFS y WCS

.. imagen:: /imagenes/fi_imagen2.png 

3.3 Configurar las capas para la web
=======================================

En la ventana Propiedades de capa, la pestaña Metadatos permite configurar mucha información para los Servicios Geográficos Web:

 - Proporcionar un título, una descripción y palabras clave
 - Especificar la atribución para respetar la licencia de los datos
 - Agregar la URL del registro de metadatos si está disponible

.. imagen:: /imagenes/fi_imagen3.png 

4 Descripción del complemento Lizmap  
**************************************

4.1 Instalar el complemento Lizmap 
====================================

El complemento Lizmap está disponible a través del repositorio oficial del proyecto QGIS: http://plugins.qgis.org/plugins/lizmap/

Para instalarlo hay que seguir el mismo procedimiento de instalación que el de cualquier complemento de QGIS:

- Menú ‣ Complementos ‣ Administrar e instalar complementos 
- Buscar Lizmap
- Instalar el complemento

El complemento aparecerá en el menú y en la barra de herramientas Web 

.. imagen:: /imagenes/fi_imagen4.png  

4.2 Organización del complemento Lizmap
========================================

El complemento está organizado en 13 pestañas:

- Opciones del mapa: las opciones generales del mapa
- Capas: las opciones de cada capa
- Capas base: las capas base utilizadas en la Web
- Locate by layer: lista desplegable que da la capacidad de hacer zoom en uno o más objetos espaciales de la capa
- Tabla de atributos: las tablas de atributos de las capas agregadas
- Edición de capa: capacidades de edición para cada capa
- Capa de herramientas de ayuda: la información sobre las herramientas del mapa disponibles para el usuario
- Filtrar capa por usuario: los filtros aplicados para mostrar a los usuarios
- Visualización de datos: la creación de gráficas a partir de capas
- Gestor de tiempos: las animaciones a partir de las capas vectoriales que contengan un atributo de fecha u hora 
- Atlas: la configuración de los atributos de una capa para hacer una secuencia 
- Filter data with form: los formularios que permite buscar entre los datos de una capa 
- Log: la información de las acciones realizadas

Y tiene 4 botones de acción:

- Aceptar
- Cancelar
- Aplicar
- Ayuda

4.3 Descripción de las pestañas de Lizmap
========================================

4.3.1 Opciones del mapa
---------------------------------

La pestaña Opciones del mapa permite habilitar o deshabilitar las herramientas básicas de Lizmap, eligiendo escalas y la extensión inicial.

.. imagen:: /imagenes/fi_imagen9.png 

Opciones genéricas:

- Ocultar el proyecto en Lizmap Web Client:
 - si esta opción está marcada, el proyecto se ocultará en la página de inicio de Lizmap que muestra miniaturas de todos los directorios y proyectos de la aplicación. Se puede utilizar esta opción para ocultar el proyecto.
 - el proyecto seguirá siendo accesible para clientes WMS o WFS en función de los derechos de directorio
 - esta característica es interesante en el caso de utilizar el proyecto como un proyecto externo para otros.

Herramientas del mapa:

- Dibujar: Lizmap 3.4, habilita algunas herramientas de dibujo
- Imprimir: habilita el uso de composiciones QGIS para generar mapas en PDF
- Herramientas de medida: habilita las herramientas de medición en el mapa (longitud, área, perímetro)
- Historia de zoom: habilita los botones de navegación en el historial de zoom y moverse en el mapa
- Geolocalización automática (Automatic geolocation): habilita las funciones para utilizar la geolocalización HTML5 basada en Wifi y/o GPS
- Búsqueda de direcciones: para agregar un motor de búsqueda de direcciones que se base en uno de estos servicios:
  - Nominatim (OpenStreetMap)
  - Google
  - IGN (Géoportail)
  - BAN 

Escalas: 

- Contiene una lista de valores enteros separados por comas (y espacios en blanco opcionales), por ejemplo: 250000, 100000, 50000.
- Lizmap también usa estas escalas para restringir la visualización entre las escalas de datos mínima y máxima. Por eso es obligatorio ingresar al menos 2 escalas en la lista.

La extensión inicial del mapa:

- Contiene una lista de coordenadas en el mapa del Sistema de Coordenadas de Referencia (SCR) en el formato: xmin, ymin, xmax, ymax, estableciendo la extensión del mapa inicial
- La extensión máxima del mapa se especifica en la pestaña del servidor OWS de la ventana "Propiedades del proyecto". Los datos no se mostrarán si están fuera de la misma.
- De forma predeterminada, la extensión inicial es la máxima.

Interfaz del mapa:

- Permite ocultar el encabezado, la barra de menú, el panel de la leyenda en el inicio, la escala y/o las herramientas de navegación.

4.3.2 Capas - ajustes para cada capa   
---------------------------------------

Permite establecer parámetros para cada capa en el proyecto. Esta pestaña muestra el árbol de capas del proyecto con la misma organización que se define en el panel Capas. 
Se pueden seleccionar uno de los elementos del árbol, una capa o un grupo, y luego configurar las opciones para el grupo o capa seleccionados.

.. imagen:: /imagenes/fi_imagen10.png 

Metadatos:

- Título: se utilizará en el árbol de capas web en lugar del nombre. Para las capas, el campo "Título" está vinculado al de la pestaña del Servidor QGIS en la ventana "Propiedades de la capa".
- Resumen: permite describir la capa o grupo. Para las capas, el campo resumen está vinculado al de la pestaña del servidor QGIS en la ventana "Propiedades de la capa".
- Enlace: la URL de un documento o una página web que describa la capa o el grupo.

Leyenda:

- Conmutado (toggled): permite especificar si una capa se muestra por defecto.
- Mostrar en árbol de leyendas (display in legend tree): alterna la visibilidad de la capa en el árbol de capas; cuando está desactivado, no permite al usuario administrar su visualización.
- Ocultar imagen de leyenda (hide legend image): le permite ocultar la leyenda de la capa en la interfaz web.
- Agrupar como capa (group as layer): opción para usar en un grupo en la leyenda para mostrarlo como una sola capa.
- Capa base (base layer): establece la capa como mapa base.

Opciones del mapa: 

- Formato de imagen:
   - png: formato de imagen completo, gama completa de colores con transparencia.
   - png: modo = 16 bits: formato de imagen más claro, color del panel restringido con transparencia.
   - png: mode = 8bit: formato de imagen muy ligero, el panel de color se restringe al máximo con transparencia, posible degradación de la imagen.
   - jpeg: formato de imagen claro sin transparencia con pérdida de calidad.

- Single tile: selecciona el modo de visualización de la capa. Puede mostrarse como varias imágenes, mosaicos o una sola imagen generada por el servidor.


Si la capa la proporciona un servicio WMS y es compatible con el sistema de referencia de coordenadas del mapa web, es posible solicitar imágenes directamente al servidor WMS. 
Esto reduce la carga de QGIS-Server y optimiza Lizmap. Esta opción está disponible en el grupo de capas WMS de terceros.

Las opciones de grupo:

- Agrupar como capa:
 - transforma un grupo en una sola capa en la interfaz web
 - utilizado para agrupar capas con visibilidad dependiente de la escala
 - simplifica la interfaz a los usuarios del mapa web
 - para crear un mapa base a partir de varias capas
- Si el grupo es una capa, se le aplican otras opciones.
- Caché de cascada del servidor.

4.3.3 Capas base 
--------------------------

A menudo es útil separar las capas base como referencia y las capas temáticas en un mapa web. En Lizmap, se pueden usar grupos o capas como capas base. También es posible utilizar servicios externos en el mapa web.
Las capas base no forman parte de la leyenda y se presentan como una lista.

.. note::  Si se configura una sola capa base (capa de proyecto, servicio externo o capa base vacía), la interfaz del cliente web Lizmap no muestra el cuadro Capas base, pero la capa será visible debajo de las otras capas.

La pestaña Capas base permite agregar servicios externos como una capa base y una capa base vacía. La capa base vacía mostrará capas temáticas sobre el color de fondo del proyecto.

.. imagen:: /imagenes/fi_imagen11.png 

** Capas base disponibles**

 - OpenStreetMap, proyecto de mapeo bajo licencias libres y abiertas:

    - OSM Mapnik: servicio disponible en openstreetmap.org
    - OSM Mapquest: servicio proporcionado por la empresa Mapquest
    - Cycle Map: mapa de promoción de datos de ciclismo de OpenStreetMap, incluida información de altitud

 - Google, requiere licencia:

    - Streets: la capa de fondo predeterminada de Google Maps
    - Satellite: el mapa de fondo que incorpora imágenes aéreas y de satélite
    - Hybrid: el mapa de fondo que mezcla calles y satélite
    - Terrain

 - Bing Map, requiere el cumplimiento del contrato de licencia de Microsoft y por lo tanto una clave:

    - Streets: la capa de fondo predeterminada de Bing Map
    - Satellite: el mapa de fondo que incorpora imágenes aéreas y de satélite
    - Hybrid: el mapa de fondo que mezcla calles y satélite

 - IGN Géoportail, requiere el cumplimiento del contrato de licencia IGN y por lo tanto una clave:

    - Plan: la representación de IGN para la Web
    - Satellite: el mapa de fondo que incorpora imágenes aéreas y de satélite del IGN
    - Scan: el mapa de fondo que mezcla los diversos escaneos IGN

.. note:: Si elige una capa base externa, el mapa se mostrará en Google Mercator (EPSG: 3857 o EPSG: 900913), las escalas son las de los servicios externos y QGIS-Server realizará una reproyección al vuelo.
Por lo tanto, es necesario preparar el proyecto QGIS en consecuencia.

4.3.4 Locate by layer
--------------------------

Esta herramienta permite presentar al usuario web de Lizmap una lista desplegable que le de la capacidad de hacer zoom en uno o más objetos espaciales de la capa.

**Ejemplo de uso**

Una capa vectorial de municipios contenidos en el proyecto QGIS. Al agregar estos municipios en la herramienta "Locate by layer", permite que los usuarios de Lizmap Web Client se ubiquen rápidamente en uno de los municipios.
Una vez que esta capa se agregó a la herramienta "Locate by layer", aparece una lista desplegable de los municipios en la interfaz web de Lizmap.
Cuando el usuario del mapa web seleccione un nombre en esta lista, el mapa se reenfocará automáticamente en el municipio seleccionado y se mostrará la geometría del municipio (opcional).

**Prerrequisitos**

La capa debe publicarse como WFS y la clave principal también debe publicarse en la pestaña "Layer properties".

**Configurando la herramienta**

.. imagen:: /imagenes/fi_imagen12.png 

Para agregar una capa a esta herramienta:

 1. Haga clic en el botón |boton_maslz|.
 2. Elija la capa de la lista de capas vectoriales del proyecto.
 3. Elija la columna que contiene la etiqueta que desea mostrar en la lista desplegable.
 4. Si desea agregar un filtro previo a sus datos, use el campo "Optional group by".
 5. Si desea que la geometría de los objetos relacionados también se muestre en el mapa cuando el usuario selecciona un elemento de la lista, marque la opción "Mostrar geometría".
 6. Si establece un valor superior a 0, el autocompletado se utilizará después de esta cantidad de caracteres mientras el usuario escribe. El cuadro combinado clásico será reemplazado por una entrada de texto editable.
 7. Si Lizmap debe activar el filtro en la capa. Solo la característica seleccionada será visible en el mapa.

- Para editar una capa en la tabla, selecciónela y haga clic en el botón |boton_editar| o haga doble clic en la fila.
- Para eliminar una capa de la tabla, selecciónela y haga clic en el botón |boton_menoslz|.
- Para mover una capa hacia arriba o hacia abajo, selecciónela y haga clic en los botones |boton_arriba| o |boton_abajo|. El orden también cambiará en Lizmap.

**Listas jerárquicas**

Si tomamos el ejemplo de los municipios, puede ser interesante proporcionar también al usuario un menú desplegable de localidades. 
De esta manera, cuando el usuario elige un municipio, el menú desplegable de localidades se filtra automáticamente para mostrar solo las localidades del municipio elegido.

Para ello, existen 2 métodos: 
 - tener 2 capas vectoriales separadas: una para municipios y otra para localidades. Por lo tanto, debe usar una combinación de campo entre las dos capas para habilitar las listas de filtrado automático en Lizmap
 - tener solo 1 capa para localidades, y luego especificar con el complemento un campo del grupo. Se crearán dos menús desplegables en lugar de uno en la aplicación web

4.3.5 Tabla de atributos
--------------------------
Lizmap está diseñado para mostrar datos espaciales en el mapa principal, y puede proponer a los usuarios que vean los datos de un objeto a través de la función "emergente" (una pequeña ventana emergente que contiene los datos de los objetos y que se muestra cada vez que el usuario hace clic en el mapa).
A veces esto no es suficiente y, como editor de mapas, le gustaría que el usuario vea todos los datos de una capa específica, como puede hacer en QGIS abriendo la tabla de atributos.

**Prerrequisitos**
La capa debe publicarse como WFS y la clave principal también debe publicarse en las propiedades de la capa.

**Configurando la herramienta**

.. imagen:: /imagenes/fi_imagen13.png 

Para agregar una capa a esta herramienta:

1. Haga clic en el botón |boton_maslz|.
2. Capa: elija una de las capas vectoriales (espacial o no). Puede ser cualquier formato de capa vectorial: GeoJSON, Shapefile, PostGIS, CSV, etc.
3. Primary key: la herramienta de la tabla de atributos debe poder definir cada característica como única. Agregue un campo de este tipo si la capa aún no lo tiene. Normalmente, el campo de ID único contiene números enteros. Si la capa no tiene este tipo de campo, puede crearla fácilmente con la calculadora de campo. 
4. Campos para ocultar: en la pestaña "Campos a ocultar" marcar las casillas para ocultar los campos. Los campos ocultos no serán visibles para el usuario final, pero seguirán estando disponibles para Lizmap Web. Utilizar esta opción para ocultar el campo ID único.

**Orden de campos**
Lizmap utiliza el orden de los campos definidos en la tabla de atributos, para editarlos:

1. Abrir la tabla de atributos de la capa.
2. Hacer clic derecho en el encabezado de una columna.
3. Hacer clic en organizar columnas.
4. Arrastrar y soltar columnas.

4.3.6 Edición de capa
--------------------------

Es posible permitir a los usuarios editar datos espaciales y de atributos desde la interfaz web de Lizmap para las capas PostgreSQL o Spatialite del proyecto QGIS. El complemento Lizmap permite agregar una o más capas y elegir qué acciones para cada una serán posibles en la interfaz web:

- crear elementos
- modificar atributos
- modificar la geometría
- eliminar elementos

El formulario web presentado al usuario para completar la tabla de atributos admite las herramientas de edición disponibles en la pestaña de campos de las propiedades de la capa vectorial de QGIS. Se puede configurar un menú desplegable, ocultar una columna, hacerla no editable, usar una casilla de verificación, un área de texto, etc. Toda la configuración se realiza con el ratón, en QGIS y en el complemento Lizmap.

Además, Lizmap Web Client detecta automáticamente el tipo de columna (entero, real, cadena, etc.) y agrega las comprobaciones y controles necesarios en los campos.

**Prerrequisitos**

Para permitir la edición de datos en Lizmap Web Client, debe:

- Tener una capa vectorial con PostGIS o Spatialite.
- Configurar la herramienta de edición para la capa en "Propiedades de capa" ‣ "Formulario de atributos". Esto no es obligatorio pero se recomienda para controlar los datos ingresados ​​por los usuarios.
- La capa debe publicarse como WFS y la clave principal también debe publicarse en las propiedades de la capa.
- A pesar de que queremos editar la capa, no es necesario usar las casillas de verificación Actualizar, Insertar y Eliminar en la tabla WFS en la pestaña Servidor QGIS. Lizmap no utiliza WFS-T. Lizmap hará la edición directamente en la fuente de datos. La configuración se realiza únicamente en el panel que se describe a continuación.

.. note::  Tenga cuidado si su capa contiene algunos valores Z o M, desafortunadamente Lizmap los establecerá en "0", que es el valor predeterminado al guardar en la base de datos.

**Configurando la herramienta**

Estos son los pasos detallados:

- Si es necesario, crear una capa en la base de datos con el tipo de geometría deseada (punto, línea, polígono, etc.)
 - agregar una clave primaria
 - esta columna de la clave primaria debe incrementarse automáticamente. Por ejemplo, serial a PostgreSQL.
 - agregar un índice espacial: esto es importante para el rendimiento.
 - crear tantos campos como sea necesario para los atributos: si es posible, usar nombres de campos simples.

.. imagen:: /imagenes/fi_imagen14.png 

- Para habilitar una capa con capacidades de edición:

1. Hacer clic en el botón |boton_maslz|
2. Seleccionar la capa en la lista desplegable
3. Marcar las acciones que se desean activar:
 - Crear
 - Editar atributos (Edit attributes)
 - Editar geometría (Edit geometry)
 - Borrar
4. Opcional, se puede agregar una lista de grupos que se pueden editar, separados por una coma.
5. El ajuste se puede activar al seleccionar al menos una capa en la lista de capas.
 - La capa debe publicarse como WFS y la clave principal también debe publicarse en las propiedades de la capa.
6. Si se selecciona una capa superior, se debe usar al menos una casilla de verificación:
 - Vértices
 - Segmentos
 - Intersecciones
7. Es posible establecer la tolerancia para la edición.

4.3.7 Capas de herramientas de ayuda
-------------------------------------

Permite que el usuario active la información sobre herramientas del mapa al desplazarse por las entidades eligiendo una lista de campos para mostrar.

**Prerrequisitos**

La capa debe publicarse como WFS y la clave principal también debe publicarse en las propiedades de la capa.

**Configurando la herramienta**

.. imagen:: /imagenes/fi_imagen15.png 

Para configurar una herramienta de ayuda en una capa:

1. Hacer clic en el botón |boton_maslz|.
2. Eligir la capa.
3. Seleccionar algunos campos para mostrar en la información sobre herramientas.
4. Elegir mostrar la geometría (opcional).
5. Si se muestra la geometría, se puede establecer el color.

4.3.8 Filtrar capa por usuario
-------------------------------------

Por lo general, la gestión de los derechos de acceso de los proyectos a Lizmap se realiza mediante un directorio. La configuración se realiza en este caso en la interfaz de administración del cliente web de Lizmap. Esto ocultará completamente algunos proyectos basados ​​en grupos de usuarios, pero requiere un directorio y administración de proyectos.

En cambio, la función de filtrado que se presenta aquí permite publicar un solo proyecto QGIS y filtrar los datos que se muestran en el mapa según el usuario que inició sesión. Es posible filtrar solo capas vectoriales porque Lizmap usa una columna en la tabla de atributos.

Actualmente, el filtrado utiliza el ID del grupo de usuarios conectado a la aplicación web. Está activo para todas las solicitudes al servidor QGIS y, por lo tanto, se ocupa de:

 - las imágenes de capas vectoriales que se muestran en el mapa
 - las ventanas emergentes
 - las listas de entidades Localizar por capa 
 - listas desplegables de formularios de edición de relación de valor
 - próximas funciones (la visualización de la tabla de atributos, funciones de búsqueda, etc.)

**Configurando la herramienta**
Para utilizar la herramienta de filtrado de datos en Lizmap Web:
 - usar QGIS 2 en el servidor
 - tener acceso a la interfaz de administración de Lizmap Web Client

.. imagen:: /imagenes/fi_imagen16.png 

4.3.9 Visualización de datos 
-------------------------------------

Con el panel de visualización de datos, es posible crear algunos tipos de gráficos con solo unos pocos clics:

 - dispersión
 - circular/pastel
 - histograma
 - caja
 - barras
 - histograma en 2D
 - polar

**Configurando la herramienta**

La configuración se hace desde el plugin Lizmap en QGIS en el panel  Visualización de datos.

.. imagen:: /imagenes/fi_imagen17.png 

Para habilitar una capa con capacidades de visualización de datos:

 1. Hacer clic en el botón |boton_maslz|.
 2. Seleccionar el tipo de gráfico para agregar. Según la elección, el formulario se adaptará por sí solo.
 3. Título: aquí se puede escribir el título que se desea para el gráfico.
 4. Descripción: la descripción del gráfico. Puede incluir HTML.
 5. Seleccionar la capa en la lista desplegable.
 6. Campo X: el eje X del gráfico. Puede que esté vacío para algunos tipos.
 7. Aggregation: para algunos tipos de gráficos, como de barras o circulares, se puede optar por agregar los datos en el gráfico. Hay algunas funciones agregadas disponibles: promedio (avg), suma, recuento, mediana, desv. estándar, mínimo, máximo, etc.
 8. Campo Y: el eje Y del gráfico. 
 9. Color: Dependiendo del tipo de gráfico, puede agregar uno o varios colores.
 10. Mostrar solo el elemento emergente secundario: el gráfico principal no se mostrará en el contenedor principal y solo el gráfico filtrado de la relación de la capa se mostrará en el elemento emergente cuando seleccione el elemento.
 11. Algunas opciones pueden estar visibles o no según el tipo de gráfico, como elegir el diseño horizontal / vertical para un gráfico de barras.

4.3.10 Gestor de tiempos
-------------------------------------

Esta herramienta permite crear animaciones de vectores, siempre que se tenga al menos una capa con una columna con una fecha/hora válida.

**Configurando la herramienta**
Después de la configuración, la aplicación web mostrará el símbolo de un reloj; al hacer clic en él, se abrirá un pequeño panel que permitirá moverse entre los pasos o reproducir toda la animación. Al inicio, la aplicación cargará la tabla completa, por lo que si tiene miles de objetos, es posible que deba esperar varios segundos antes de que la aplicación esté disponible.

.. imagen:: /imagenes/fi_imagen18.png 

Para configurar el gestor de tiempo con una capa:

 1. Hacer clic en el botón |boton_maslz|
 2. Seleccionar una capa que contenga en su tabla de atributos fecha / hora.
 3. Seleccionar la columna de inicio con fecha / hora. 
 4. Seleccionar la columna final con fecha / hora. Esto es opcional.
 5. Establecer la resolución de fecha / hora de los atributos elegidos.

También se puede elegir:
 - el tamaño del marco de tiempo
 - el tipo de marco
 - la longitud del cuadro de animación

4.3.11 Atlas
-------------------------------------
Esta función permite elegir y configurar una capa para hacer una secuencia de entidades en el proyecto Lizmap.

Desde Lizmap 3.4:

Se pueden configurar muchas capas en esta herramienta. Si la casilla de verificación Reproducción automática está marcada, se utiliza la primera capa de la lista.

.. imagen:: /imagenes/fi_imagen19.png 

Para configurar una capa de atlas:

 1. Hacer clic en el botón |boton_maslz|
 2. Elegir la capa que se quiere agregar al atlas
 3. Seleccionar el campo de clave principal, debe ser un número entero
 4. Comprobar si desea mostrar la descripción de la capa en el atlas
 5. Elegir el campo que contiene el nombre de sus características, se mostrará en lugar de la clave principal en la lista de características, el atlas se ordenará de acuerdo con este campo
 6. Se puede elegir resaltar la función seleccionada por el atlas, cambiará cada vez que cambie a una nueva función
 7. Eligir entre un zoom en la función o convertirlo en el centro del mapa
 8. Verificar si se desea activar el filtro en la característica seleccionada por el atlas, esto ocultará todas las demás características de la capa y solo mostrará la seleccionada

También se puede elegir:
 - abrir la herramienta atlas cuando se abra el proyecto
 - iniciar el modo de reproducción automática cuando abra el proyecto

4.3.12 Filter data with form
-------------------------------------

Esta herramienta muestra un formulario en el panel izquierdo, basado en algunos campos, y permite a los usuarios buscar entre los datos de la capa con una variedad de entradas de formulario: cuadros combinados, casillas de verificación, entradas de texto con autocompletado, selector de fecha con deslizadores entre un mínimo y un máximo de fechas, etc.

Usando declaraciones SQL, Lizmap consultará los datos para recuperar:

 - el recuento total de funciones para el filtro actual
 - los valores únicos de algunos campos (para el tipo de valores únicos, por ejemplo)
 - el mínimo y máximo de los campos numéricos o de fecha
 - la extensión de los datos para el filtro actual

**Configurando la herramienta**

.. imagen:: /imagenes/fi_imagen20.png 

La pestaña permite configurar las entradas de filtro en función de los campos de la capa. Puede agregar uno o más campos para una o más capas. Si agrega campos de 2 o más capas diferentes, Lizmap Web Client mostrará un cuadro combinado para permitir al usuario elegir la capa para filtrar. Seleccionar una capa actualizará el formulario y desactivará el filtro actual.

Se debe agregar una línea en la tabla de complementos para cada campo que necesite agregar en el formulario de filtro. Para cada campo, debe configurar algunas opciones:

 1. Hacer clic en el botón |boton_maslz|
 2. Capa: la capa de origen
 3. Título: el título que se le dará a la entrada, que se mostrará encima de la entrada del formulario. Por ejemplo, "Elija una categoría"
 4. Tipo: el tipo de entrada del formulario, entre uno de los siguientes: Texto, Valores únicos, Fecha, Numérico.
 5. Campo: el nombre del campo (en la tabla de atributos). Solo para los tipos Texto, Valores únicos y Numérico.
 6. Fecha mínima: el campo que contiene la fecha de inicio del objeto (por ejemplo: "fecha_inicio" de un evento). Esto solo es necesario para el tipo de fecha.
 7. Fecha máxima: el campo que contiene la fecha de finalización de los datos. Si tiene 2 campos que contienen fechas, uno para la fecha de inicio y otro para la fecha de finalización, puede diferenciarlos. De lo contrario, debe utilizar el mismo nombre de campo para la fecha mínima y la fecha máxima.
 8. Formato: el formato del tipo de valores únicos. Mostrará un cuadro combinado, o casillas de verificación que mostrarán una casilla de verificación para cada valor distinto. Los distintos valores son consultados dinámicamente por Lizmap Web Client.
 9. Divisor: solo para el tipo de valores únicos. Usarlo si se desea dividir los valores de campo por un separador. Ej: cultura, medio ambiente se pueden dividir en cultura y medio ambiente con el separador `,`.


6	Referencias
**************************************

- Lizmap 3.2. Publisher guide. (2014). Lizmap Documentation. https://docs.lizmap.com/current/es/publish/index.html
- Lizmap 3.4. Lizmap QGIS plugin. (2014). Lizmap Documentation. https://docs.lizmap.com/next/en/publish/lizmap_plugin/index.html

.. |boton_maslz| image:: /imagenes/boton_maslz.png            
            :height: 25px
            :width: 25px

.. |boton_editar| image:: /imagenes/boton_editar.png            
            :height: 25px
            :width: 25px

.. |boton_menoslz| image:: /imagenes/boton_menoslz.png            
            :height: 25px
            :width: 25px
            
.. |boton_arriba| image:: /imagenes/boton_arriba.png            
            :height: 25px
            :width: 25px

.. |boton_abajo| image:: /imagenes/boton_abajo.png            
            :height: 25px
            :width: 25px