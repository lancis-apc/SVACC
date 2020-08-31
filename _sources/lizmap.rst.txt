Lizmap-QGIS
###############

Guía de usuario de Lizmap-QGIS
################################

1 Introducción
***************
1.1 ¿Por qué es necesario Lizmap?
================================

2 Organización del manual 
*************************

Este manual tiene el propósito de mostrar como publicar proyectos mediante el complemento de QGIS: Lizmap, mediante (1) la explicación de como preparar un proyecto QGIS para publicarlo en la web, (2) como configurar un proyecto para Lizmap y (3) una explicación de las funciones avanzadas.

3 Preparar un proyecto QGIS para publicarlo en la Web
******************************************************

3.1 Crear un proyecto
======================

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
 - Mover las capas y los grupos arrastrandolos y soltandandolos
 - Cambiar el nombre de las capas y grupos con la tecla F2 o en la ventana de propiedades de la capa
 - Manipular el orden de representación de las capas:

    - modificar el orden de las capas de la leyenda: las capas superiores se visualizan sobre las demás
    - especificar el orden de las capas desde menú Ver> Paneles> Orden de capas

Agregar un título al proyecto y guardarlo en formato .qgs en el directorio de trabajo.

3.2 Configurar el proyecto para la web
=======================================

Configurar el sistema de referencia de coordenadas, CRS, del proyecto:

Seleccionar el CRS del mapa web, por ejemplo:

 - EPSG: 3857 para Google Mercator
 - EPSG: 2154 para Lambert 93
 - etc

Configurar los parámetros de la Web de Servicios Geográficos (Web Map Services (WMS)) con la pestaña del servidor de QGIS (acceder a ella desde el menú Proyecto ‣ Propiedades del proyecto ‣ Servidor de QGIS):

 - Establecer el título de los servicios geograficos de la WMS
 - Agregar información como el nombre de la organización, el propietario de la publicación, el resumen, etc.
 - Establecer la extensión máxima del servicio WMS
 - Restringir la lista de CRS del servicio WMS:

    - al menos seleccione el de la proyección utilizada en el proyecto
    - puede usar el botón "Usado" para obtener todos los CRS de las capas y la del proyecto

 - Excluir composiciones y capas si los datos no se pueden publicar en WMS
 - Habilitar las capas que desea publicar WFS y WCS

3.3 Configurar las capas para la web
=======================================

En la ventana Propiedades de capa, la pestaña Metadatos permite configurar mucha información para los Servicios Geográficos Web:

 - Proporcionar un título, una descripción y palabras clave
 - Especificar la atribución para respetar la licencia de los datos
 - Agregar la URL del registro de metadatos si está disponible


4 Configurar el proyecto para Lizmap
**************************************

4.1 Instalar el complemento Lizmap 
====================================

El complemento Lizmap está disponible a través del repositorio oficial del proyecto QGIS: http://plugins.qgis.org/plugins/lizmap/
Para instalarlo seguir el mismo procedimiento de instalación que el de cualquier complemento de QGIS:

- Menú ‣ Complementos ‣ Administrar e instalar complementos 
- Buscar Lizmap
- Instalar el complemento

El complemento aparecerá en el menú y en la barra de herramientas Web 

4.2 Organización del complemento Lizmap
========================================

El complemento está organizado en 13 pestañas:

- Map options: las opciones generales del mapa
- Layers: las opciones de cada capa
- Baselayers: las capas base utilizadas en la Web
- Locate by layer: 
- Attribute table: las tablas de atributos de las capas agregadas
- Layer editing: 
- Tooltip layers: 
- Filter layer by user:
- Dataviz:
- Time manager:
- Atlas:
- Filter data with form:
- Log: muestra información de las acciones realizadas

Y tiene 4 botones de acción:

- Aceptar
- Cancelar
- Aplicar
- Ayuda

4.3 Configurar las capas y los grupos
========================================

La configuración de la capas se realiza en la pestaña Layers
Esta pestaña muestra el árbol de capas del proyecto con la misma organización que se define en el panel Capas. Puede seleccionar uno de los elementos del árbol, una capa o grupo, y luego configurar las opciones para el grupo o capa seleccionados.

Información sobre grupos y capas:

- Título: se utilizará en el árbol de capas web en lugar del nombre. Para las capas, el campo de título está vinculado al de la pestaña Metadatos en la ventana de propiedades de la capa.
- Resumen: permite describir la capa o grupo. Para las capas, el campo resumen está vinculado al de la pestaña Metadatos en la ventana de propiedades de la capa.
- Enlace: la dirección web de un documento o una página web que describe la capa o el grupo. Aparece un icono (i) en la leyenda si se ha enviado el enlace.

Opciones de capas:

- Toggled: permite especificar si una capa se muestra por defecto
- Activate popup: habilita ventanas emergentes de información sobre el mapa haciendo clic 
- Hide legend image: permite ocultar la leyenda de la capa en la interfaz web
- Display in legend tree: alterna la visibilidad de la capa en el árbol de capas; cuando está desactivado, no permite al usuario administrar su visualización
- Base layer: establece la capa como mapa base. Esto será accesible a través de la lista de mapa base
- Single Tile: selecciona el modo de visualización de la capa. Puede mostrarse como varias imágenes, mosaicos o una sola imagen generada por el servidor
- Image format:

  - png: formato de imagen completo, gama completa de colores con transparencia
  - png; modo = 16 bits: formato de imagen más claro, color del panel restringido con transparencia
  - png; mode = 8bit: formato de imagen muy ligero, el panel de color se restringe al máximo con transparencia, posible degradación de la imagen
  - jpeg: formato de imagen claro sin transparencia con pérdida de calidad

