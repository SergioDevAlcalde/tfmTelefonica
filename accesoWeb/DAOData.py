import accesoWeb.DatabaseConnect as DatabaseConnect
from pymongo import MongoClient, errors


class DAOData:
    connection = ""
    collectionName = ""

    def setCollectionToUse(self):
        collection = self.connection[self.collectionName]
        return collection

    def __init__(self, databaseName):
        self.connection = DatabaseConnect.getConnection(databaseName)

    def saveManyData(self, collectionName, listToSave):
        collection = self.connection[collectionName[0]]
        collection.insert_many(listToSave.to_dict("records"))

    def getOneCollectionNoId(self, collectionName):
        collection = self.connection[collectionName]
        return collection.find({}, {"_id": 0})

    def getManyCollectionNoId(self, collectionsName):
        listToReturn = []
        for i in collectionsName:
            collection = self.connection[i]
            listToReturn.append(collection.find({}, {"_id": 0}))
        return listToReturn
