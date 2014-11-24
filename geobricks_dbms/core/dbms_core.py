from geobricks_dbms.core.dbms_mongodb import DBMSMongoDB


class DBMS():

    # User's parameters.
    db_type = None
    db_name = None
    collection_name = None

    # Computed parameters
    mongodb = None

    def __init__(self, db_type, db_name, collection_name):

        # Store user's parameters.
        self.db_type = db_type
        self.db_name = db_name
        self.collection_name = collection_name

        # Connect to the DB
        self.connect()

    def connect(self):
        if 'mongodb' in self.db_type:
            self.mongodb = DBMSMongoDB(self.db_name, self.collection_name)

    def find(self):
        if 'mongodb' in self.db_type:
            return self.mongodb.find()

    def find_by_id(self, item_id):
        if 'mongodb' in self.db_type:
            return self.mongodb.find_by_id(item_id)

    def insert(self, item):
        if 'mongodb' in self.db_type:
            return self.mongodb.insert(item)


mydb = DBMS('mongodb', 'test', 'posts')
mydb.insert({"pippo": "pluto"})
for post in mydb.find():
    print post
print
for post in mydb.find_by_id('54730665f8cd671e687311e8'):
    print post