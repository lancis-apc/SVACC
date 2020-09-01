SIGindex
########

Guía de usuario de SIGindex
***************************

1 Introducción
****************

SIGIndex es una herramienta que integra mapas de aptitud a partir de funciones de valor. mediante una interfaz amigable.

SIGIndex tiene tres opciones de modos de decisión: el compensatorio (combinación lineal ponderada), el no compensatorio y el parcialmente compensatorio 

La aplicación permite explorar interactivamente el mapa de aptitud generado, así como las capas que lo integran 

1.1	¿Por qué es necesario SIGindex?
===================================

2 Organización del manual 
***************************

3 Organización de la interfaz
*****************************
 
.. imagen:: /imagenes/mapa_org_interfaz_sigindex.png 

La interfaz está organizada en las siguientes secciones: |no_1| el encabezado contiene al título y las funciones básicas, |no_2| en el panel izquierdo se ubica la barra de herramientas, y |no_3| el visualizador de capas incluye |no_4| los ajustes de despliegue de capas y |no_5| los ajustes de visualización.

3.1	Funciones básicas
=====================

Las funciones básicas son tres: botón de inicio, exportar resultados y regresar. 

3.1.1 Botón de inicio
---------------------

Al hacer clic en el botón de inicio |b_inicio|, se despliega una ventana con tres opciones: |no_1| redirecciona al **inicio** (home) de la plataforma SIGplanning, |no_2| muestra el **nombre del usuario** activo y |no_3| **cierra la sesión** del usuario activo. 

.. imagen:: /imagenes/mapa_b_inicio_sigindex.png

3.1.2 Exportar
--------------

Al hacer clic en el botón exportar |b_exportar| se despliega una ventana que descarga |no_1| el mapa de aptitud normalizado o |no_2| clasificado. Los mapas exportados en formato .zip incluyen una capa ráster en formato *.tif y el archivo de metadatos en formato *.xml.
 
.. imagen:: /imagenes/mapa_b_exportar_sigindex.png

3.1.3 Regresar 
--------------

SIGIndex tiene dos opciones para regresar al catálogo de proyectos y al resto de los módulos de SIGplaning: |no_1| el botón regresar |b_regresar| y |no_2| el ícono del módulo |b_icono|.

.. imagen:: /imagenes/mapa_b_regresar_sigindex.png

3.2	Visualizador de capas
==========================

En el visualizador de capas |no_1| se muestran los resultados de SIGindex, así como, |no_2| los ajustes de despliegue de capas y |no_3| los ajustes de visualización. En el visualizador se puede mover el mapa, rotar el mapa, hacer acercamientos y ver valores de la capa.  
 
.. imagen:: /imagenes/mapa_vis_capas_sigindex.png

3.2.1 Mover el mapa
---------------------

Al hacer clic en cualquier parte del visualizador de capas, mover el ratón en cualquier dirección hasta que el mapa esté en la ubicación deseada. 

.. imagen:: /imagenes/mapa_mover_sigindex.png

3.2.2 Rotar el mapa
---------------------

Al hacer clic en cualquier parte del visualizador de capas, sin soltar el ratón, oprimir la tecla Shift y rotar la capa hasta llegar a la orientación deseada. 
Al rotar el mapa, |no_1| aparece el botón del norte geográfico rotado |b_norterotado|. Al hacer clic sobre el norte geográfico, se reposiciona el mapa a la orientación original.    

.. imagen:: /imagenes/mapa_rotar_sigindex.png

3.2.3 Hacer acercamientos
---------------------------

Al hacer clic en cualquier parte del visualizador de capas, mover la barra de desplazamiento del ratón para acercarse o alejarse. 

.. imagen:: /imagenes/mapa_acercar_sigindex.png

3.2.4 Valores de la capa
--------------------------

Al hacer clic sobre |no_1| el pixel, se despliega |no_2| la ventana de valores en la parte inferior derecha de la ventana, donde se indica el valor del pixel.

.. imagen:: /imagenes/mapa_valor_capa.png

