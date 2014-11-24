from pymongo import MongoClient
from bson.objectid import ObjectId


class DBMSMongoDB():

    # User's parameters
    host = None
    port = None
    db_name = None
    collection_name = None

    # Computed variables.
    client = None
    db = None
    collection = None

    def __init__(self, db_name, collection_name, host='localhost', port=27017):

        # Store user's settings
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name

        # Connect to the DB
        self.connect()

    def connect(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def insert(self, item):
        return self.collection.insert(item)

    def find(self):
        return self.collection.find()

    def find_by_id(self, item_id):
        return self.collection.find({"_id": ObjectId(item_id)})