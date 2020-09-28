SIGclassifier
#############

Guía de usuario de SIGclassifier
********************************

1 Introducción
***************

1.1	¿Por qué es necesario SIGclassifier?
=========================================

2 Organización del manual 
*************************

Este manual tiene el propósito de mostrar el uso del módulo SIGclassifier mediante (1) la explicación de todas las funciones de la plataforma (Sección 3. Organización de la Interfaz) y (2) la ilustración de un ejemplo de uso (Sección 4. Ejemplo de uso). Asimismo, se incluye bibliografía relevante como complemento teórico.

3 Organización de la interfaz
*****************************
.. imagen:: /imagenes/mapa_org_interfaz_sigclassifier.png 

La interfaz está organizada en las siguientes secciones: |no_1| el encabezado contiene al título y las funciones básicas, |no_2| en el panel izquierdo se ubica la barra de herramientas, y |no_3| el visualizador de capas incluye |no_4| los ajustes de despliegue de capas y |no_5| los ajustes de visualización.

3.1	Funciones básicas
=====================

Las funciones básicas son cuatro: botón de inicio, aplicar clasificador, exportar resultados y regresar.

3.1.1 Botón de inicio
---------------------

Al hacer clic en el botón de inicio |b_inicio|, se despliega una ventana con tres opciones: |no_1| redirecciona al **inicio** (home) de la plataforma SIGplanning, |no_2| muestra el **nombre del usuario** activo y |no_3| **cierra la sesión** del usuario activo. 

.. imagen:: /imagenes/mapa_b_inicio_sigclassifier.png

3.1.2 Aplicar clasificador
--------------------------

Al hacer clic en el botón de aplicar clasificador |b_aplicar|, se despliega el mapa con el clasificador seleccionado. Para que se genere este archivo, el usuario debe haber seleccionado un tipo de clasificador y los parámetros correspondientes (ver apartado 3.5.1.1).

.. imagen:: /imagenes/mapa_aplica_clasificador.png

3.1.3 Exportar
--------------

Al hacer clic en el botón de exportar |b_exportar|, se descarga un shapefile de las unidades naturales en formato **.zip**, el cual contiene la capa ráster .tif y el metadato asociado en formato .xml, producto del uso del SIGclassifier. Para que se genere este archivo, el usuario debe haber seleccionado un tipo de clasificador y los parámetros correspondientes (ver apartado 3.5.1.1).

.. imagen:: /imagenes/mapa_b_exportar_sigclassifier.png

3.1.4 Regresar
--------------

SIGclassifier tiene dos opciones para regresar al catálogo de proyectos y al resto de los módulos de SIGplanning: |no_1| el botón de regresar |b_regresar| y |no_2| el ícono del módulo |b_icono_classifier|. 

.. imagen:: /imagenes/mapa_b_regresar_sigclassifier.png

3.2	Visualizador de capas 
=========================

En el visualizador de capas |no_1| se muestran los resultados de SIGclassifier, así como, |no_2| los ajustes de despliegue de capas y |no_3| los ajustes de visualización. En el visualizador se puede mover el mapa, rotar el mapa, hacer acercamientos y ver el valor resultante de la clasificación.  

.. imagen:: /imagenes/mapa_vis_capas_sigclassifier.png

3.2.1 Mover el mapa
-------------------

Hacer clic en cualquier parte del visualizador de capas, mover el ratón en cualquier dirección hasta que el mapa esté en la ubicación deseada. 

.. imagen:: /imagenes/mapa_mover_sigclassifier.png

3.2.2 Rotar el mapa
-------------------
Hacer clic en cualquier parte del visualizador de capas, sin soltar el ratón, oprimir la tecla Shift y rotar la capa hasta llegar a la orientación deseada. 
Al rotar el mapa, |no_1| aparece el botón del norte geográfico rotado |b_norterotado|. Al hacer clic sobre el norte geográfico, se reposiciona el mapa a la orientación original.    

.. imagen:: /imagenes/mapa_rotado_sigclassifier.png

3.2.3 Hacer acercamientos
-------------------------

