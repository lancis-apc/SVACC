SIGnificance
###############
Guía de usuario de SIGnificance
*********************************

1 Introducción
****************

SIGnificance es una herramienta que agrega y sintetiza indicadores de impacto de distintos componentes ambientales en un índice único de significancia. 

SIGnificance emplea un algoritmo para incorporar la incertidumbre inherente durante la determinación de la significancia de impactos mediante una interfaz amigable. 

La aplicación permite explorar interactivamente los distintos enfoques o posiciones respecto a los impactos ambientales de un proyecto en un territorio. 

1.1	¿Por qué es necesario SIGnificance?
=======================================

SIGnificance facilita una discusión organizada de los principales impactos ambientales y sus implicaciones en el territorio. 

SIGnificance propicia un entorno para alcanzar acuerdos sobre cómo prevenir, mitigar o compensar impactos ambientales específicos. 

2 Organización del manual 
*************************

Este manual tiene el propósito de mostrar el uso del módulo SIGnificance mediante (1) la explicación de todas las funciones de la plataforma (Sección 3. Organización de la Interfaz) y (2) la ilustración de un ejemplo de uso (Sección 4. Ejemplo de uso). Asimismo, se incluye bibliografía relevante como complemento teórico.

3 Organización de la interfaz
*****************************

.. imagen:: /imagenes/fi_org_interfaz.png

La interfaz está organizada en las siguientes secciones: |no_1| el encabezado contiene al título y las funciones básicas, |no_2| en el panel izquierdo se ubica la barra de herramientas, y |no_3| el visualizador de capas incluye |no_4| los ajustes de despliegue de capas y |no_5| los ajustes de visualización.

3.1	Funciones básicas
=====================

Las funciones básicas son tres: botón de inicio, exportar resultados y regresar. 

3.1.1 Botón de inicio
---------------------

Al hacer clic en el botón de inicio |b_inicio|, se despliega una ventana con tres opciones: |no_1| redirecciona al **inicio** (home) de la plataforma SIGplanning, |no_2| muestra el **nombre del usuario** activo y |no_3| **cierra la sesión** del usuario activo. 

.. imagen:: /imagenes/mapa_b_inicio.png

3.1.2 Exportar
--------------

Al hacer clic en el botón de exportar |b_exportar|, se descarga un shapefile de las unidades naturales en formato **.zip** con los resultados del uso de SIGnificance. Para que se generen el shapefile de resultados, el usuario debió haber seleccionado un enfoque y factor de progresión (ver apartados 3.5.1.1 y 3.5.1.2). 

.. imagen:: /imagenes/mapa_b_exportar.png

3.1.3 Regresar
--------------

SIGnificance tiene dos opciones para regresar al catálogo de proyectos y al resto de los módulos de SIGplanning: |no_1| el botón de regresar |b_regresar| y |no_2| el ícono del módulo |b_icono|. 

.. imagen:: /imagenes/mapa_b_regresar.png

3.2	Visualizador de capas
=========================

En el visualizador de capas |no_1| se muestran los resultados de SIGnificance, así como, |no_2| los ajustes de despliegue de capas y |no_3| los ajustes de visualización. En el visualizador se puede mover el mapa, rotar el mapa, hacer acercamientos y seleccionar atributos.  

.. imagen:: /imagenes/mapa_visualizador_capas.png

3.2.1 Mover el mapa
-------------------

Al hacer clic en cualquier parte del visualizador de capas, mover el ratón en cualquier dirección hasta que el mapa esté en la ubicación deseada. 

.. imagen:: /imagenes/mapa_mover.png

3.2.2	Rotar el mapa
---------------------

Al hacer clic en cualquier parte del visualizador de capas, sin soltar el ratón, oprimir la tecla Shift y rotar la capa hasta llegar a la orientación deseada. 
Al rotar el mapa, |no_1| aparece el botón del norte geográfico rotado |b_norterotado|. Al hacer clic sobre el norte geográfico, se reposiciona el mapa a la orientación original.    

.. imagen:: /imagenes/mapa_rotado.png

3.2.3 Hacer acercamientos
-------------------------

Al hacer clic en cualquier parte del visualizador de capas, mover la barra de desplazamiento del ratón para acercarse o alejarse. 

.. imagen:: /imagenes/mapa_acercar.png

3.2.4 Seleccionar polígonos
---------------------------

