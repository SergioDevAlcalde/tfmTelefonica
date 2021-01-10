# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:20:25 2021

@author: jogar
"""

import pandas as pd


# proceso de carga inicial
def carga_datos(fichero, empresa):
    carga = pd.read_csv(ruta + fichero)
    carga['Desc'] = empresa
    return carga


ruta = r"C:\Users\jogar\Downloads"

bitcoin_eur = '\\BTC_EUR.csv'
bitcoin_usd = '\\BTC_USD.csv'
amazon = '\\AMZN.csv'
facebook = '\\FB.csv'
google = '\\GOOG.csv'
microsoft = '\\MSFT.csv'

lista = [bitcoin_eur, bitcoin_usd, amazon, facebook, google, microsoft]
empresa = ['Bitcoin EUR', 'Bitcoin USD', 'Amazon', 'Facebook', 'Google', 'Microsoft']
carga_lista = []

n = 0
for i in lista:
    carga = carga_datos(lista[n], empresa[n])
    carga_lista.append(carga)
    n += 1

print(carga_lista)