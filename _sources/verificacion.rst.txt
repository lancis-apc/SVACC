Verificación de capas
#############################


Los puntos a verificar son los siguientes:


1. Proyección.  Existe el archivo prj asociado 
2. Geometría completa.  La capa contiene el mismo número de elementos geométricos y datos tabulares en la tabla de atributos
3. Sobrelapamiento. La capa no cuenta con errores topológicos
4. Nulos. No existen campos vacios en la tabla de atributos
5. Codificación*. No existen campos con carácteres especiales o extraños en su contenido o datos numéricos esten declardos como texto
6. Metadatos. Existe el archivo xml asociado a los metadatos geográficos 


.. Note::

    La códificación se basa en la revisión de elementos con UTF-8, si la capa cuenta con otro tipo de codificación y contiene carácteres especiales
    el módulo de códificación reconocerá carácteres extraños en el contenido. dandole un puntaje de 0 en este rubro.


Descargar el código de ejemplo 

:download:`verificacion_layers.py <../../codigos/verificacion_layers.py>`.


Requerimientos generales 
--------------------------



Ejemplo:
---------

1. Abrir el código 
********************

Abrir el código **verificación_layers.py** en Qgis 3.4 o superior, 
para resolver cualquier duda al respecto, consultar la guia_

.. _guia: https://vichdzgeo.github.io/geo_lancis/ejecucion.html

.. image:: ../../verificacion/images/codigo.PNG

2. Indicar el directorio
***************************


El código verifica todas las capas vectoriales contenidas en el directorio
indicado en la variable **path_dir**

.. code-block:: python

    path_dir = "C:/Dropbox (LANCIS)/SIG/insumos/agricultura/conabio/vector/produccion_miel/"


Salidas
********

Capas de topología
^^^^^^^^^^^^^^^^^^^^


el código crea una carpeta llamada **temp**, dentro de ella otra carpeta llamada **topologia** en esta 
carpeta se guardan los 3 archivos shapefile  resultantes de la función **topologia**

estan nombrados de la siguiente manera:

**nombrecapa_error**.shp 

Capa de puntos que índica la posición en donde 2 o más poligonos no colindan adecuadamente
o que su geometría puede causar problemas en algún análisis espacial

**nombrecapa_invalido**.shp

Capa de poligonos que índica geométria inválida de la capa 

**nombrecapa_valido**.shp 

Capa de poligonos que indica la geometría válida de la capa


Imagen de la capa
^^^^^^^^^^^^^^^^^^^^

.. note::

    El código genera una imagen de la capa con el mapa base de openstreetmap 
    sí y solo sí la capa tiene un puntaje de 10 en el criterio de **proyección**