3.2.4.1	Selección de un polígono
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en un polígono de la capa de unidades naturales, |no_1| se resalta con un contorno azul y |no_2| se despliega una ventana con el valor de significancia.  

.. imagen:: /imagenes/mapa_seleccion_poligono.png

3.2.4.2	Selección de varios polígonos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Crear una ventana de selección sobre el visualizador de capas, |no_1| al oprimir la tecla Ctrl, hacer clic en la esquina superior izquierda del inicio de la ventana, |no_2| desplazar el ratón hacia la derecha y abajo hasta seleccionar el número de polígonos deseados y |no_3| verificar el resultado. 

.. imagen:: /imagenes/mapa_selecc_variospo.png

.. imagen:: /imagenes/mapa_selecc_variospo2.png

Para eliminar cualquier selección oprimir el botón izquierdo del ratón en cualquier lugar fuera de la capa de unidades naturales. 
Nota: Todas las selecciones generan un filtro de los polígonos seleccionados en la tabla de Indicadores de impacto (ver Sección 3.5.2).

3.3	Ajustes de despliegue de capas
==================================

Al hacer clic en el botón de ajustes de despliegue de capas |b_ajuste_capas|, se despliega una ventana con las opciones: |no_1| activar o desactivar capas, |no_2| cambiar el orden de sobreposición de las capas, |no_3| cambiar la transparencia de las capas y |no_4| cambiar la capa base. 

.. imagen:: /imagenes/mapa_despliegue_capas.png

3.3.1	Activar o desactivar capas
----------------------------------

Al hacer clic sobre las casillas de verificación |b_activar_capas|, se activan o desactivan las capas deseadas. 

.. imagen:: /imagenes/mapa_b_activarcapas.png

3.3.2	Cambiar el orden de sobreposición de las capas
------------------------------------------------------

Al hacer clic sobre el botón del orden de sobreposición de capas |b_sobreposicion|, deslizar hacia arriba o abajo hasta que se ubiquen en el orden deseado. 

.. imagen:: /imagenes/mapa_sobreposicion.png

3.3.3	Cambiar la opacidad de las capas
----------------------------------------

Al hacer clic sobre el control deslizante de opacidad de capas |b_opacidad|, desplazar a la derecha o izquierda hasta llegar a la opacidad deseada.

.. imagen:: /imagenes/mapa_opacidad.png

3.3.4	Cambiar la capa base
----------------------------

Los ajustes de despliegue de capas tienen cuatro opciones de capa base: |no_1| OpenLayer, |no_2| Stamen, |no_3| Mapa o |no_4| Satélite.  Al hacer clic en el botón de selección |b_seleccion|, se selecciona la capa base deseada. 

.. imagen:: /imagenes/mapa_cambiar_capab.png

Nota: La opción predeterminada es Satélite.  

3.4	Ajustes de visualización
============================

La sección de ajustes de visualización se compone de seis botones: |no_1| cambiar al visualizador de capas en pantalla completa, |no_2| acercar el mapa, |no_3| alejar el mapa, |no_4| reajustar el norte geográfico, |no_5| ver la guía rápida de controles de despliegue y |no_6| ver la licencia de la capa base. 

.. imagen:: /imagenes/mapa_ajustes_vis.png

3.4.1	Poner el mapa en pantalla completa
------------------------------------------

Al hacer clic |no_1| en el botón de pantalla completa |b_pantalla_comp|, |no_2| se muestra el área de visualización en la pantalla sin el resto de las secciones. 

.. imagen:: /imagenes/mapa_pantalla_comp.png

.. imagen:: /imagenes/mapa_pantalla_comp2.png

Para salir de la pantalla completa, volver a oprimir el botón de los ajustes de visualización o la tecla Esc. 

3.4.2	Acercar o alejar el mapa
--------------------------------

Al hacer clic sobre el botón de acercar |b_mas|, |no_1| se aumenta el zoom en el visualizador de capas. 
Al hacer clic sobre el botón de alejar |b_menos|, |no_2| se disminuye el zoom en el visualizador de capas. 

.. imagen:: /imagenes/mapa_acercar_alejar.png

3.4.3	Ajustar el norte del mapa
---------------------------------

Al hacer clic en el botón de norte geográfico |b_norte|, se reajusta la orientación del visualizador de capas a la posición original.  

.. imagen:: /imagenes/mapa_ajustar_norte.png

3.4.4	Guía rápida de controles de despliegue
----------------------------------------------

