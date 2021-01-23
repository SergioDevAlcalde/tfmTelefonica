from pymongo import MongoClient, errors


# DEVUELVE LA CONEXION A LA BASE DE DATOS.
def getConnection(databaseName):
                                                        #THIS INFO IS TEMP
    mongoClient = MongoClient('localhost', port=27017, username ='root', password='1234')
    db = mongoClient[databaseName]
    return db
