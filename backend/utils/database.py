from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['cyber_incident_monitoring']

def insert_incident(data):
    db.incidents.insert_one(data)