Al hacer clic en el botón de guía rápida de controles de despliegue |b_interrogacion|, se despliega una ventana con tres opciones: |no_1| rotar el mapa, |no_2| seleccionar un polígono, y |no_3| hacer zoom a una ventana específica. 

.. imagen:: /imagenes/mapa_guia.png

3.5	Barra de herramientas 
=========================

3.5.1	Agregación 
------------------

Al hace clic en el botón de **Agregación** |b_agregacion|, se despliega una ventana con dos paneles: |no_1| **Enfoques** y |no_2| **Factor de progresión**. 

.. imagen:: /imagenes/mapa_agregacion.png

3.5.1.1	Ver el enfoque seleccionado
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El enfoque seleccionado en la agregación de significancia se muestra |no_1| en la matriz más grande del panel y |no_2| en el cuadro de texto. 

.. imagen:: /imagenes/fi_enfoque_selec.png

3.5.1.2	Cambiar el enfoque 
^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en cualquiera de los botones de enfoques |b_conservacionista|, |b_neutral|, o |b_desarrollista|, se selecciona el enfoque. La primera opción |no_1| corresponde al enfoque **conservacionista**, la segunda opción |no_2| al enfoque **neutral** y la tercera opción |no_3| al enfoque **desarrollista**. 

.. imagen:: /imagenes/fi_cambiar_enfoque.png

Los enfoques se pueden identificar al posicionar el cursor sobre de ellos. 

.. imagen:: /imagenes/fi_cambiar_enfoque2.png

Nota: La opción predeterminada es **neutral**.

3.5.1.3	Cambiar el nombre del enfoque
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Al escribir en el cuadro de texto |b_selec_neutral|, se sobrescribe el nombre original. Al hacer clic en el botón de guardar |b_guardar|, se salva el nuevo nombre del enfoque. 

.. imagen:: /imagenes/fi_cambiar_nombre_enfoque.png

Nota: No se recomienda cambiar los nombres predeterminados, a menos de que se haya determinado que éstos dificultan el proceso de facilitación.

3.5.1.4	Cambiar el factor de progresión
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en el botón del control deslizante y deslizar hacia la izquierda o derecha |b_factor_progre|, |no_1| se selecciona el factor de progresión. Al seleccionar el factor de progresión, |no_2| se actualizan la gráfica y panel de colores con los nuevos cortes de las categorías de significancia. C.E. |no_3| corresponde a una **clasificación equidistante**. 

.. imagen:: /imagenes/fi_factor_progre.png

3.5.1.5	Categorías de significancia
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Significance usa una paleta de colores de semáforo durante la clasificación de la significancia. Esta paleta se usa tanto en los enfoques como en la selección de factores de progresión.

.. imagen:: /imagenes/fi_significancia.png

3.5.2	Indicadores de impacto
------------------------------

Al hacer clic en el botón de indicadores de impacto |b_indicadores|, se despliega una ventana con |no_1| los valores de la tabla de indicadores tal como se agregaron al proyecto y |no_2| los resultados de la agregación |b_r|. 

.. imagen:: /imagenes/fi_indica_impacto.png

3.5.2.1	Ordenar columnas 
^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en la flecha |b_f_arriba| del encabezado de una columna, |no_1| se ordena **ascendentemente** esa columna.

Al hacer clic en la flecha |b_f_abajo| del encabezado de una columna, |no_2| se ordena **descendentemente** esa columna.

.. imagen:: /imagenes/fi_ordenar_colum.png

3.5.2.2	Aumentar o disminuir el tamaño de los caracteres 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en el botón |b_amas|, |no_1| se aumenta el tamaño de los caracteres en la tabla de indicadores. 
Al hacer clic en el botón |b_amenos|, |no_2| se disminuye el tamaño de los caracteres en la tabla de indicadores. 

.. imagen:: /imagenes/fi_ventana_tama_carac.png

3.5.2.3	Ver el nombre de los campos originales en la tabla de indicadores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los encabezados en la tabla de indicadores son nombrados con |no_1| los primeros dos caracteres de los nombres de los campos del archivo original para los indicadores de impacto y |no_2| las letras |b_vu| para los indicadores de vulnerabilidad. Al posicionar el ratón sobre cualquier encabezado, |no_3| se despliega el nombre de los campos del archivo original. 

.. imagen:: /imagenes/fi_campos_original.png

3.5.2.4	Seleccionar polígonos (renglones) específicos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en cualquier renglón de la tabla de indicadores, |no_1| se selecciona ese renglón y |no_2| se selecciona su polígono correspondiente en el visualizador de capas. 

