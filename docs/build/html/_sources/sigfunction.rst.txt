Sigfunction
###############

Guía de usuario de SIGfunction
******************************

1 Introducción
***************

SIGfunction es una herramienta que genera una representación de la condición o estado de un atributo del territorio en un valor numérico que denota su capacidad para satisfacer un objetivo o meta en particular. 

SIGfunction emplea una expresión matemática para transformar la escala natural que mide el estado de un atributo del territorio a una escala de valor entre cero y uno, que representa un gradiente de un estado anti-ideal a uno ideal de acuerdo con su contribución para el cumplimiento del objetivo o meta (0 representando la condición más indeseable y 1 la más deseable).
Existen dos tipos generales de funciones de valor: nominales y continuas. Las funciones de valor nominales se usan para representar los diferentes estados de variables que se identifican con categorías o nombres. Por ejemplo, el tipo de vegetación que se representa en categorías como bosque o selva; o el tipo de suelo, que se representa en categorías como xerosol o regosol. Las funciones de valor continuas se usan para representar los diferentes estados de variables cuyo valor cambia en forma gradual. Por ejemplo, precipitación (en mm) o distancia a una carretera (en km). Estas funciones se pueden representar a través de diversos tipos de curvas.

SIGfunction se utiliza para desarrollar funciones de valor continuas.

SIGfunction permite analizar la condición de los atributos del territorio a partir de su significado y visualizarlo en un mapa. Así, se hace una liga explícita entre la información fáctica y el juicio de valor (Beinat 1997).

1.1	¿Por qué es necesario SIGfunction?
=========================================

SIGfunction facilita la visualización de las condiciones del territorio, en términos de su significado para el cumplimiento de un objetivo o meta. 

SIGfunction permite tratar como equivalentes diversos atributos del territorio, mediante el uso de una escala de medición común que representa su contribución para cumplir un objetivo o meta. 

2 Organización del manual 
*************************

Este manual tiene el propósito de mostrar el uso del módulo SIGfunctionD mediante (1) la explicación de todas las funciones de la plataforma (Sección 3. Organización de la Interfaz) y (2) la ilustración de un ejemplo de uso (Sección 4. Ejemplo de uso). Asimismo, se incluye bibliografía relevante como complemento teórico.

3 Organización de la interfaz
*****************************
.. imagen:: /imagenes/mapa_org_interfaz_sigfunction.png 

La interfaz está organizada en las siguientes secciones: |no_1| el encabezado contiene al título y las funciones básicas, |no_2| en el panel izquierdo se ubica la barra de herramientas, y |no_3| el visualizador de capas incluye |no_4| los ajustes de despliegue de capas y |no_5| los ajustes de visualización.

3.1	Funciones básicas
=====================

Las funciones básicas son cuatro: botón de inicio, generar función de valor, exportar resultados y regresar. 

3.1.1 Botón de inicio
---------------------

Al hacer clic en el botón de inicio |b_inicio|, se despliega una ventana con tres opciones: |no_1| redirecciona al **inicio** (home) de la plataforma SIGplanning, |no_2| muestra el **nombre del usuario** activo y |no_3| **cierra la sesión** del usuario activo. 

.. imagen:: /imagenes/mapa_b_inicio_sigfunction.png

3.1.2 Generar función de valor
------------------------------

Al hacer clic en el botón generar función de valor |b_aplicar|, se genera el mapa que resulta de la aplicación de SIGfunction y se despliega en el visualizador de capas. Para que se genere el mapa, el usuario debió haber seleccionado una función de valor y especificado los parámetros (ver apartado 3.5.1.1).

.. imagen:: /imagenes/mapa_generar_fv.png

3.1.3 Exportar
--------------

Al hacer clic en el botón de exportar |b_exportar|, se descarga un shapefile de las unidades naturales en formato **.zip**, el cual contiene la capa ráster .tif y el metadato asociado en formato .xml, producto del uso del SIGfunction. Para que se genere el shapefile de resultados, el usuario debió haber seleccionado una función de valor, especificado los parámetros y hacer clic en el botón de Generar Función de Valor |b_aplicar| (ver apartado 3.5.1.1). 

.. imagen:: /imagenes/mapa_b_exportar_sigfunction.png

3.1.4 Regresar
--------------

SIGfunction tiene dos opciones para regresar al catálogo de proyectos y al resto de los módulos de SIGplanning: |no_1| el botón de regresar |b_regresar| y |no_2| el ícono del módulo |b_icono_function|. 

.. imagen:: /imagenes/mapa_b_regresar_sigfunction.png

3.2	Visualizador de capas 
=========================

En el visualizador de capas |no_1| se muestran los resultados de SIGfunction, así como, |no_2| los ajustes de despliegue de capas y |no_3| los ajustes de visualización. En el visualizador se puede mover el mapa, rotar el mapa, hacer acercamientos y ver el valor resultante de la clasificación.  

.. imagen:: /imagenes/mapa_vis_capas_sigfunction.png

3.2.1 Mover el mapa
-------------------

Hacer clic en cualquier parte del visualizador de capas, mover el ratón en cualquier dirección hasta que el mapa esté en la ubicación deseada. 