Hacer clic en cualquier parte del visualizador de capas y mover la barra de desplazamiento del ratón para acercarse o alejarse. 

.. imagen:: /imagenes/mapa_acercar_sigclassifier.png

3.2.4 Visualizar el resultado de la clasificación
-------------------------------------------------

Al hacer clic en un pixel de la capa, se despliega |no_1| una ventana con el valor del pixel de la capa original y la capa resultado de la clasificación. 

.. imagen:: /imagenes/mapa_vis_clasif_sigclassifier.png 

3.3	Ajustes de despliegue de capas 
==================================

Al hacer clic en el botón de ajustes de despliegue de capas |b_ajuste_capas|, se despliega una ventana con las opciones: |no_1| activar o desactivar capas, |no_2| cambiar el orden de sobreposición de las capas, |no_3| cambiar la transparencia de las capas y |no_4| cambiar la capa base. 

.. imagen:: /imagenes/mapa_desp_capa_sigclassifier.png

3.3.1 Activar o desactivar capas
--------------------------------

Al hacer clic sobre las casillas de verificación |b_activar_capas|, |no_1| se activan o desactivan las capas deseadas. Si se desactiva la capa resultado o la capa original |no_2| se cierran o despliegan las ventanas de los gradientes de estas capas.  

.. imagen:: /imagenes/mapa_b_activarcapa_sigclassifier.png

3.3.2	Cambiar el orden de sobreposición de las capas
------------------------------------------------------
 
Al hacer clic sobre el botón del orden de sobreposición de capas |b_sobreposicion|, deslizar hacia arriba o abajo hasta que se ubiquen en el orden deseado. 

.. imagen:: /imagenes/mapa_sobreposicion_sigclassifier.png

3.3.3	Cambiar la opacidad de las capas
----------------------------------------

Al hacer clic sobre el control deslizante de opacidad de capas |b_opacidad|, desplazar a la derecha o izquierda hasta llegar a la opacidad deseada.

.. imagen:: /imagenes/mapa_opacidad_sigclassifier.png
 
3.3.4	Cambiar la capa base
----------------------------

Los ajustes de despliegue de capas tienen cuatro opciones de capa base: |no_1| OpenLayer, |no_2| Stamen, |no_3| Mapa o |no_4| Satélite. Al hacer clic en el botón de selección |b_seleccion|, se selecciona la capa base deseada. 

.. imagen:: /imagenes/mapa_camb_capab_sigclassifier.png

Nota: La opción predeterminada es Satélite.  

3.4	Ajustes de visualización
============================

Esta sección se compone de seis botones: |no_1| cambiar al visualizador de capas en pantalla completa, |no_2| acercar el mapa, |no_3| alejar el mapa, |no_4| reajustar el norte geográfico, |no_5| ver la guía rápida de controles de despliegue y |no_6| ver la licencia de la capa base. 
 
.. imagen:: /imagenes/mapa_ajustes_vis_sigclassifier.png

3.4.1	Poner el mapa en pantalla completa
------------------------------------------

Al hacer clic |no_1| en el botón de pantalla completa |b_pantalla_comp|, |no_2| se muestra el área de visualización en la pantalla sin el resto de las secciones. 

.. imagen:: /imagenes/mapa_pantalla_comp_sigclassifier.png

.. imagen:: /imagenes/mapa_pantalla_comp2_sigclassifier.png

Para salir de la pantalla completa, volver a oprimir el botón de los ajustes de visualización o la tecla **Esc**. 

3.4.2	Acercar o alejar el mapa
--------------------------------

Al hacer clic sobre el botón de acercar |b_mas|, |no_1| se aumenta el zoom en el visualizador de capas. 
Al hacer clic sobre el botón de alejar |b_menos|, |no_2| se disminuye el zoom en el visualizador de capas. 

.. imagen:: /imagenes/mapa_acercar_alejar_sigclassifier.png

3.4.3	Ajustar el norte del mapa
---------------------------------
 
Al hacer clic en el botón de norte geográfico |b_norte|, se reajusta la orientación del visualizador de capas a la posición original.  