3.3	Ajustes de despliegue de capas
====================================

Los ajustes de despliegue de capas |b_ajuste_capas| permiten |no_1| activar o desactivar capas, |no_2| cambiar el orden de sobreposición de las capas, |no_3| cambiar la opacidad de las capas y |no_4| cambiar el mapa base.

.. imagen:: /imagenes/mapa_desp_capa_sigindex.png

3.3.1 Activar o desactivar capas
----------------------------------

Al hacer clic sobre las casillas de verificación |b_activar_capas| en la sección de ajustes de despliegue, se activan o desactivan las capas deseadas. 

.. imagen:: /imagenes/mapa_b_activarcapa_sigindex.png
 
3.3.2 Cambiar el orden de sobreposición de las capas
------------------------------------------------------

Para cambiar el orden de sobreposición de las capas, mantener oprimido el botón izquierdo del ratón sobre las flechas |b_sobreposicion| que aparecen a la derecha del panel y desplazar las capas hacia abajo o arriba conforme al orden deseado.  

.. imagen:: /imagenes/mapa_sobreposicion_sigindex.png

3.3.3 Cambiar la opacidad de las capas
----------------------------------------

Al hacer clic sobre el control deslizante de opacidad de capas |b_opacidad|, desplazar a la derecha o izquierda hasta llegar a la opacidad deseada.

.. imagen:: /imagenes/mapa_opacidad_sigindex.png
 
3.3.4 Cambiar la capa base
----------------------------

SIGIndex tiene cuatro opciones de capas base: |no_1| OpenLayer, |no_2| Stamen, |no_3| Mapa, |no_4| Satelite, para cambiar la capa base oprimir el botón de opción |b_seleccion| para seleccionar el mapa base de su preferencia.

.. imagen:: /imagenes/mapa_camb_capab_sigindex.png
 
Nota: La opción predeterminada es satélite. 

3.4	Ajustes de visualización
==============================

La sección de ajustes de visualización se compone de ocho botones: |no_1| mostrar/ocultar ventana de valores, |no_2| cambiar al visualizador de capas en pantalla completa, |no_3| acercar el mapa, |no_4| alejar el mapa, |no_5| reajustar el norte geográfico, |no_6| ver la guía rápida de controles de despliegue, |no_7| ocultar gradientes de capas, y |no_8| ver la licencia de la capa base. 

.. imagen:: /imagenes/mapa_ajustes_vis_sigindex.png

3.4.1 Mostrar/Ocultar ventana de valores  
------------------------------------------

Al hacer clic en el botón mostrar/ocultar ventana de valores |b_valores|, el fondo del botón cambia a verde indicando que la ventana de valores esta activa |b_valores_activ|, |no_1| al hacer clic en un píxel de cualquier se despliega una ventana que muestra el valor del píxel del mapa de aptitud, y |no_2| al hacer clic en el botón de la ventana de valores |b_pestaña|, se despliegan los valores de las funciones de valor (atributos). 

.. imagen:: /imagenes/mapa_ventana_val_sigindex.png 

.. imagen:: /imagenes/mapa_ventana_val_sigindex2.png 

3.4.2 Poner el mapa en pantalla completa
------------------------------------------

Al hacer clic |no_1| en el botón de pantalla completa |b_pantalla_comp|, |no_2| se muestra el área de visualización en la pantalla sin el resto de las secciones. 

.. imagen:: /imagenes/mapa_pantalla_comp_sigindex.png

.. imagen:: /imagenes/mapa_pantalla_comp2_sigindex.png

Para salir de la pantalla completa, volver a oprimir el botón de los ajustes de visualización o la tecla Esc. 

3.4.3 Acercarse o alejarse del mapa 
-------------------------------------
 
Al hacer clic sobre el botón de acercar |b_mas|, |no_1| se aumenta el zoom en el visualizador de capas. 
Al hacer clic sobre el botón de alejar |b_menos|, |no_2| se disminuye el zoom en el visualizador de capas. 

