# -*- coding: utf-8 -*-

'''
Autores: Fidel Serrano,Victor Hernandez


Qgis 3.4 o superior

'''

import copy
import pprint
import string
import qgis 
import qgis.core
from osgeo import gdal
import gdal_calc
import os
import processing as pr 
def raster_min_max(path_raster):
    '''
    Esta funcion regresa los valores maximos y minimos de una capa raster

    :param path_raster: ruta de la capa raster
    :type path_raster: str 
    '''
    rlayer = QgsRasterLayer(path_raster,"raster")
    extent = rlayer.extent()
    provider = rlayer.dataProvider()
    stats = provider.bandStatistics(1,
                                    QgsRasterBandStats.All,
                                    extent,
                                    0)

    v_min = stats.minimumValue
    v_max = stats.maximumValue
    return v_min, v_max

def get_region(path_layer):
    '''
    Esta función regresa en forma de cadena de texto 
    las coordenadas de la extensión de una capa raster

    param path_layer: ruta de la capa raster
    type path_layer: str
    '''

    layer = QgsRasterLayer(path_layer,"")
    ext = layer.extent()
    xmin = ext.xMinimum()
    xmax = ext.xMaximum()
    ymin = ext.yMinimum()
    ymax = ext.yMaximum()

    region = "%f,%f,%f,%f" % (xmin, xmax, ymin, ymax)
    return region

def nombre_capa(path_capa):
    '''
    Esta función regresa el nombre de una capa sin extensión 

    :param path_capa: ruta de la capa
    :type path_capa: str 


    '''
    nombre_capa=(path_capa.split("/")[-1:])[0].split(".")[0]
    return nombre_capa

def pesos_factores_vulnerabilidad(dicc):
    lista = []
    for k,v in dicc.items():
        lista.append(dicc[k]['w'])
    return lista

def ecuacion_vulnerabilidad(n):
    '''
    Esta función expresa la ecuación para el cálculo de la vulnerabilidad

    .. math::
        vulnerabilidad = \exp^{( 1 - sus)^{(1 + ca)}}


        | exp = Exposición
        | sus = Susceptibilidad
        | ca = Capacidad adaptativa

    :returns: str ecuacion
    '''
    if n==1:
        ecuacion = 'pow(A,(1-B))'
    if n==2:
        ecuacion = 'pow(pow(A,(1-B)),(1+C))'
    return ecuacion
def media_raster(path_raster):
    '''
    Esta función regresa el promedio de todos los pixeles válidos
    de un archivo raster

    :param path_raster: Ruta del archivo raster
    :type path_raster: String
    '''
    rlayer = qgis.core.QgsRasterLayer(path_raster,"raster")
    extent = rlayer.extent()
    provider = rlayer.dataProvider()
    stats = provider.bandStatistics(1,
                                    qgis.core.QgsRasterBandStats.All,
                                    extent,
                                    0)
    promedio = stats.mean
    return round(promedio,3)
def lista_criterios(dicc):
    '''
    Esta función regresa una lista de los criterios de un diccionario

    :param dicc: Diccionario que contiene nombres, rutas y pesos para el análisis de vulnerabilidad / sensibilidad
    :type dicc: diccionario python
    
    '''
    criterios = []
    for k1,v1 in dicc.items():
        for k2,v2, in v1['criterios'].items():
            elementos = list(v2.keys())
            if 'ruta' in elementos:
                criterios.append(k2)
            if 'criterios' in elementos:
                for k3,v3, in v2['criterios'].items():
                    elementos = list(v3.keys())
                    if 'ruta' in elementos:
                        criterios.append(k3)
                    if 'criterios' in elementos:
                        for k4,v4, in v3['criterios'].items():
                            elementos = list(v4.keys())
                            if 'ruta' in elementos:
                                criterios.append(k4)
                            if 'criterios' in elementos:
                                for k5,v5, in v4['criterios'].items():
                                    elementos = list(v5.keys())
                                    if 'ruta' in elementos:
                                        criterios.append(k5)
                        
    return criterios
