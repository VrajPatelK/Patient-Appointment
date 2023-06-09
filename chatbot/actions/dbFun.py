import datetime
from pymongo import MongoClient

import certifi
import ssl

# mongodb+srv://gauravteli:gauravteli@cluster0.iykzyey.mongodb.net/?retryWrites=true&w=majority
DB_URL = "mongodb://localhost:27017"
# DB_URL = "mongodb+srv://gauravteli:gauravteli@cluster0.iykzyey.mongodb.net/?retryWrites=true&w=majority"

# adding not adding the security by Secure Socket Layer
client = MongoClient(DB_URL, ssl_cert_reqs=ssl.CERT_NONE)


print("connected successfully")

db = client["RasaDb"]

allCollection = ['dr1', 'dr2', 'dr3']
    

def saveNewAppointmentData(doc,collectionName=allCollection[0]):
    collection = db[collectionName]
    collection.insert_one(doc)
    return "data saved"


def getSingleAppointmentData(aid,collectionName=allCollection[0]):
    collection = db[collectionName]
    return collection.find_one({"_id": aid})


def updateStatus(aid, status,collectionName=allCollection[0]):
    collection = db[collectionName]
    collection.update_one({"_id": aid}, {"$set": {"status": status}})