.. imagen:: /imagenes/mapa_ajustar_norte_sigclassifier.png

3.4.4	Guía rápida de controles de despliegue
----------------------------------------------

Al hacer clic en el botón de guía rápida de controles de despliegue |b_interrogacion|, se despliega una ventana con dos opciones: |no_1| rotar el mapa y |no_2| hacer zoom a una ventana específica. 

.. imagen:: /imagenes/mapa_guia_sigclassifier.png

3.5	Barra de herramientas 
=========================

3.5.1 Clasificador 
--------------------------

Al hacer clic en el botón **Clasificador** |b_atributos| se despliega una ventana con dos paneles: |no_1| **Clasificador** y |no_2| **Parámetros**.

.. imagen:: /imagenes/mapa_b_clasificador.png

El primer panel tiene la función de |no_1|, seleccionar el tipo de clasificador. El segundo panel tiene la función de |no_2| seleccionar parámetros según el clasificador elegido.

.. imagen:: /imagenes/fi_ventana_clasif.png

3.5.1.1	Seleccionar el Clasificador
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en la lista de despliegue |b_seleccionar| del clasificador se despliegan cuatro tipos de clasificaciones: |no_1| Weber-Feshner, |no_2| Progresiva, |no_3| Cuantiles y |no_4| Natural breaks.

.. imagen:: /imagenes/fi_ventana_selec_clasif.png            
 
Al hacer clic en el clasificador |b_weber|, en el panel de **Parámetros** se muestran los valores **Máximo** y **Mínimo** predeterminados, los cuales no pueden ser modificados. El usuario debe elegir |no_1| el valor del factor de progresión que aparece |no_2| en la casilla del **Factor** y |no_3| el **número de categorías**.

.. imagen:: /imagenes/fi_ventana_clasif_weber.png    

Para cambiar el factor de progresión, hacer clic en el botón del control deslizante |b_factor_progre|, desplazar hacia la derecha o izquierda hasta llegar al valor deseado. Automáticamente se muestra el valor en la casilla del **Factor** que puede ir de la **clasificación equidistante** (C. E.) hasta el valor 3. 

.. imagen:: /imagenes/fi_ventana_clas_equid.png 

Para cambiar el número de categorías hacer clic en los botones |boton_mas| y |boton_menos| para aumentar o disminuir la cantidad de las categorías seleccionadas. 

.. imagen:: /imagenes/fi_ventana_num_catego.png 

Hacer clic en el botón de **Aplicar clasificador** |b_aplicar| que se encuentra en la parte superior de las funciones básicas de la interfaz, y se despliega en el visualizador de capas el mapa resultado de la aplicación del clasificador seleccionado.  

.. imagen:: /imagenes/mapa_aplic_clas_weber.png 

Al hacer clic en el clasificador |b_progresiva| en el panel de **Parámetros** se muestran los valores **Máximo** y **Mínimo** predeterminados, los cuales no pueden ser modificados. El usuario debe elegir |no_1| el valor del factor de progresión que aparece |no_2| en la casilla del **Factor**, y |no_3| el **número de categorías**. 

.. imagen:: /imagenes/fi_ventana_clasif_progre.png    

Para cambiar el factor de progresión, hacer clic en el botón del control deslizante |b_factor_progre|, desplazar hacia la derecha o izquierda hasta llegar al valor deseado. Automáticamente se muestra el valor en la casilla del **Factor** que puede ir de la **clasificación equidistante** (C. E.) hasta el valor 3. 

.. imagen:: /imagenes/fi_ventana_ce_progre.png   

Para cambiar el número de categorías hacer clic en los botones |boton_mas| y |boton_menos| para aumentar o disminuir la cantidad de las categorías seleccionadas. 

.. imagen:: /imagenes/fi_ventana_num_catego_progre.png 

Hacer clic en el botón de **Aplicar clasificador** |b_aplicar| que se encuentra en la parte superior de las funciones básicas de la interfaz, y se despliega en el visualizador de capas el mapa resultado de la aplicación del clasificador seleccionado.  

.. imagen:: /imagenes/mapa_aplic_clas_progre.png 

