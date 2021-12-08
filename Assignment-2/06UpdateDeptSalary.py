from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

qr={}
id=input('Enter ID : ')
qr["_id"]=id

for doc in coll.find(qr):
    upd={}
    dept=input('Enter Department : ')
    city=input('Enter City : ')
    upd["dept"]=dept
    upd["city"]=city

    upddata={"$set":upd}
    coll.update_one(qr,upddata)
    print()
    print("Document Updated...")