def crea_capa(ecuacion,rasters_input,salida): 

    '''
    Esta función crea una capa mediante la calculadora raster
    de GDAL, esta función esta limitada hasta 14 variables en la ecuación.

    :param ecuacion: ecuación expresada en formato gdal,\
                    es este caso es la salida de la funcion *ecuacion_clp*
    :type ecuacion: String
    :param rasters_input: lista de los paths de los archivos rasters, salida de la función *separa_ruta_pesos*
    :type rasters_input: lista
    :param salida: ruta con extensión tiff de la salida
    :type salida: String
    '''
    path_A=''
    path_B=''
    path_C=''
    path_D=''
    path_E=''
    path_F=''
    path_G=''
    path_H=''  
    path_I=''
    path_J=''
    path_K=''
    path_L=''
    path_M=''
    path_N=''


    total_raster = len(rasters_input)
    
    for a,b in zip(range(total_raster), rasters_input):
        if a == 0:
            path_A=b
        elif a == 1:
            path_B=b
        elif a == 2:
            path_C=b
        elif a == 3:
            path_D=b
        elif a == 4:
            path_E=b
        elif a == 5:
            path_F=b
        elif a == 6:
            path_G=b
        elif a == 7:
            path_H=b
        elif a == 8:
            path_I=b
        elif a == 9:
            path_J=b
        elif a == 10:
            path_K=b
        elif a == 11:
            path_L=b
        elif a == 12:
            path_M=b
        elif a == 13:
            path_N=b



            
    if total_raster == 1:
        gdal_calc.Calc(calc=ecuacion, 
                            A=path_A, 
                            outfile=salida,
                            NoDataValue=-9999.0,
                            quiet=True)
                            
    if total_raster == 2:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)

    if total_raster == 3:
            gdal_calc.Calc(calc=ecuacion, 
                            A=path_A, 
                            B=path_B,
                            C=path_C, 
                            outfile=salida,
                            NoDataValue=-9999.0,
                            quiet=True)
                            
    if total_raster == 4:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        C=path_C, 
                        D=path_D,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)

    if total_raster == 5:
            gdal_calc.Calc(calc=ecuacion, 
                            A=path_A, 
                            B=path_B,
                            C=path_C, 
                            D=path_D,
                            E=path_E, 
                            outfile=salida,
                            NoDataValue=-9999.0,
                            quiet=True)
                            
    if total_raster == 6:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        C=path_C, 
                        D=path_D,
                        E=path_E, 
                        F=path_F,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)

    if total_raster == 7:
            gdal_calc.Calc(calc=ecuacion, 
                            A=path_A, 
                            B=path_B,
                            C=path_C, 
                            D=path_D,
                            E=path_E, 
                            F=path_F,
                            G=path_G, 
                            outfile=salida,
                            NoDataValue=-9999.0,
                            quiet=True)
                            
    if total_raster == 8:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        C=path_C, 
                        D=path_D,
                        E=path_E, 
                        F=path_F,
                        G=path_G, 
                        H=path_H,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)
        
    if total_raster == 9:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        C=path_C, 
                        D=path_D,
                        E=path_E, 
                        F=path_F,
                        G=path_G, 
                        H=path_H,
                        I=path_I,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)

    if total_raster == 10:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        C=path_C, 
                        D=path_D,
                        E=path_E, 
                        F=path_F,
                        G=path_G, 
                        H=path_H,
                        I=path_I,
                        J=path_J,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)

    if total_raster == 11:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        C=path_C, 
                        D=path_D,
                        E=path_E, 
                        F=path_F,
                        G=path_G, 
                        H=path_H,
                        I=path_I,
                        J=path_J,
                        K=path_K,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)

    if total_raster == 12:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        C=path_C, 
                        D=path_D,
                        E=path_E, 
                        F=path_F,
                        G=path_G, 
                        H=path_H,
                        I=path_I,
                        J=path_J,
                        K=path_K,
                        L=path_L,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)

    if total_raster == 13:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        C=path_C, 
                        D=path_D,
                        E=path_E, 
                        F=path_F,
                        G=path_G, 
                        H=path_H,
                        I=path_I,
                        J=path_J,
                        K=path_K,
                        L=path_L,
                        M=path_M,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)

    if total_raster == 14:
        gdal_calc.Calc(calc=ecuacion, 
                        A=path_A, 
                        B=path_B,
                        C=path_C, 
                        D=path_D,
                        E=path_E, 
                        F=path_F,
                        G=path_G, 
                        H=path_H,
                        I=path_I,
                        J=path_J,
                        K=path_K,
                        L=path_L,
                        M=path_M,
                        N=path_N,
                        outfile=salida,
                        NoDataValue=-9999.0,
                        quiet=True)


