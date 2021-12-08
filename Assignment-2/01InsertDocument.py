from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=input('Enter Workers ID : ')
nm=input('Name : ')
age=int(input('Age : '))
gen=input('Gender : ')
dept=input('Department : ')
post=input('Post : ')
city=input('City : ')
sal=float(input('Salary : '))
mob=input('Mobile No. : ')
email=input('Email : ')

dic={}
dic["_id"]=id
dic["empnm"]=nm
dic["age"]=age
dic["gender"]=gen
dic["dept"]=dept
dic["post"]=post
dic["city"]=city
dic["salary"]=sal
dic["mobile"]=mob
dic["email"]=email

coll.insert_one(dic)
print('-'*50)
print('New document added to workers collection')