.. imagen:: /imagenes/mapa_acercar_alejar_sigindex.png
 
3.4.4 Ajustar el norte del mapa 
---------------------------------

Al hacer clic en el botón de norte geográfico |b_norte|, se reajusta la orientación del visualizador de capas a la posición original.  

.. imagen:: /imagenes/mapa_ajustar_norte_sigindex.png

3.4.5 Guía rápida de ajustes de visualización 
-----------------------------------------------
 
Al hacer clic en el botón de guía rápida de controles de despliegue |b_interrogacion|, se despliega una ventana con dos opciones: |no_1| rotar el mapa y |no_2| hacer zoom a una ventana específica. 

.. imagen:: /imagenes/mapa_guia_sigindex.png
 
3.4.6 Ocultar gradientes de capas
-----------------------------------

Al hacer clic |no_1| en el botón mostrar/ocultar gradientes de capas |b_gradiente_azul|, |no_2| el fondo del botón cambia a verde desplegando la ventana de gradientes |b_gradiente_verde|. 

.. imagen:: /imagenes/mapa_guia_sigindex.png

.. imagen:: /imagenes/mapa_guia_sigindex.png

3.5	Barra de herramientas 
===========================

Cuenta con tres herramientas, |no_1| Atributos |b_atributos|, |no_2| Clasificación progresiva |b_factor_progre| y |no_3| Paleta de colores |b_paleta|.
  
.. imagen:: /imagenes/mapa_barra_herramienta.png

3.5.1 Atributos
-----------------

Al hacer clic en el botón **Atributos** |b_atributos| se despliega una ventana con seis secciones: |no_1| nombre generado por el sistema, |no_2| lista de despliegue de modos de decisión, |no_3| atributos o funciones de valor, |no_4| lista de pesos asignados a cada función de valor, |no_5| casillas de verificación de los atributos seleccionados para integrar análisis de aptitud y |no_6| botón de Generar mapa de aptitud.

.. imagen:: /imagenes/fi_ventana_atributos.png

3.5.1.1	Modos de decisión
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en la lista de despliegue |b_list| se muestran cuatro opciones: |no_1| Compensatorio, |no_2| Parcialmente compensatorio, |no_3| No compensatorio, |no_4| Combinación lineal ponderada.

.. imagen:: /imagenes/fi_ventana_decision.png 

3.5.1.2	Selección y ponderación de atributos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En la ventana |no_1| se despliegan todos los atributos (funciones de valor) preseleccionados y su ponderación, |no_2| al seleccionar/deseleccionar haciendo clic en la casilla de verificación |no_3| se modifican los pesos de los atributos seleccionados automáticamente.   

.. imagen:: /imagenes/fi_selec_atributos.png 

Obsérvese que la suma de los pesos debe ser igual a 1 

3.5.1.3	Generar mapa de aptitud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en el botón |no_1| **Generar mapa de aptitud** |no_2| se desplegará en el visualizador de capas, el mapa de aptitud con el nombre |no_3| **Capa resultado**.

.. imagen:: /imagenes/mapa_actitud.png 

3.5.2 Factor de progresión
----------------------------

Al hacer clic en el botón **clasificación progresiva** se despliega una ventana con el control deslizante. Al hacer clic en el botón del control deslizante y deslizar hacia la izquierda o derecha |b_factor_progre|, |no_1| se selecciona el factor de progresión. C.E. |no_2| corresponde a una **clasificación equidistante**. 

.. imagen:: /imagenes/fi_ventana_fprogresion.png 

3.5.3 Paleta de colores
-------------------------

Al hacer clic en el botón paleta de colores |b_paleta|, |no_1| se despliegan los atributos (funciones de valor) y el mapa de aptitud (Proyecto). Cada capa cuenta con una lista de despliegue, |no_2| al hacer clic en el botón de la lista de despliegue |b_list|, |no_3| elegir la paleta de colores deseada.

.. imagen:: /imagenes/fi_ventana_paleta.png 

