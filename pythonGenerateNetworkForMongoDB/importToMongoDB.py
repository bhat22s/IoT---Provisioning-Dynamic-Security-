# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:31:45 2020

@author: Chenjun Li
"""

from pymongo import MongoClient
import pandas as pd

# DB connectivity
client =MongoClient('localhost', 27017)
dblist = client.list_database_names()
if "cs682" in dblist:
    print("cs682 exist")
else:
    print("Need create cs682 database")

db = client.cs682
collection = db.devices

x = collection.delete_many({})
print(x.deleted_count, " documents deleted in devices.")
df = pd.read_csv("Devices.csv", na_filter=False)
records_ = df.to_dict(orient = 'records')
result = collection.insert_many(records_ )

df = pd.read_csv("Radio.csv", na_filter=False)
records_ = df.to_dict(orient = 'records')
result = collection.insert_many(records_ )

x = db.users.delete_many({})
print(x.deleted_count, " documents deleted in users.")

df = pd.read_csv("Users.csv", na_filter=False)
records_ = df.to_dict(orient = 'records')
result = db.users.insert_many(records_ )

x = db.proj_preferences.delete_many({})
print(x.deleted_count, " documents deleted in proj_preferences.")

df = pd.read_csv("Project.csv", na_filter=False)
records_ = df.to_dict(orient = 'records')
result = db.proj_preferences.insert_many(records_ )

x = db.result.delete_many({})
print(x.deleted_count, " documents deleted in result.")