Si la capa la proporciona un servicio WMS y es compatible con el sistema de referencia de coordenadas del mapa web, es posible solicitar imágenes directamente al servidor WMS. Esto reduce la carga de QGIS-Server y optimiza Lizmap. Esta opción está disponible en el grupo de capas WMS de terceros.

Opciones de grupo:

 - Agrupar como capa:

    - transforma un grupo en una sola capa en la interfaz web
    - utilizado para agrupar capas con visibilidad dependiente de la escala
    - simplifica la interfaz a los usuarios del mapa web
    - para crear un mapa base a partir de varias capas
 
 - si el grupo es una capa, se le aplican otras opciones

4.4 Configurar el mapa
========================================

La pestaña Mapa le permite habilitar o deshabilitar las herramientas básicas de Lizmap, eligiendo escalas y la extensión inicial.

Las opciones genéricas (generic options):

  - ocultar el proyecto en Lizmap Web Client:

    - si esta opción está habilitada, el proyecto se ocultará en la página de inicio de Lizmap que muestra miniaturas de todos los directorios y proyectos de la aplicación. Puede utilizar esta opción para ocultar el proyecto.
    - el proyecto seguirá siendo accesible para clientes WMS o WFS en función de los derechos de directorio
    - esta característica es interesante en el caso de utilizar este proyecto como un proyecto externo para otros.

Las herramientas de mapa (map tools):
 
 - Print: permite el uso de composiciones QGIS para mapas de generación de PDF
 - Measure tools: habilita las herramientas de medición en el mapa (longitud, área, perímetro)
 - Zoom history: habilita los botones de navegación en el historial de zoom y moverse en el mapa
 - Automatic geolocation: habilita las funciones para utilizar la geolocalización HTML5 basada en Wifi y / o GPS
 - Adress search: para agregar un motor de búsqueda de direcciones que se base en uno de estos servicios:

    - Nominatim (OpenStreetMap)
    - Google
    - Ban
    - Ign

Las escalas (scales):

 - una lista de valores enteros separados por comas (y espacios en blanco opcionales), por ejemplo: 250000, 100000, 50000.
 - Lizmap también usa estas escalas para restringir la visualización entre las escalas de datos mínima y máxima. Por eso es obligatorio ingresar al menos 2 escalas en la lista.

La extensión del mapa inicial (inicial map extent)

 - una lista de coordenadas del mapa en el Sistema de Coordenadas de referencia en el formato: xmin, ymin, xmax, ymax, estableciendo la extensión del mapa inicial
 - la extensión máxima del mapa está especificada en la pestaña del servidor OWS de la ventana Propiedades del proyecto. Los datos no se mostrarán si están fuera de él
 - de forma predeterminada, la extensión inicial es la máxima.

4.5 Configurar las capas base
========================================

A menudo es útil separar las capas base como referencia y las capas temáticas en un mapa web. En Lizmap, se pueden usar grupos o capas como capas base. También es posible utilizar servicios externos en el mapa web.
Las capas base no forman parte de la leyenda y se presentan como una lista.

.. note::  
   
   Si se configura una sola capa base (capa de proyecto, servicio externo o capa base vacía), la interfaz del cliente web Lizmap no muestra el cuadro Capas base, pero la capa será visible debajo de las otras capas.

La pestaña Baselayers permite agregar servicios externos como capa base y una capa base vacía. La capa base vacía mostrará capas temáticas sobre el color de fondo del proyecto.

4.5.1 Las capas base disponibles
---------------------------------

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

.. note:: 

   Si elige una capa base externa, el mapa se mostrará en Google Mercator (EPSG: 3857 o EPSG: 900913), las escalas son las de los servicios externos y QGIS-Server realizará una reproyección al vuelo.
   Por lo tanto, es necesario preparar el proyecto QGIS en consecuencia.

5 Publicar el mapa por FTP Server
**************************************

Lizmap se basa en el sistema de repositorios. Para publicar un mapa en Lizmap, es suficiente con asegurarse de que el contenido del directorio local que contiene los datos y los proyectos QGIS se reproduzca exactamente idéntico en el repositorio del servidor correspondiente.
Para ello, es necesario sincronizar el directorio local con el del servidor cada vez que actualice el proyecto QGIS, modifique la configuración de Lizmap con el complemento o agregue archivos en el directorio local.

.. note:: 

   Si está trabajando localmente, dado que Lizmap Web Client está instalado en la misma máquina que usa para QGIS, no necesita sincronizar sus archivos con FTP. Esta configuración solo debe existir para realizar pruebas.

.. note:: 

   Puede utilizar cualquier herramienta y protocolo de sincronización (FTP, FTPS, SFTP, rsync, unison, etc.).

6 Utilizar un FTP para clientes
**************************************

FTP permite acceder a archivos desde un servidor, recuperarlos y agregar documentos y/o carpetas. Por lo tanto, se puede utilizar para sincronizar el directorio local con el del servidor donde se encuentra Lizmap Web Client. Este protocolo es un estándar web que puede explotarse a través de muchos clientes FTP.
Puede utilizar alguna de las siguientes extensiones o alguna que utilice habitualmente:

  - FireFTP: complemento de Firefox
  - Filezilla: software multiplataforma gratuito (Windows, MacOS, Linux)
  - WinSCP: software gratuito para Windows

 Puede utilizar estas herramientas para realizar cambios manuales en el directorio remoto:
  - hacer una copia de seguridad
  - eliminar contenido
  - sobrescribir archivos manualmente: proyecto QGIS (.qgs) y configuración de Lizmap (.qgs.cfg).


7	Referencias
**************************************

- Lizmap 3.2. Publisher guide. (2014). Lizmap Documentation. https://docs.lizmap.com/current/es/publish/index.html