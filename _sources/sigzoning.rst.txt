SIGzoning
#########

Guía de usuario de SIGzoning
****************************

1 Introducción
**************

SIGzoning es una herramienta computacional que combina técnicas de análisis espacial con métodos de toma de decisiones y geovisualización para realizar el análisis de aptitud del territorio.

SIGzoning integra más de aptitud sectoriales en un análisis multiobjetivo de clasificación numérica y ganancia de homogeneidad para identificar grupos de aptitud. 

La clasificación numérica utiliza un método geoespacial recursivo politético-divisivo acoplado a técnicas de visualización que faciliten la traducción y comunicación de resultados. 

1.1	¿Por qué es necesario SIGzoning?
====================================

SIGzoning es necesario durante la realización de estudios de ordenamiento ecológico, en la etapa de diagnóstico, para minimizar los conflictos sectoriales que resultan de actividades incompatibles den el territorio. 

2 Organización del manual 
*************************

Este manual tiene el propósito de mostrar el uso del módulo SIGzoning mediante (1) la explicación de todas las funciones de la plataforma (Sección 3. Organización de la Interfaz) y (2) la ilustración de un ejemplo de uso (Sección 4. Ejemplo de uso). Asimismo, se incluye bibliografía relevante como complemento teórico.

3 Organización de la interfaz
*****************************
 
.. imagen:: /imagenes/mapa_org_interfaz_sigzoning.png 

La interfaz está organizada en las siguientes secciones: |no_1| el encabezado contiene al título y las funciones básicas, |no_2| en el panel izquierdo se ubica la barra de herramientas, y |no_3| el visualizador de capas incluye |no_4| los ajustes de despliegue de capas y |no_5| los ajustes de visualización.

3.1	Funciones básicas
=====================

Las funciones básicas son seis: botón de inicio, exportar resultados, exportar residuales, exportar promedios, número de cortes y regresar. 

3.1.1 Botón de inicio
---------------------

Al hacer clic en el botón de inicio |b_inicio|, se despliega una ventana con tres opciones: |no_1| redirecciona al **inicio** (home) de la plataforma SIGplanning, |no_2| muestra el **nombre del usuario** activo y |no_3| **cierra la sesión** del usuario activo. 

.. imagen:: /imagenes/mapa_b_inicio_sigzoning.png

3.1.2 Exportar resultados
-------------------------

Al hacer clic en el botón de exportar |b_exportar|, se descarga un archivo en formato **.zip**, el cual contiene la capa ráster .tif y el metadato asociado en formato .xml, producto del uso del SIGzoning. Para que se genere el mapa, el usuario debe haber seleccionado los cortes y generado el mapa de grupos de cortes (ver apartado 3.5.1.1).
 
.. imagen:: /imagenes/mapa_b_exportar_sigzoning.png

3.1.3 Exportar residuales
-------------------------

Al hacer clic en el botón de exportar residuales |b_exportar_residual|, se descarga un archivo **.xls**, con los valores de los residuales de los grupos de cortes elegidos (ver apartado *3.5.1.1* y *3.5.2.2*).

.. imagen:: /imagenes/mapa_b_export_residuales.png

3.1.4 Exportar promedios
------------------------

Al hacer clic en el botón de exportar promedios |b_exportar_promedio|, se descarga un archivo **.xls**, con los valores de los promedios de los grupos de cortes elegidos por sector (ver apartado *3.5.1.1* y *3.5.2.2*).

.. imagen:: /imagenes/mapa_b_export_promedio.png

3.1.5 Número de cortes
----------------------

El ícono |b_num_cortes| muestra el nivel de avance en la clasificación numérica. SIGzoning permite el análisis de resultados una vez terminado 15 cortes (o menos si los insumos no permiten una desagregación mayor).  

.. imagen:: /imagenes/mapa_b_num_cortes.png

3.1.6 Regresar 
--------------

SIGzoning tiene dos opciones para regresar al catálogo de proyectos y al resto de los módulos de SIGplaning: |no_1| el botón regresar |b_regresar| y |no_2| el ícono del módulo |b_icono|.