.. imagen:: /imagenes/mapa_mover_sigfunction.png

3.2.2 Rotar el mapa
-------------------
Hacer clic en cualquier parte del visualizador de capas, sin soltar el ratón, oprimir la tecla *Shift* y rotar la capa hasta llegar a la orientación deseada. 
Al rotar el mapa, |no_1| aparece el botón del norte geográfico rotado |b_norterotado|. Al hacer clic sobre el norte geográfico, se reposiciona el mapa a la orientación original.    

.. imagen:: /imagenes/mapa_rotado_sigfunction.png

3.2.3 Hacer acercamientos
-------------------------

Hacer clic en cualquier parte del visualizador de capas y mover la barra de desplazamiento del ratón para acercarse o alejarse. 

.. imagen:: /imagenes/mapa_acercar_sigfunction.png

3.2.4 Visualizar valores de la capa
-----------------------------------

Al hacer clic |no_1| en un pixel de la capa, se despliega |no_2| una ventana con el valor del pixel de la capa original y la capa resultante del uso de SIGfunction. 

.. imagen:: /imagenes/mapa_vis_valores_capas.png 

3.3	Ajustes de despliegue de capas 
==================================

Al hacer clic en el botón de ajustes de despliegue de capas |b_ajuste_capas|, se despliega una ventana con las opciones: |no_1| activar o desactivar capas, |no_2| cambiar el orden de sobreposición de las capas, |no_3| cambiar la transparencia de las capas y |no_4| cambiar la capa base. 

.. imagen:: /imagenes/mapa_desp_capa_sigfunction.png

3.3.1 Activar o desactivar capas
--------------------------------

Al hacer clic sobre las casillas de verificación |b_activar_capas|, |no_1| se activan o desactivan las capas deseadas. Si se desactiva la capa resultado o la capa original |no_2| se cierran o despliegan las ventanas de los gradientes de estas capas.  

.. imagen:: /imagenes/mapa_b_activarcapa_sigfunction.png

3.3.2	Cambiar el orden de sobreposición de las capas
------------------------------------------------------
 
Al hacer clic sobre el botón del orden de sobreposición de capas |b_sobreposicion|, deslizar hacia arriba o abajo hasta que se ubiquen en el orden deseado. 

.. imagen:: /imagenes/mapa_sobreposicion_sigfunction.png

3.3.3	Cambiar la opacidad de las capas
----------------------------------------

Al hacer clic sobre el control deslizante de opacidad de capas |b_opacidad|, desplazar a la derecha o izquierda hasta llegar a la opacidad deseada.

.. imagen:: /imagenes/mapa_opacidad_sigfunction.png
 
3.3.4	Cambiar la capa base
----------------------------

Los ajustes de despliegue de capas tienen cuatro opciones de capa base: |no_1| OpenLayer, |no_2| Stamen, |no_3| Mapa o |no_4| Satélite. Al hacer clic en el botón de selección |b_seleccion|, se selecciona la capa base deseada. 

.. imagen:: /imagenes/mapa_cambiar_capab_sigfunction.png

Nota: La opción predeterminada es Satélite.  

3.4	Ajustes de visualización
============================

Esta sección se compone de seis botones: |no_1| cambiar al visualizador de capas en pantalla completa, |no_2| acercar el mapa, |no_3| alejar el mapa, |no_4| reajustar el norte geográfico, |no_5| ver la guía rápida de controles de despliegue y |no_6| ver la licencia de la capa base. 
 
.. imagen:: /imagenes/mapa_ajustes_vis_sigfunction.png

3.4.1	Poner el mapa en pantalla completa
------------------------------------------

Al hacer clic |no_1| en el botón de pantalla completa |b_pantalla_comp|, |no_2| se muestra el área de visualización en la pantalla sin el resto de las secciones. 

.. imagen:: /imagenes/mapa_pantalla_comp_sigfunction.png

.. imagen:: /imagenes/mapa_pantalla_comp2_sigfunction.png

Para salir de la pantalla completa, volver a oprimir el botón de los ajustes de visualización o la tecla **Esc**. 

3.4.2	Acercar o alejar el mapa
--------------------------------

Al hacer clic sobre el botón de acercar |b_mas|, |no_1| se aumenta el zoom en el visualizador de capas. 
Al hacer clic sobre el botón de alejar |b_menos|, |no_2| se disminuye el zoom en el visualizador de capas. 

.. imagen:: /imagenes/mapa_acercar_alejar_sigfunction.png

3.4.3	Ajustar el norte del mapa
---------------------------------
 
Al hacer clic en el botón de norte geográfico |b_norte|, se reajusta la orientación del visualizador de capas a la posición original.  

.. imagen:: /imagenes/mapa_ajustar_norte_sigfunction.png

3.4.4	Guía rápida de controles de despliegue
----------------------------------------------

Al hacer clic en el botón de guía rápida de controles de despliegue |b_interrogacion|, se despliega una ventana con dos opciones: |no_1| rotar el mapa y |no_2| hacer zoom a una ventana específica. 