.. imagen:: /imagenes/fi_polig_orig_esp.png

Al hacer clic en cualquier área del visualizador de capas fuera del mapa, se elimina la selección. 

.. imagen:: /imagenes/fi_polig_orig_esp2.png

3.5.3 Combo
-----------

El combo |b_combo| integra la funcionalidad de las herramientas |no_1| **Agregación** e |no_2| **Indicadores de impacto** en la misma ventana con el fin de facilitar el proceso de facilitación. Las funciones específicas de **Agregación** e **Indicadores de impacto** son explicadas en las herramientas 3.5.1 y 3.5.2.   

.. imagen:: /imagenes/fi_combo.png

3.5.4 Paletas de colores
------------------------

Al hacer clic en el botón **paletas de colores** |b_paleta|, |no_1| se despliega una ventana que muestra el color de la capa plano arquitectónico. 

.. imagen:: /imagenes/mapa_paleta.png

3.5.4.1	Cambiar el color del proyecto arquitectónico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en el botón de paletas de colores, |no_1| se despliega una ventana con dos secciones, |no_2| deslizar el cursor hacia arriba o abajo para seleccionar el tono en el panel derecho (en la rampa de colores) y |no_3| deslizar el cursor hasta seleccionar la saturación y brillo en el panel izquierdo. 

.. imagen:: /imagenes/fi_cambiar_color.png

4 Requerimientos
****************

SIGnificance tiene dos opciones de importación: insumos integrados o insumos desagregados. 

4.1	Insumos integrados 
======================

4.1.1 Shapefile de unidades naturales comprimido en formato .zip
----------------------------------------------------------------

•	Shapefile de unidades naturales que se compone de un mínimo de cinco archivos con las extensiones: nombre**.shp**, nombre**.shx**, nombre**.dbf**, nombre**.prj** y nombre.**xml**. Puede contener más archivos con extensiones adicionales dependiendo de la forma como se creó el shapefile. Para más información revisar: https://desktop.arcgis.com/es/arcmap/10.3/manage-data/shapefiles/shapefile-file-extensions.htm
•	Archivo **.dbf** que contiene la tabla de atributos debe incluir: |no_1| un campo de número identificador, |no_2| un campo con el nombre descriptivo de las unidades naturales y |no_3| un campo por cada índice de impacto y su contraparte de índice de vulnerabilidad. **Los valores de los campos de los índices de impacto y vulnerabilidad deben ser numéricos y normalizados entre cero y uno.** 

.. imagen:: /imagenes/fi_shape.png

4.1.2 Shapefile del plan maestro o proyecto arquitectónico (insumo opcional)
----------------------------------------------------------------------------

•	El shapefile que se compone de un mínimo de cinco archivos con las extensiones: nombre**.shp**, nombre**.shx**, nombre**.dbf**, nombre**.prj** y nombre**.xml.**  

4.2	Insumos desagregados
========================

4.2.1 Shapefile de unidades naturales comprimido en formato .zip 
----------------------------------------------------------------

•	Shapefile de unidades naturales que se compone de un mínimo de cinco archivos con las extensiones: nombre**.shp**, nombre**.shx**, nombre**.dbf**, nombre**.prj** y nombre**.xml**. Puede contener más archivos con extensiones adicionales dependiendo de la forma como se creó el shapefile. Para más información revisar: https://desktop.arcgis.com/es/arcmap/10.3/manage-data/shapefiles/shapefile-file-extensions.htm
•	Archivo **.dbf** que contiene la tabla de atributos debe incluir: (1) un campo de número identificador, y (2) nombre descriptivo de las unidades naturales

4.2.2 Archivo .csv de indicadores
---------------------------------

•	Archivo .csv debe incluir: |no_1| un campo del número identificador de la unidad natural (el mismo identificador usado en el shapefile para cada unidad natural) y |no_2| un campo por cada índice de impacto y su contraparte de índice de vulnerabilidad. **Los valores de los campos de los índices de impacto y vulnerabilidad deben ser numéricos y normalizados entre cero y uno.** 

.. imagen:: /imagenes/fi_csv.png

4.2.3 Shapefile del plan maestro o proyecto arquitectónico (insumo opcional)
----------------------------------------------------------------------------

•	Shapefile que se compone de un mínimo de cinco archivos con las extensiones: nombre**.shp**, nombre**.shx**, nombre**.dbf**, nombre**.prj** y nombre**.xml.**