.. imagen:: /imagenes/mapa_b_regresar_sigindex.png

3.2	Visualizador de capas
==========================

En el visualizador de capas |no_1| se muestran los resultados de SIGzoning, así como, |no_2| los ajustes de despliegue de capas y |no_3| los ajustes de visualización. En el visualizador se puede mover el mapa, rotar el mapa y hacer acercamientos.  
 
.. imagen:: /imagenes/mapa_vis_capas_sigzoning.png

3.2.1 Mover el mapa
---------------------

Al hacer clic en cualquier parte del visualizador de capas, mover el ratón en cualquier dirección hasta que el mapa esté en la ubicación deseada. 

.. imagen:: /imagenes/mapa_mover_sigzoning.png

3.2.2 Rotar el mapa
---------------------

Al hacer clic en cualquier parte del visualizador de capas, sin soltar el ratón, oprimir la tecla *Shift* y rotar la capa hasta llegar a la orientación deseada. 
Al rotar el mapa, |no_1| aparece el botón del norte geográfico rotado |b_norterotado|. Al hacer clic sobre el norte geográfico, se reposiciona el mapa a la orientación original.    

.. imagen:: /imagenes/mapa_rotar_sigzoning.png

3.2.3 Hacer acercamientos
---------------------------

Al hacer clic en cualquier parte del visualizador de capas, mover la barra de desplazamiento del ratón para acercarse o alejarse. 

.. imagen:: /imagenes/mapa_acercar_sigzoning.png

3.2.4 Visualizar valores de los grupos de corte
-----------------------------------------------

Al hacer clic |no_1| en un pixel del mapa de grupo del proyecto, se despliega |no_2| una ventana con los valores de los pixeles de las capas de aptitud de las actividades seleccionadas por grupo de corte elegido (ver apartado *3.5.1.1*).

.. imagen:: /imagenes/mapa_vis_valores_sigzoning.png

3.3	Ajustes de despliegue de capas
====================================

Los ajustes de despliegue de capas |b_ajuste_capas| permiten |no_1| activar o desactivar capas, |no_2| cambiar el orden de sobreposición de las capas, |no_3| cambiar la opacidad de las capas y |no_4| cambiar el mapa base.

.. imagen:: /imagenes/mapa_desp_capa_sigzoning.png

3.3.1 Activar o desactivar capas
----------------------------------

Al hacer clic sobre las casillas de verificación |b_activar_capas| en la sección de ajustes de despliegue, se activan o desactivan las capas deseadas. 

.. imagen:: /imagenes/mapa_b_activarcapa_sigzoning.png
 
3.3.2 Cambiar el orden de sobreposición de las capas
------------------------------------------------------

Para cambiar el orden de sobreposición de las capas, mantener oprimido el botón izquierdo del ratón sobre las flechas |b_sobreposicion| que aparecen a la derecha del panel y desplazar las capas hacia abajo o arriba conforme al orden deseado.  

.. imagen:: /imagenes/mapa_sobreposicion_sigzoning.png

3.3.3 Cambiar la opacidad de las capas
----------------------------------------

Al hacer clic sobre el control deslizante de opacidad de capas |b_opacidad|, desplazar a la derecha o izquierda hasta llegar a la opacidad deseada.

.. imagen:: /imagenes/mapa_opacidad_sigzoning.png
 
3.3.4 Cambiar la capa base
----------------------------

SIGIndex tiene cuatro opciones de capas base: |no_1| OpenLayer, |no_2| Stamen, |no_3| Mapa, |no_4| Satelite, para cambiar la capa base oprimir el botón de opción |b_seleccion| para seleccionar el mapa base de su preferencia.

.. imagen:: /imagenes/mapa_camb_capab_sigzoning.png
 
Nota: La opción predeterminada es satélite. 

3.4	Ajustes de visualización
==============================

La sección de ajustes de visualización se compone de siete botones: |no_1| cambiar al visualizador de capas en pantalla completa, |no_2| acercar el mapa, |no_3| alejar el mapa, |no_4| reajustar el norte geográfico, |no_5| ver la guía rápida de controles de despliegue |no_6| ver u ocultar gradientes de capas y |no_7| ver la licencia de la capa base. 