.. imagen:: /imagenes/mapa_guia_sigfunction.png

3.5	Barra de herramientas 
=========================

3.5.1 Función y valores 
-----------------------

Al hace clic en el botón de **Funciones y Valores**, |b_atributos| se despliega una ventana con dos paneles: |no_1| **Funciones** |no_2| y **Parámetros**.   

.. imagen:: /imagenes/mapa_funciones_valores.png

3.5.1.1	Seleccionar la función de valor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
En el panel **Funciones** se muestra el **Nombre de la Capa de Salida** del atributo |no_1| para el cual se va a generar la función de valor y una lista de despliegue |no_2| con diferentes tipos de funciones de valor al hacer clic sobre ésta se despliega una lista con once diferentes opciones.

.. imagen:: /imagenes/mapa_selec_fv.png 

Al hacer clic sobre cualquiera de las funciones de valor, se despliega una gráfica de dicha función con valores previamente establecidos al inicio del uso del módulo de sigfunction.

.. imagen:: /imagenes/mapa_grafica_fv.png 

3.5.1.2	Ajustar los parámetros de la función de valor 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
En el panel de **Parámetros**, hacer clic en los botones |boton_mas| y |boton_menos| para aumentar o disminuir los valores de la función de valor. 

.. imagen:: /imagenes/mapa_parametros.png 

3.5.1.3	Funciones campana y campana invertida
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al seleccionar las funciones **Campana** y **Campana Invertida**, se deben ingresar en los cuadros de texto: |no_1| el valor máximo y |no_2| el valor mínimo que puede tener el atributo en el territorio analizado, así como |no_3| el valor de la amplitud y |no_4| el valor del punto óptimo de la curva.

.. imagen:: /imagenes/mapa_campana.png 

3.5.1.4	Funciones cóncava creciente, cóncava decreciente, convexa creciente y convexa decreciente
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al seleccionar las funciones **Cóncava Creciente**, **Cóncava Decreciente**, **Convexa Creciente** y **Convexa Decreciente**, se deben ingresar en los cuadros de texto: |no_1| el valor máximo y |no_2| el valor mínimo que puede tener el atributo en el territorio analizado, así como |no_3| el valor de saturación de la curva.

.. imagen:: /imagenes/mapa_concava.png             

3.5.1.5	Funciones lineal y lineal invertida
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al seleccionar las funciones **Lineal** y **Lineal Invertida**, se deben ingresar en los cuadros de texto: |no_1| el valor máximo y |no_2| el valor mínimo que puede tener el atributo en el territorio analizado, así como |no_3| el valor de la pendiente y de |no_4| la ordenada en el origen.

.. imagen:: /imagenes/mapa_lineal.png   
 
3.5.1.6	Funciones logística y logística invertida
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al seleccionar las funciones **Logística** y **Logística Invertida**, se deben ingresar en los cuadros de texto: |no_1| el valor máximo y |no_2| el valor mínimo que puede tener el atributo en el territorio analizado, así como |no_3| el valor de saturación y |no_4| el valor del centro de la curva.

.. imagen:: /imagenes/mapa_logistica.png    

3.5.1.7	Función coseno
^^^^^^^^^^^^^^^^^^^^^^
Al seleccionar la función de **Coseno**, se deben ingresar en los cuadros de texto: |no_1| el valor máximo y |no_2| el valor mínimo que puede tener el atributo en el territorio analizado, así como los valores de los parámetros de la función |no_3| A, |no_4| B, |no_5| C y |no_6| D. 

.. imagen:: /imagenes/mapa_coseno.png    

3.5.1.8	Generar mapa resultante de la aplicación de la función de valor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una vez definida la función de valor deseada, al hacer clic en el ícono **Generar Función de Valor** |b_aplicar| que se encuentra en el menú de Funciones básicas en la parte superior derecha, se muestra en |no_1| el visualizador de capas el texto **“Aplicando función de valor...”** y, después de unos segundos, se despliega |no_2| el mapa resultante de la aplicación de la función de valor seleccionada.

.. imagen:: /imagenes/mapa_aplicando.png 
 	 
3.5.2 Paletas de colores
------------------------

Al hacer clic en el botón |b_paleta| se despliega una ventana que muestra la gama de color en la que aparece |no_1| la capa original y |no_2| la capa resultado invitando a seleccionar un color. 

.. imagen:: /imagenes/mapa_paleta_sigfunction.png
 
3.5.2.1	Cambiar el color de las capas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al hacer clic en el botón |b_list| aparece una lista de despliegue con 12 paletas de colores a elegir, al hacer clic en el control deslizante hacia arriba y abajo se puede seleccionar una paleta para representar los valores de la capa en el visualizador. 

.. imagen:: /imagenes/fi_ventana_paleta_sigfunction.png   

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

.. |b_icono_functiond| image:: /imagenes/fi_b_iconosigfunctiond.png
            :height: 25px
            :width: 25px         

.. |b_icono_function| image:: /imagenes/fi_b_iconosigfunction.png
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

.. |b_atributos| image:: /imagenes/fi_b_valores_funciones.png
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


