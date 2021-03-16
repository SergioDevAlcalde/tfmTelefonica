# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:42:39 2021

@author: jogar
"""

import csv
import pandas as pd
import numpy as np
import pymongo

#proceso de carga inicial
def carga_datos(fichero,empresa): 
    with open( (ruta + fichero)   ) as File:
        reader = csv.DictReader(File) 
        p=0
        for row in reader: 
            row['Desc'] = empresa  
            if p==0:
                print(row)
                print('*** primera línea*****')
            cotz.append(row) 
            p +=1
        print(row)
        print('*** útima línea*****')
        return(cotz)

ruta = r"C:\Users\jogar\Desktop\Big Data\PROYECTO\cotz"
#bitcoin_eur = '\\BTC_EUR.csv' 
#bitcoin_usd = '\\BTC_USD.csv'
bitcoin = '\\BTC_USD.csv'
amazon = '\\AMZN.csv'
facebook = '\\FB.csv'
google = '\\GOOG.csv'
microsoft = '\\MSFT.csv'

uri="mongodb://localhost:27017"
cx=pymongo.MongoClient(uri)
mndb = cx["BD_proyecto"]
mycol = mndb['bbdd1']
cotz = [] 

#lista = [bitcoin_eur,bitcoin_usd,amazon,facebook,google,microsoft] 
#empresa = ['Bitcoin EUR','Bitcoin USD','Amazon','Facebook','Google','Microsoft']
lista = [bitcoin,amazon,facebook,google,microsoft] 
empresa = ['BTC_USD','AMZN','FB','GOOG','MSFT']
n=0
m=len(lista)   
 
for i in range(n, m): 
    print(n,m)
    print(empresa[n]) 
    x=carga_datos(lista[n],empresa[n])  
    n += 1
    
#instrucción de carga
ins = mycol.insert_many(cotz)