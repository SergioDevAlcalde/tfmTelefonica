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
mycol = mndb['bbdd2']
null = 'null' 


#Se leen los datos de yahoo
#este código puede lanzarse cada día o cada cierto tiempo (hasta 99 laborables) accediendo primero a la bbdd y 
# recuperando fecha máxima , incluir también la fecha máxima en la carga para tener datos consolidados

PeerCoin   = pd.read_html('https://finance.yahoo.com/quote/PPC-USD/history?p=PPC-USD')
Ripple     = pd.read_html('https://finance.yahoo.com/quote/XRP-USD/history?p=XRP-USD')
Litecoin   = pd.read_html('https://finance.yahoo.com/quote/LTC-USD/history?p=LTC-USD')
Dogecoin   = pd.read_html('https://finance.yahoo.com/quote/DOGE-USD/history?p=DOGE-USD') 
Ether      = pd.read_html('https://finance.yahoo.com/quote/ETH-USD/history?p=ETH-USD')
Miota      = pd.read_html('https://finance.yahoo.com/quote/MIOTA-USD/history?p=MIOTA-USD')
Neo        = pd.read_html('https://finance.yahoo.com/quote/NEO-USD/history?p=NEO-USD')
Monero     = pd.read_html('https://finance.yahoo.com/quote/XMR-USD/history?p=XMR-USD')
Cardano    = pd.read_html('https://finance.yahoo.com/quote/ADA-USD/history?p=ADA-USD')
Nem        = pd.read_html('https://finance.yahoo.com/quote/XEM-USD/history?p=XEM-USD')
Dash       = pd.read_html('https://finance.yahoo.com/quote/DASH-USD/history?p=DASH-USD') 


cotz = [['PeerCoin',PeerCoin], 
        ['Ripple',Ripple],   
        ['Litecoin',Litecoin], 
        ['Dogecoin',Dogecoin], 
        ['Ether',Ether],    
        ['Miota',Miota],    
        ['Neo',Neo],      
        ['Monero',Monero],   
        ['Cardano',Cardano],  
        ['Nem',Nem],      
        ['Dash',Dash]]  

    

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
        mycol.delete_one(borrado)
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
                ins = mycol.insert_many([dic]) 
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 

 

q_fmax=[{ "$group": {"_id": null,"MaximumValue": { "$max": "$Date" }}}]


fecmax= buscar_fecmax(q_fmax)
print(fecmax)

borrado = { "Date": fecmax }
del_cotz = borrar_fecmax(borrado) 

for i in cotz:  
    lista_carga = cotz[n][1]
    df_carga= lista_carga[0]
    df_carga['Desc']= cotz[n][0] 
    carga=update_bbdd1(df_carga)
    n += 1