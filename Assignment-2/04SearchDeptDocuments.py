from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

dept=input('Enter Department : ')

qr={}
qr["dept"]=dept

for doc in coll.find(qr):
    print(doc)