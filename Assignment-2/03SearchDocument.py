from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=input('Enter Workers ID : ')
qr={}
qr["_id"]=id

for doc in coll.find(qr):
    print(doc)