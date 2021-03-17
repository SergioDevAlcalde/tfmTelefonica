# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:20:25 2021

@author: jogar
"""

import pandas as pd
from pandas import DataFrame


# proceso de carga inicial
def carga_datos(fichero, empresa):
    carga = pd.read_csv(ruta + fichero)
    # carga['Desc'] = empresa
    carga.insert(0, "Company", empresa)
    return carga


ruta = r"D:\proyectos\masterBigData\TFM\cogidoProyecto\tfmTelefonica\cargaInicial"

bitcoin_eur = '\\BTC_EUR.csv'
bitcoin_usd = '\\BTC_USD.csv'
amazon = '\\AMZN.csv'
facebook = '\\FB.csv'
google = '\\GOOG.csv'
microsoft = '\\MSFT.csv'

lista = [bitcoin_eur, bitcoin_usd, amazon, facebook, google, microsoft]
empresa = ['Bitcoin_EUR', 'Bitcoin_USD', 'Amazon', 'Facebook', 'Google', 'Microsoft']
carga_lista = []


from old.accesoWeb.DAOData import DAOData

database = DAOData("tfmTelefonica")

n = 0
for i in lista:
    carga = carga_datos(lista[n], empresa[n])
    carga_lista.append(carga)

    df = DataFrame(carga)
    df.columns = ['Company', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    # ESTO TENDRIA QUE SER LA LLAMADA A UN DAO.
    database.saveManyData(empresa[n], df)
    n += 1

print(carga_lista)
