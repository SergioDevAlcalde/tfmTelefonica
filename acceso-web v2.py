# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 20:18:24 2021

@author: jogar
"""

import pymongo
import pandas as pd


uri="mongodb://localhost:27017"
cx=pymongo.MongoClient(uri)
mndb = cx["BD_proyecto"]
mycol = mndb['bbdd1']
null = 'null' 

#Se leen los datos de yahoo
#este código puede lanzarse cada día o cada cierto tiempo (hasta 99 laborables) accediendo primero a la bbdd y 
# recuperando fecha máxima , incluir también la fecha máxima en la carga para tener datos consolidados
bitcoin_eur=pd.read_html('https://finance.yahoo.com/quote/BTC-EUR/history?p=BTC-EUR')
bitcoin_usd=pd.read_html('https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD') 
amazon=pd.read_html('https://finance.yahoo.com/quote/AMZN/history?p=AMZN') 
facebook=pd.read_html('https://finance.yahoo.com/quote/FB/history?p=FB') 
google=pd.read_html('https://finance.yahoo.com/quote/GOOG/history?p=GOOG') 
microsoft=pd.read_html('https://finance.yahoo.com/quote/MSFT/history?p=MSFT') 

cotz = [['Bitcoin EUR',bitcoin_eur],
        ['Bitcoin USD',bitcoin_usd],
        ['Amazon',amazon],
        ['Facebook', facebook],
        ['Google',google],
        ['Microsoft', microsoft]]   
    

n=0
columnas = ['Date', 'Open', 'High','Low','Close','Adj Close','Volume','Desc']

#recupero fecha de última cotización
def buscar_fecmax(query_fecha):
    for inst in mycol.aggregate([{ "$group": {"_id": null,"MaximumValue": { "$max": "$Date" }}}]):
        fecmax=inst ['MaximumValue'] 
        return fecmax   


# borro datos de última cotización para volver a cargarlos con datos consolidados
# puede que el último día de carga no se hubiera cerrado cotización
def borrar_fecmax(borrado): 
    for caso in mycol.find(borrado):
        print(caso) 
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
#        mycol.delete_one(borrado)
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    

#cambio fecha a YYYY-MM-DD
def formato_fecha(fecha_amer): 
    meses = {'Jan':'-01-', 'Feb':'-02-', 'Mar':'-03-', 'Apr':'-04-', 'May':'-05-', 'Jun':'-06-',
             'Jul':'-07-', 'Aug':'-08-', 'Sep':'-09-', 'Oct':'-10-', 'Nov':'-11-', 'Dec':'-12-'}
    fec_amd=(fecha_amer[2]+meses[fecha_amer[0]]+fecha_amer[1].strip(',')) 
    return fec_amd

def update_bbdd1(datos):
    for indice_fila, fila in df_carga.iterrows():
        dic = dict(zip(columnas,fila))
        fecha = dic['Date']
        if fecha[0] != '*':
            fec_amd = formato_fecha(dic['Date'].split()) 
            if fec_amd >= fecmax: 
                dic['Date']=fec_amd
                print(dic)
                print(sep)
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
#                ins = mycol.insert_many([dic]) 
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 

 

q_fmax=[{ "$group": {"_id": null,"MaximumValue": { "$max": "$Date" }}}]


fecmax= buscar_fecmax(q_fmax)
print(fecmax)

borrado = { "Date": fecmax }
del_cotz = borrar_fecmax(borrado)
sep='*********************************'

for i in cotz: 
    print('pasada '+ str(n))
    lista_carga = cotz[n][1]
    df_carga= lista_carga[0]
    df_carga['Desc']= cotz[n][0] 
    carga=update_bbdd1(df_carga)
    n += 1