def ecuacion_clp(pesos):

    '''
    Esta función recibe una lista de pesos para regresar la ecuación
    en la estructura requerida por gdal para la combinación lineal ponderada.

    :param pesos: lista de los pesos de las capas, salida de la función *separa_ruta_pesos*
    :type pesos: lista
    '''
    n_variables=len(pesos)
    abc = list(string.ascii_uppercase)
    ecuacion = ''
    for a,b in zip(range(n_variables),pesos):
        
        if a < n_variables-1:
            ecuacion+= (str(b)+str(' * ')+str(abc[a])+' + ' )
        else:
            ecuacion+= (str(b)+str(' * ')+str(abc[a]))
    return ecuacion
def lista_pesos_ruta(dicc):
    '''
    Funcion para sacar listas por subcriterio
    '''
    exp_fis=[]
    exp_bio=[]
    sus_fis=[]
    sus_bio=[]
    pesos_1n = []
    for k1, v1 in dicc.items():

        for k2, v2 in v1['criterios'].items():
            pesos_1n.append(k1+"|"+str(v1['w'])+"|"+k2+"|"+str(v2['w']))
            for k3, v3 in v2['criterios'].items():
                if k1=='exposicion' and k2=='fisico':
                    exp_fis.append(v3['ruta'] + "|" + str(v3['w']))
                    #print (k1,v1['w'],k2,v2['w'],k3,v3['w'],v3['ruta'])
                elif k1=='exposicion' and k2=='biologico':
                    exp_bio.append(v3['ruta'] + "|" + str(v3['w']))
                    #print (k1,v1['w'],k2,v2['w'],k3,v3['w'],v3['ruta'])
                elif k1=='susceptibilidad' and k2=='fisico':
                    sus_fis.append(v3['ruta'] + "|" + str(v3['w']))
                    #print (k1,v1['w'],k2,v2['w'],k3,v3['w'],v3['ruta']
                elif k1=='susceptibilidad' and k2=='biologico':
                    sus_bio.append(v3['ruta'] + "|" + str(v3['w']))
                    #print (k1,v1['w'],k2,v2['w'],k3,v3['w'],v3['ruta']
    return exp_fis, exp_bio, sus_fis, sus_bio,pesos_1n

def separa_ruta_pesos(lista):
    rutas =[]
    pesos= []
    for capa in lista:
        rutas.append(capa.split("|")[0])
        pesos.append(capa.split("|")[1])
    return rutas,pesos


def rutas_pesos_globales(factor,dicc):
    lista = []   # se tiene que pasar a nivel recursiva 
    for k1, v1 in dicc[factor].items():
        if type(v1) is dict:
            for k2, v2 in v1.items(): # nivel de biologicos o fisico
                if type(v2) is dict: 
                    for k3,v3 in v2.items():
                        if type(v3) is dict: 
                             for k4,v4 in v3.items(): #k4 e sel nombre de los criterios  como v_acuatica_exp
                                elementos = list(v4.keys())
                                if 'ruta' in elementos:
                                    lista.append(v4['ruta']+"|"+str(v2['w']*v4['w']))
                                elif 'criterios' in elementos and  type(v4) is dict:
                                    for k5,v5, in v4.items():
                                        if type(v5) is dict:
                                            for k6,v6 in v5.items():
                                                elementos = list(v6.keys())
                                                if 'ruta' in elementos:
                                                    lista.append(v6['ruta']+"|"+str(v2['w']*v4['w']*v6['w']))
                                                elif 'criterios' in elementos and  type(v6) is dict:
                                                    for k7,v7, in v6.items():
                                                        if type(v7) is dict:
                                                            for k8,v8 in v7.items():
                                                                elementos = list(v8.keys())
                                                                if 'ruta' in elementos:
                                                                    lista.append(v8['ruta']+"|"+str(v2['w']*v4['w']*v6['w']*v8['w']))
    return lista


