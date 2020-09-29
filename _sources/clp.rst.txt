Combinación líneal ponderada
#############################




Requerimientos generales 
--------------------------

Para asegurar la ejecución correcta del código es importante 
verificar la instalación y funcionamiento de los siguientes elementos:


- Qgis 3.10 con GRASS 7 y librerías de Osgeo4W
- Librerías python:
 - os
 - string


Requerimientos generales de los insumos
----------------------------------------

Es importante que todas las capas raster cumplan con las siguientes condiciones:


- Misma proyección cartográfica
- Mismo tamaño de pixel
- Misma extensión de capa
- Mismo valor de NoData


Requerimientos específicos
-----------------------------------------

El código esta diseñado para recibir como datos de entrada hasta 13 capas raster.




Diccionario de insumos
========================

Para ingresar los insumos a la función, el tipo de datos requerido 
es un diccionario en python, su estructura debe ser la siguiente:

.. code-block:: python

    dicc = {'nombre_criterio_1':{'ruta':"/criterio_1.tif",'peso':0.5},
            'nombre_criterio_2':{'ruta':"/criterio_1.tif",'peso':0.3},
            'nombre_criterio_3':{'ruta':"/criterio_1.tif",'peso':0.2}}
        
donde : **nombre_criterio_1** es el nombre del criterio, **ruta** es la ruta de la capa tif y **peso** es el valor del peso correspondiente al modelo.

Modo de decisión
========================
En la función **multicriteria_gis** se requiere que se específique el modo de decisión 


- Para elegir la combinación líneal ponderada escriba 'clp'
- Para elegir el modo parcialmente compensatorio escriba 'pc'
- Para elegir el modo no compensatorio escriba 'nc'


Documentación dentro del código
-----------------------------------------

.. automodule:: clpqgis3
    :members: