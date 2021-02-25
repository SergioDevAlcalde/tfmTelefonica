# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:22:37 2021

@author: jogar
"""


# cambio fecha a YYYY-MM-DD
def formato_fecha(fecha_amer):
    meses = {'Jan': '-01-', 'Feb': '-02-', 'Mar': '-03-', 'Apr': '-04-', 'May': '-05-', 'Jun': '-06-',
             'Jul': '-07-', 'Aug': '-08-', 'Sep': '-09-', 'Oct': '-10-', 'Nov': '-11-', 'Dec': '-12-'}
    fec_amd = (fecha_amer[2] + meses[fecha_amer[0]] + fecha_amer[1].strip(','))
    return fec_amd


# proceso de carga inicial
def carga_datos(fichero, cotz):
    nombreEmpresa = []
    fecha = []
    abrir = []
    maximo = []
    minimo = []
    cierre = []
    cier_ajus = []
    volumen = []
    for x in range(0, 100):
        fec_amd = formato_fecha(fichero[0]['Date'][x].split())
        fecha.append(fec_amd)
        abrir.append(fichero[0]['Open'][x])
        maximo.append(fichero[0]['High'][x])
        minimo.append(fichero[0]['Low'][x])
        cierre.append(fichero[0]['Close*'][x])
        cier_ajus.append(fichero[0]['Adj Close**'][x])
        volumen.append(fichero[0]['Volume'][x])
        nombreEmpresa.append(cotz[0])

    lista = [nombreEmpresa, fecha, abrir, maximo, minimo, cierre, cier_ajus, volumen]
    return lista


import pandas as pd
# Se leen los datos de yahoo
from pandas import DataFrame

# este código puede lanzarse cada día o cada cierto tiempo (hasta 99 laborables) accediendo primero a la bbdd y
# recuperando fecha máxima
# bitcoin_eur=pd.read_html('https://es.finance.yahoo.com/quote/BTC-EUR/history?p=BTC-EUR')
bitcoin_eur = pd.read_html('https://finance.yahoo.com/quote/BTC-EUR/history?p=BTC-EUR')
bitcoin_usd = pd.read_html('https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD')
amazon = pd.read_html('https://finance.yahoo.com/quote/AMZN/history?p=AMZN')
facebook = pd.read_html('https://finance.yahoo.com/quote/FB/history?p=FB')
google = pd.read_html('https://finance.yahoo.com/quote/GOOG/history?p=GOOG')
microsoft = pd.read_html('https://finance.yahoo.com/quote/MSFT/history?p=MSFT')

cotz = [['Bitcoin_EUR', bitcoin_eur],
        ['Bitcoin_USD', bitcoin_usd],
        ['Amazon', amazon],
        ['Facebook', facebook],
        ['Google', google],
        ['Microsoft', microsoft]]

from accesoWeb.DAOData import DAOData

database = DAOData("tfmTelefonica")

n = 0
for i in cotz:
    lista = carga_datos(cotz[n][1], cotz[n])
    df = DataFrame(lista).transpose()
    df.columns = ['Company', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    # ESTO TENDRIA QUE SER LA LLAMADA A UN DAO.
    database.saveManyData(cotz[n][0], df)
    n = n + 1

print("save its ok")
