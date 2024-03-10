import numpy as np 
import pandas as pd 

def object_float_injuve(df):
    for columna in df.iloc[:,1:]:
        df[columna] = df[columna].str.replace('.','').str.replace(',','.').astype(float)
    return df

def injuve(t1,t2,t3,t4):
    lista_df = [t1,t2,t3,t4]
    for archivo in lista_df:
        if '1T' in archivo:
            trimestre1 = pd.read_csv(('./data/'+ archivo + '.csv'), sep=';', encoding='latin-1').iloc[[1,5,9,13,17],0:2]
        elif '2T' in archivo:
            trimestre2 = pd.read_csv(('./data/'+ archivo + '.csv'), sep=';', encoding='latin-1').iloc[[1,5,9,13,17],1:2]
        elif '3T' in archivo:
            trimestre3 = pd.read_csv(('./data/'+ archivo + '.csv'), sep=';', encoding='latin-1').iloc[[1,5,9,13,17],1:2]
        else:
            trimestre4 = pd.read_csv(('./data/'+ archivo + '.csv'), sep=';', encoding='latin-1').iloc[[1,5,9,13,17],1:2]
    df = pd.concat([trimestre1,trimestre2,trimestre3,trimestre4], axis=1)
    df = object_float_injuve(df)
    return df

def injuve_diez_años(t114,t214,t314,t414,t115,t215,t315,t415,t116,t216,t316,t416,t117,t217,t317,t417,t118,t218,t318,t418,
                 t119,t219,t319,t419,t120,t220,t320,t420,t121,t221,t321,t421,t122,t222,t322,t422,t123,t223,t323,t423):
    injuve_2014 = injuve(t114,t214,t314,t414)
    injuve_2015 = (injuve(t115,t215,t315,t415)).iloc[:,1:]
    injuve_2016 = (injuve(t116,t216,t316,t416)).iloc[:,1:]
    injuve_2017 = (injuve(t117,t217,t317,t417)).iloc[:,1:]
    injuve_2018 = (injuve(t118,t218,t318,t418)).iloc[:,1:]
    injuve_2019 = (injuve(t119,t219,t319,t419)).iloc[:,1:]
    injuve_2020 = (injuve(t120,t220,t320,t420)).iloc[:,1:]
    injuve_2021 = (injuve(t121,t221,t321,t421)).iloc[:,1:]
    injuve_2022 = (injuve(t122,t222,t322,t422)).iloc[:,1:]
    injuve_2023 = (injuve(t123,t223,t323,t423)).iloc[:,1:]
    injuve_diez_años = pd.concat([injuve_2014,injuve_2015,injuve_2016,injuve_2017,injuve_2018,
                              injuve_2019,injuve_2020,injuve_2021,injuve_2022,injuve_2023], axis=1)
    injuve_diez_años=injuve_diez_años.set_index(injuve_diez_años.iloc[:,0])
    injuve_diez_años=injuve_diez_años.drop(columns='JÓVENES DE 16 A 29 AÑOS EN LA EPA')
    return injuve_diez_años

def precios_alquiler(archivo):
    precios_alquiler = pd.read_csv(('./data/'+ archivo + '.csv'), sep=';', encoding='latin-1')
    for columna in precios_alquiler.iloc[:,1:]:
        precios_alquiler[columna] = precios_alquiler[columna].str.replace('/m2','').str.replace('%','').str.replace(',','.').astype(float)
    return precios_alquiler

def distribucion_salarial(dist1,dist2,dist3,dist4,dist5,dist6):
    lista_distribucion_salarial = [dist1,dist2,dist3,dist4,dist5,dist6]
    lista_concat = []
    for archivo in lista_distribucion_salarial:
        if 'mediana' in archivo:
            distribuion_salarial = (pd.read_csv(('./data/'+ archivo + '.csv'), sep=';', encoding='latin-1')).iloc[:,3:]
            distribuion_salarial['Total'] = distribuion_salarial['Total'].str.replace('.','').str.replace(',','.').astype(float)
            distribuion_salarial = distribuion_salarial.rename(columns={'Total': archivo})
            lista_concat.append(distribuion_salarial)
        elif 'mediana' not in archivo:
            distribuion_salarial = (pd.read_csv(('./data/'+ archivo + '.csv'), sep=';', encoding='latin-1')).iloc[:,3:]
            distribuion_salarial['Total'] = distribuion_salarial['Total'].str.replace('.','').str.replace(',','.').astype(float)
            distribuion_salarial = distribuion_salarial.drop(columns=['Periodo'])
            distribuion_salarial = distribuion_salarial.rename(columns={'Total': archivo})
            lista_concat.append(distribuion_salarial)
    df = pd.concat(lista_concat, axis=1)
    return df

def variacion_salario_ipc(archivo):
    variacion_salario_ipc = pd.read_csv(('./data/'+ archivo + '.csv'), sep=';').iloc[5:,:]
    variacion_salario_ipc = (variacion_salario_ipc.drop(columns=['Periodo'])).set_index('Año')
    for columna in variacion_salario_ipc:
        variacion_salario_ipc[columna] = variacion_salario_ipc[columna].str.replace('.','').str.replace(',','.').astype(float)
    return variacion_salario_ipc

def vut(archivo):
    vut = pd.read_csv(('./data/'+ archivo + '.csv'), sep=';', encoding='latin-1')
    vut = vut.set_index('CIUDADES')
    for columna in vut.iloc[:,:-1]:
        vut[columna] = vut[columna].str.replace(',','').astype(float)
    vut.iloc[:,-1] = vut.iloc[:,-1].str.replace(',','.').astype(float)
    return vut