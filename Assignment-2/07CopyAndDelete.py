from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll1=db["workers"]
coll2=db["exworkers"]

qr={}
id=input('Enter ID : ')
qr["_id"]=id

for doc in coll1.find(qr):
    coll2.insert_one(doc)
    coll1.delete_one(qr)
    print()
    print('Document copied to exworkers....')
    print('And deleted from workers')