.. imagen:: /imagenes/mapa_ajustes_vis_sigzoning.png

3.4.1 Poner el mapa en pantalla completa
------------------------------------------

Al hacer clic |no_1| en el botón de pantalla completa |b_pantalla_comp|, |no_2| se muestra el área de visualización en la pantalla sin el resto de las secciones. 

.. imagen:: /imagenes/mapa_pantalla_comp_sigzoning.png

.. imagen:: /imagenes/mapa_pantalla_comp2_sigzoning.png

Para salir de la pantalla completa, volver a oprimir el botón de los ajustes de visualización o la tecla Esc. 

3.4.2 Acercarse o alejarse del mapa 
-----------------------------------
 
Al hacer clic sobre el botón de acercar |b_mas|, |no_1| se aumenta el zoom en el visualizador de capas. 
Al hacer clic sobre el botón de alejar |b_menos|, |no_2| se disminuye el zoom en el visualizador de capas. 

.. imagen:: /imagenes/mapa_acercar_alejar_sigzoning.png
 
3.4.3 Ajustar el norte del mapa 
-------------------------------

Al hacer clic en el botón de norte geográfico |b_norte|, se reajusta la orientación del visualizador de capas a la posición original.  

.. imagen:: /imagenes/mapa_ajustar_norte_sigzoning.png

3.4.4 Guía rápida de ajustes de visualización 
---------------------------------------------
 
Al hacer clic en el botón de guía rápida de controles de despliegue |b_interrogacion|, se despliega una ventana con dos opciones: |no_1| rotar el mapa y |no_2| hacer zoom a una ventana específica. 

.. imagen:: /imagenes/mapa_guia_sigzoning.png
 
3.4.5 Ocultar gradientes de capas
---------------------------------

Al hacer clic |no_1| en el botón mostrar/ocultar gradientes de capas |b_gradiente_azul|, |no_2| el fondo del botón cambia a verde desplegando la ventana de gradientes |b_gradiente_verde|. 

.. imagen:: /imagenes/mapa_gradientes.png

.. imagen:: /imagenes/mapa_gradientes2.png

3.5	Barra de herramientas 
=========================

3.5.1 Cortes
------------

Al hace clic en el botón de **Cortes** |b_cortes|, se despliega una ventana con dos botones: |no_1| **Ver mapa de grupos del proyecto** y |no_2| **Ver gráficas de residuales del proyecto**, y el listado de los cortes: |no_3| **Mapas generados**.

.. imagen:: /imagenes/mapa_cortes.png

3.5.1.1	Seleccionar los mapas de los cortes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en la lista de despliegue |b_list| se muestran cuatro opciones: |no_1| Compensatorio, |no_2| Parcialmente compensatorio, |no_3| No compensatorio, |no_4| Combinación lineal ponderada.

.. imagen:: /imagenes/fi_ventana_decision.png 

3.5.1.2	Selección y ponderación de atributos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

3.5.4 Paleta de colores
-----------------------

Al hacer clic en el botón |b_paleta| se despliega una ventana que muestra la gama de color en la que aparecen las capas de las actividades invitando a seleccionar un color. 

.. imagen:: /imagenes/mapa_paleta_sigzoning.png
 
3.5.4.1	Cambiar el color de las capas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en el botón |b_list| aparece |no_1| una lista de despliegue con 12 paletas de colores a elegir, |no_2| al hacer clic en el control deslizante hacia arriba y abajo se puede |no_3| seleccionar una paleta para representar los valores de la capa en el visualizador. 

.. imagen:: /imagenes/fi_ventana_paleta_sigzoning.png   

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

.. |b_icono| image:: /imagenes/fi_b_iconosigzoning.png
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

.. |b_exportar_residual| image:: /imagenes/fi_b_export_residual.png
            :scale: 40

.. |b_exportar_promedio| image:: /imagenes/fi_b_export_promedio.png
            :scale: 40

.. |b_num_cortes| image:: /imagenes/fi_b_num_cortes.png
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

.. |b_clas_progre| image:: /imagenes/fi_b_factorp_sigindex.png
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

