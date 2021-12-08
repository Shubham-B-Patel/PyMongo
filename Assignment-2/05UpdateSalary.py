from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

qr={}
id=input('Enter ID : ')
qr["_id"]=id

for doc in coll.find(qr): 
    val={}
    sal=float(input('Enter New Salary : '))
    val["salary"]=sal

    upd={"$set":val}
    coll.update_one(qr,upd)
    print()
    print("Document Updated...")
    print()
    for doc in coll.find(qr):
        print(doc)