def find_key(d, key):

    for k,v in d.items():
        
        if isinstance(v, dict):
            p = find_key(v, key)
            if p:
                return [k] + p
        if k == key:
            return [k]
def quita(dicc,key):
    '''
    Esta función retira un elemento del diccionario y regresa un nuevo diccionario 
    sin dicho elemento <<dicc_q>>.

    :param dicc: Diccionario con la estructura requerida
    :type dicc: diccionario
    :param key: nombre de la variable a quitar
    :type key: String

    '''
    dicc_q = copy.deepcopy(dicc)

    niveles = find_key(dicc_q,key)

    if len(niveles)==1:
        dicc_q.pop(niveles[0])
    if len(niveles)==3:
        dicc_q[niveles[0]]['criterios'].pop(niveles[2])
        if len(dicc_q[niveles[0]]['criterios'])==0:
            dicc_q.pop(niveles[0])
    if len(niveles)==5:
        dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'].pop(niveles[4])
        if len(dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'])==0:
            dicc_q[niveles[0]]['criterios'].pop(niveles[2])
        if len(dicc_q[niveles[0]]['criterios'])==0:
            dicc_q.pop(niveles[0])
    if len(niveles)==7:
        dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'][niveles[4]]['criterios'].pop(niveles[6])
        if len(dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'][niveles[4]]['criterios'])==0:
            dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'].pop(niveles[4])
        if len(dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'])==0:
            dicc_q[niveles[0]]['criterios'].pop(niveles[2])
        if len(dicc_q[niveles[0]]['criterios'])==0:
            dicc_q.pop(niveles[0])
    if len(niveles)==9:
        dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'][niveles[4]]['criterios'][niveles[6]]['criterios'].pop(niveles[8])
        if len(dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'][niveles[4]]['criterios'][niveles[6]]['criterios'])==0:
            dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'][niveles[4]]['criterios'].pop(niveles[6])
        if len(dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'][niveles[4]]['criterios'])==0:
            dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'].pop(niveles[4])
        if len(dicc_q[niveles[0]]['criterios'][niveles[2]]['criterios'])==0:
            dicc_q[niveles[0]]['criterios'].pop(niveles[2])
        if len(dicc_q[niveles[0]]['criterios'])==0:
            dicc_q.pop(niveles[0])


    return dicc_q

    
def reescala(dicc_q):
    '''
    Esta función rescala un diccionario que se le a quitado un criterio
    y regresa el diccionario con los pesos rescalados

    :param dicc_q: salida de la función *quita* 
    
    '''

    dicc_r = copy.deepcopy(dicc_q)
    suma = 0
    for k1, v1 in dicc_r.items():
        suma += v1['w']
    for k1, v1 in dicc_r.items():
        v1['w'] = v1['w']/suma
        
    for k1, v1 in dicc_r.items():
        suma = 0
        elementos = list(v1.keys())
        if 'criterios' in elementos:
            for k2, v2 in v1['criterios'].items():
                suma += v2['w']
            for k2, v2 in v1['criterios'].items():
                v2['w'] = v2['w'] / suma
            
            
    for k1, v1 in dicc_r.items():
        elementos = list(v1.keys())
        if 'criterios' in elementos:
            for k2, v2 in v1['criterios'].items():      
                suma = 0
                elementos = list(v2.keys())
                if 'criterios' in elementos:
                    for k3, v3 in v2['criterios'].items():   
                        suma += v3['w']
                    for k3, v3 in v2['criterios'].items():
                        v3['w'] = v3['w'] / suma

    
    for k1, v1 in dicc_r.items():
        elementos = list(v1.keys())
        if 'criterios' in elementos:
            for k2, v2 in v1['criterios'].items():      
                elementos = list(v2.keys())
                if 'criterios' in elementos:
                    for k3, v3 in v2['criterios'].items():
                        suma = 0
                        elementos = list(v3.keys())
                        if 'criterios' in elementos:
                            for k4, v4 in v3['criterios'].items():   
                                suma += v4['w']
                            for k4, v4 in v3['criterios'].items():
                                v4['w'] = v4['w'] / suma

    for k1, v1 in dicc_r.items():
        elementos = list(v1.keys())
        if 'criterios' in elementos:
            for k2, v2 in v1['criterios'].items():      
                elementos = list(v2.keys())
                if 'criterios' in elementos:
                    for k3, v3 in v2['criterios'].items():
                        elementos = list(v3.keys())
                        if 'criterios' in elementos:
                            for k4, v4 in v3['criterios'].items():   
                                suma = 0
                                elementos = list(v4.keys())
                                if 'criterios' in elementos:
                                    for k5, v5 in v4['criterios'].items():   
                                        suma += v5['w']
                                    for k5, v5 in v4['criterios'].items():
                                        v5['w'] = v5['w'] / suma




    return dicc_r
    
def quita_reescala(dicc,key):
    '''
    Función que integra las funciones quita y reescala y regresa
    un diccionario sin la variable y con los pesos reescalados.
    
    :param dicc: Diccionario con la estructura requerida
    :type dicc: diccionario
    :param key: nombre de la variable a quitar
    :type key: String
    '''
    dicc_q = quita(dicc,key)
    dicc_r = reescala(dicc_q)
    return dicc_r
def pesos_superiores(dicc):
    pesos=[]
    for k1,v1 in dicc.items():
        #print (k1,v1['w'])
        pesos.append([k1,str(v1['w'])])
    return pesos 


def ideales(path_raster, path_raster_n):
    min,max = raster_min_max(path_raster)
    no_data =raster_nodata(path_raster)
    ec_norm ='(A' + ') / (' + str(max) +')'  # llevar a ideal 
    #ec_norm ='(A - '+str(min) + ') / (' + str(max)+'-'+str(min) +')'  # normalizar 
    dicc ={        
        'INPUT_A':path_raster,
        'BAND_A':1,
        'FORMULA':ec_norm,
        'NO_DATA': no_data,
        'RTYPE':5,
        'OUTPUT':path_raster_n}
    pr.run("gdal:rastercalculator",dicc)


def raster_nodata(path_raster):

    '''
    Esta función regresa el valor de NoData de una capa raster

    :param path_raster:  ruta de la capa raster
    :type path_raster: srt

    '''

    rlayer = QgsRasterLayer(path_raster,"raster")
    extent = rlayer.extent()
    

    provider = rlayer.dataProvider()
    rows = rlayer.rasterUnitsPerPixelY()
    cols = rlayer.rasterUnitsPerPixelX()
    block = provider.block(1, extent,  rows, cols)

    no_data = block.noDataValue()

    
    return no_data

def lineal_decreciente(path_raster, path_raster_n):
    '''
    Función de valor líneal decreciente

    '''
    min,max = raster_min_max(path_raster)
    no_data =raster_nodata(path_raster)
    xmax_menos_xmin = max-min
    xmax_menos_xmin_xmax = xmax_menos_xmin / max
    xmax_mas_xmin = max + min
    xmax_mas_xmin_xmax = xmax_mas_xmin / max

    ec_norm ='((-A * '+str(xmax_menos_xmin_xmax)+') / '+str(xmax_menos_xmin)+') + '+str(xmax_mas_xmin_xmax)  # llevar a ideal 
    
    dicc ={        
        'INPUT_A':path_raster,
        'BAND_A':1,
        'FORMULA':ec_norm,
        'NO_DATA': no_data,
        'RTYPE':5,
        'OUTPUT':path_raster_n}
    pr.run("gdal:rastercalculator",dicc)
