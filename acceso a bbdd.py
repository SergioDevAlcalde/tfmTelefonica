#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo
uri="mongodb://localhost:27017"
cx=pymongo.MongoClient(uri)
mndb = cx["BD_proyecto"]
mycol = mndb['bbdd2']
null = 'null' 


# In[2]:


for inst in mycol.aggregate([{ "$group": {"_id": null,"MaximumValue": { "$max": "$Date" }}}]):
    fecmax=inst ['MaximumValue']
print(fecmax) 


# In[3]:


list_emp = []
for inst in  mycol.distinct( "Desc" ) : 
    list_emp.append(inst) 
    
print(list_emp)    


# In[4]:


enum_emp = enumerate(list_emp)
for enum_emp in enumerate(list_emp):
    print(enum_emp)


# In[25]:


x=int(input("introduce número identificativo de criptomoneda de campo que quieres comparar==> "))
print(list_emp[x])
cryp = list_emp[x]


# In[26]:


datos=[]
#for inst in mycol.find({"Desc":list_emp[x]},{"_id": 0,"Date":1,"Close":1}):  
for inst in mycol.find({"Desc":list_emp[x]},{"_id": 0}):  
    datos.append(inst)
#    print(inst) 


# In[35]:


#datos
from pandas import DataFrame 
df_cryp = DataFrame (datos)
df_cryp.sort_values(by="Date", ascending=False)
df_cryp.head()


# In[36]:


df_cryp_cierre = df[["Date","Close"]]
df_cryp_cierre = df_cryp_cierre.rename(columns = {"Close" : "Close"+cryp})
df_cryp_cierre.set_index('Date', inplace = True)


# In[37]:


# a partir de aquí ya se puede acceder a código de Rubén, 
# cambiando btc_usd_cierre  por df_cryp_cierre
df_cryp_cierre.head()