Al hacer clic en el clasificador |b_cuantiles| en el panel de **Parámetros** se muestran los valores **Máximo** y **Mínimo** predeterminados, los cuales no pueden ser modificados. En la parte inferior del panel se muestra una lista desplegable con los tipos de cuantiles a elegir: |no_1| Cuartiles, |no_2| Quintiles y |no_3| Deciles.

.. imagen:: /imagenes/fi_ventana_clasif_cuantiles.png   

Hacer clic en el botón de **Aplicar clasificador** |b_aplicar| que se encuentra en la parte superior de las funciones básicas de la interfaz, y se despliega en el visualizador de capas el mapa resultado de la aplicación del clasificador seleccionado.   	
 
.. imagen:: /imagenes/mapa_aplic_clas_cuantiles.png 	
 
Al hacer clic en el clasificador |b_natural| en el panel de **Parámetros** se muestran los valores **Máximo** y **Mínimo** predeterminados, los cuales no pueden ser modificados. Para cambiar el número de categorías hacer clic en los botones |boton_mas| y |boton_menos| para aumentar o disminuir la cantidad de las categorías seleccionadas. 
 
.. imagen:: /imagenes/fi_ventana_clasif_natural.png   

Hacer clic en el botón de **Aplicar clasificador** |b_aplicar| que se encuentra en la parte superior de las funciones básicas de la interfaz, y se despliega en el visualizador de capas el mapa resultado de la aplicación del clasificador seleccionado.   	

.. imagen:: /imagenes/mapa_aplic_clas_natural.png 
 	 
3.5.2 Paletas de colores
------------------------

Al hacer clic en el botón |b_paleta| se despliega una ventana que muestra la gama de color en la que aparece la capa original y la capa resultado invitando a seleccionar un color. 

.. imagen:: /imagenes/mapa_paleta_sigclassifier.png
 
3.5.2.1	Cambiar el color de las capas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en el botón |b_list| aparece |no_1| una lista de despliegue con 12 paletas de colores a elegir, |no_2| al hacer clic en el control deslizante hacia arriba y abajo se puede |no_3| seleccionar una paleta para representar los valores de la capa en el visualizador. 

.. imagen:: /imagenes/fi_ventana_paleta_sigclassifier.png   

4	Requerimientos
******************

5	Herramientas 
****************

5.1	Crear un proyecto nuevo
===========================

6	Ejemplo de uso 
******************

7	Referencias
***************

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

.. |b_icono_classifier| image:: /imagenes/fi_b_iconosigclassifier.png
            :height: 25px
            :width: 25px         

.. |boton_mas| image:: /imagenes/boton_mas.png
            :height: 25px
            :width: 25px   

.. |boton_menos| image:: /imagenes/boton_menos.png
            :height: 25px
            :width: 25px  

.. |b_valores| image:: /imagenes/b_ocultar_sigindex.png
            :height: 25px
            :width: 25px  

.. |b_valores_activ| image:: /imagenes/fi_b_mostrar_sigindex.png
            :height: 25px
            :width: 25px   

.. |b_pestaña| image:: /imagenes/fi_b_ventana_val_sigindex.png
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
            :scale: 40

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

.. |b_atributos| image:: /imagenes/fi_b_atributos.png
            :height: 25px
            :width: 25px 

.. |b_seleccionar| image:: /imagenes/fi_b_seleccionar.png
            :scale: 40

.. |b_weber| image:: /imagenes/fi_b_weber.png
            :scale: 50

.. |b_progresiva| image:: /imagenes/fi_b_progresiva.png
            :scale: 50

.. |b_cuantiles| image:: /imagenes/fi_b_cuantiles.png
            :scale: 50
 
.. |b_natural| image:: /imagenes/fi_b_natural.png
            :scale: 50

.. |b_factor_progre| image:: /imagenes/fi_b_factorp.png
            :scale: 30 

.. |b_aplicar| image:: /imagenes/fi_b_aplicar_clas.png
            :height: 25px
            :width: 25px

.. |b_list| image:: /imagenes/fi_lista_despliegue.png
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
            :scale: 50


