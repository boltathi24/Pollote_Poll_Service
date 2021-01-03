from pymongo import MongoClient
import urllib

mongo_uri = urllib.parse.quote("mongodb+srv://boltathi24:ZohoTest@24cluster0.xckok.mongodb.net")
myclient = MongoClient(mongo_uri)

mydb = myclient["pollote"]