4 Requerimientos
****************

5 Herramientas 
**************

5.1	Crear un proyecto nuevo
===========================

6 Ejemplo de uso 
****************
 
7 Referencias
*************

Alvarez-Yépiz, J.C., Martínez-Yrízar, A., Búrquez, A., Lindquist, C. 2008. Variation in vegetation structure and soil properties related to land use history of old-growth and secondary tropical dry forests in northwestern Mexico. Forest Ecology and Management 256: 355-366. 

Bye, R., Cervantes, L., Rendón, B. 2002. Etnobotánica en la región de Chamela, Jalisco, México. En: Noguera, F., Vega-Rivera, J., García-Aldrete A., Quesada-Avendaño, M. Historia Natural de Chamela, pp. 545-559. Instituto de Biología, UNAM, México, DF.

Chao, A. 1987. Estimating the population size for capture-recapture data with unequal catchability. Biometrics 43, 783-791. 

César Dachary, Alfredo y Stella Maris Arnaiz Burne (Eds.) (2005) Turismo rural. Modelos y propuestas. Universidad de Guadalajara. México. 

CENAPRED. 2003. Integración de información para la estimación del Peligro Sísmico. Pág 61-74 En: Guía Básica para la Elaboración de Atlas Estatales y Municipales de Peligros y Riesgos, Sistema nacional de Protección Civil, 385pp. 

Colín-García, G., Ibáñez-Castillo, L., Reyes-Sánchez, J. y R. Arteaga-Ramírez. 2013. Diagnóstico de la erosión hídrica de la cuenca del Río Pichucalco. Ingeniería agrícola y biosistemas 5(1): 23-31. 

CONAGUA, 2012. Cobertura de agua potable por municipios y cobertura de alcantarillado por munici-pio. Atlas Digital del Agua de México, 2012. Sistema Nacional de Información del Agua. Consultado el 25/07/2014 en: http://www.conagua.gob.mx/atlas/mapa/28/index_svg.html y http://www.conagua.gob.mx/atlas/mapa/30/index_svg.html.

CONABIO 2012. Portal de Geoinformación, Sistema Nacional de Información sobre Biodiversidad. Consultado el 1/09/2014 en http://www.conabio.gob.mx/informacion/gis/

CONAGUA. 2012. Atlas Digital del Agua México 2012. Sistema Nacional de Información del Agua. Subdirección General Técnica. Gerencia de Aguas Subterráneas. Representación gráfica y espacial de las Zonas de Veda. Consultado el 7 de julio de 2014: http://www.conagua.gob.mx/atlas/mapa/36/index_svg.html.


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

.. |no_7| image:: /imagenes/fi_siete.png
            :scale: 50

.. |no_8| image:: /imagenes/fi_ocho.png
            :scale: 50

.. |b_inicio| image:: /imagenes/boton_inicio.png            
            :height: 25px
            :width: 25px

.. |b_gradiente_azul| image:: /imagenes/boton_gradientea.png            
            :height: 25px
            :width: 25px

.. |b_gradiente_verde| image:: /imagenes/boton_gradientev.png            
            :height: 25px
            :width: 25px  

.. |b_exportar| image:: /imagenes/fi_b_exportar.png
            :height: 25px
            :width: 25px

.. |b_regresar| image:: /imagenes/fi_b_regresar.png
            :height: 25px
            :width: 25px         

.. |b_icono| image:: /imagenes/fi_b_iconosigindex.png
            :height: 25px
            :width: 25px         

.. |b_valores| image:: /imagenes/b_ocultar_sigindex.png
            :height: 25px
            :width: 25px  

.. |b_valores_activ| image:: /imagenes/fi_b_mostrar_sigindex.png
            :height: 25px
            :width: 25px   

.. |b_pestaña| image:: /imagenes/fi_b_ventana_val_sigindex.png
            :height: 20px
            :width: 20px              

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

.. |b_factor_progre| image:: /imagenes/fi_b_factorp.png
            :scale: 30


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