5 Ejemplo de uso 
*******************

6 Referencias
*************


.. |no_1| image:: /imagenes/fi_uno.png
            :scale: 50

.. |no_2| image:: /imagenes/fi_dos.png
            :scale: 50

.. |no_3| image:: /imagenes/fi_tres.png
            :scale: 50

.. |no_4| image:: /imagenes/fi_cuatro.png
            :scale: 50   

.. |no_5| image:: /imagenes/fi_cinco.png
            :scale: 50

.. |no_6| image:: /imagenes/fi_seis.png
            :scale: 50

.. |b_inicio| image:: /imagenes/boton_inicio.png            
            :height: 25px
            :width: 25px

.. |b_exportar| image:: /imagenes/fi_b_exportar.png
            :height: 25px
            :width: 25px

.. |b_regresar| image:: /imagenes/fi_b_regresar.png
            :height: 25px
            :width: 25px         

.. |b_icono| image:: /imagenes/fi_b_icono.png
            :height: 25px
            :width: 25px         

.. |b_norterotado| image:: /imagenes/fi_norte_rotado.png
            :height: 25px
            :width: 25px 

.. |b_ajuste_capas| image:: /imagenes/fi_b_despliegue_capa.png
            :height: 25px
            :width: 25px 

.. |b_activar_capas| image:: /imagenes/fi_b_activar.png
            :height: 25px
            :width: 25px 

.. |b_sobreposicion| image:: /imagenes/fi_b_sobreposicion.png
            :height: 25px
            :width: 25px 

.. |b_opacidad| image:: /imagenes/fi_opacidad.png
            :height: 25px
            :width: 25px 

.. |b_seleccion| image:: /imagenes/fi_b_cambiarcapab.png
            :height: 25px
            :width: 25px 

.. |b_pantalla_comp| image:: /imagenes/fi_b_pantalla_comp.png
            :height: 25px
            :width: 25px 

.. |b_mas| image:: /imagenes/fi_b_mas.png
            :height: 25px
            :width: 25px 

.. |b_menos| image:: /imagenes/fi_b_menos.png
            :height: 25px
            :width: 25px       

.. |b_norte| image:: /imagenes/fi_b_norte.png
            :height: 25px
            :width: 25px                   

.. |b_interrogacion| image:: /imagenes/fi_b_interrogacion.png
            :height: 25px
            :width: 25px  

.. |b_agregacion| image:: /imagenes/fi_b_agregacion.png
            :height: 25px
            :width: 25px         

.. |b_conservacionista| image:: /imagenes/fi_b_conservacionista.png
            :height: 25px
            :width: 25px      

.. |b_neutral| image:: /imagenes/fi_b_neutral.png
            :height: 25px
            :width: 25px                                      

.. |b_desarrollista| image:: /imagenes/fi_b_desarrollista.png
            :height: 25px
            :width: 25px   

.. |b_selec_neutral| image:: /imagenes/fi_neutral.png
            :height: 25px
            :width: 25px    

.. |b_guardar| image:: /imagenes/fi_b_guardar.png
            :height: 25px
            :width: 25px 

.. |b_factor_progre| image:: /imagenes/fi_b_factorp.png
            :height: 25px
            :width: 25px   

.. |b_indicadores| image:: /imagenes/fi_b_indica_impac.png
            :height: 25px
            :width: 25px   

.. |b_r| image:: /imagenes/fi_b_r.png
            :height: 25px
            :width: 25px 

.. |b_f_arriba| image:: /imagenes/fi_flecha_arriba.png
            :height: 25px
            :width: 25px        

.. |b_f_abajo| image:: /imagenes/fi_flecha_abajo.png
            :height: 25px
            :width: 25px      

.. |b_amas| image:: /imagenes/fi_amas.png
            :height: 25px
            :width: 25px     
            
.. |b_amenos| image:: /imagenes/fi_amenos.png
            :height: 25px
            :width: 25px      

.. |b_vu| image:: /imagenes/fi_vu.png
            :height: 25px
            :width: 25px   

.. |b_combo| image:: /imagenes/fi_b_combo.png
            :height: 25px
            :width: 25px   

.. |b_paleta| image:: /imagenes/fi_b_paleta.png
            :height: 25px
            :width: 25px     

.. |b_paleta| image:: /imagenes/fi_b_paleta.png
            :height: 25px
            :width: 25px                                                                             