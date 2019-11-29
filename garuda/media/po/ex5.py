#Finding one document from the collection, find_one

import pymongo

from pymongo import MongoClient
client=MongoClient()
dbs=client.database_names()
db=client.pyex #db pyex
#db.pycoll.insert({'a':1,"b":2,"c":3}) #inserting a doc in to collection pycoll
s=db.pycoll.find_one({"a":1})
print (s)
s=db.pycoll.find_one({})
print (s)

