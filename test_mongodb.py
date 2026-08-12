from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://aswin_surya:<password>@aswinsurya.bnm3d5g.mongodb.net/?appName=Aswinsurya"

client = MongoClient(uri, server_api=ServerApi("1"))

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)