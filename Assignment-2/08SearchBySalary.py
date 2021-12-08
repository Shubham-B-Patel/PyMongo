from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

sal=float(input('Enter Salary : '))

qr={"salary": { "$gt" : sal}}

for doc in coll.find(qr):
    print(doc)