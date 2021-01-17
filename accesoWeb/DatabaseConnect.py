from pymongo import MongoClient, errors


# DEVUELVE LA CONEXION A LA BASE DE DATOS.
def getConnection(databaseName):
    mongoClient = MongoClient('localhost', port=27017)
    db = mongoClient[databaseName]
    return db
