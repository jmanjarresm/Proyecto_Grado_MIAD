# -*- coding: utf-8 -*-

import os
import re

import datetime as dt
import pandas as pd
import numpy as np


from pyod.models.iforest import IForest
from pyod.utils.data import generate_data


os.chdir(r'D:\01_MaestriaAnalitica_UnivAndes\13_Proyecto_ElectroDunas')

cwd = os.getcwd()


# =============================================================================
# Funciones
# =============================================================================

import pandas as pd

def crear_variables_tiempo(df, time_series):
    # Realiza una copia del DataFrame original
    df = df.copy()

    df[time_series] = pd.to_datetime(df[time_series])

    df['año'] = df[time_series].dt.year

    df['mes'] = df[time_series].dt.month

    df['trimestre'] = df[time_series].dt.quarter

    df['dia'] = df[time_series].dt.day

    df['hora'] = df[time_series].dt.hour

    # Extrae el día de la semana (0 = lunes, 6 = domingo)
    df['dia_semana'] = df[time_series].dt.dayofweek

    # Puedes agregar más desagregaciones si es necesario

    return df



def detertar_anomalias(X_train, X_test):   
    # Crea y entrena el modelo Isolation Forest
    model = IForest(contamination=0.1, random_state=42)
    model.fit(X_train)
    
    # Predice anomalías en los datos de prueba
    y_pred_test = model.predict(X_test)
    return y_pred_test
    


# listar los clientes:
  
lista_clientes = os.listdir(os.path.join(cwd,'GPA-Data-ElectroDunas'))

lista_clientes = [ele for ele in lista_clientes if re.search(r'csv',ele)]

base_clientes = []

for cliente in lista_clientes:
    reporte_cliente = pd.read_csv(os.path.join(cwd,'GPA-Data-ElectroDunas',cliente))
    reporte_cliente['id_cliente'] = re.search(r'CLIENTE[0-9]+',cliente).group(0)
    base_clientes.append(reporte_cliente)

base_clientes = pd.concat(base_clientes).reset_index(drop=True)

base_clientes['fecha_date'] =  pd.to_datetime(base_clientes['Fecha'])

base_clientes = crear_variables_tiempo(base_clientes, 'fecha_date')
base_clientes 


X_train = base_clientes[(base_clientes['hora']==10 ) & (base_clientes['dia_semana']==3) & (base_clientes['Fecha']!='2023-03-30 10:00:00')].reset_index(drop=True)
X_test = base_clientes[base_clientes['Fecha']=='2023-03-30 10:00:00'].reset_index(drop=True)
X_test.shape

anomalos = detertar_anomalias(X_train[['Active_energy', 'Reactive_energy', 'Voltaje_FA', 'Voltaje_FC']], X_test[['Active_energy', 'Reactive_energy', 'Voltaje_FA', 'Voltaje_FC']])
anomalos



