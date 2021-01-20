import pandas as pd
from pandas import DataFrame
import numpy as np

from accesoWeb.DAOData import DAOData


def getDataByOneCollection(databaseName, collectionName):
    database = DAOData(databaseName)
    recoverList = database.getOneCollectionNoId(collectionName)
    return DataFrame(recoverList)


# def getDataManyCollection():
#     database = DAOData("tfmlTelefonica")
#     collectionsName = ["Amazon"]
#     recoverList = database.getManyCollectionNoId(collectionsName)
#     arrayToDataset = np.array(recoverList)
#     return DataFrame(arrayToDataset)


# print(getDataByOneCollection("tfmTelefonica","Amazon"))
# print(getDataManyCollection())
