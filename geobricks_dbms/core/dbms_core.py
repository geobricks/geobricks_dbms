from geobricks_dbms.core.dbms_mongodb import DBMSMongoDB
from geobricks_dbms.core.dbms_postgresql import DBMSPostgreSQL


class DBMS():

    # User's parameters.
    db_type = None
    db_name = None
    username = None
    password = None
    collection_name = None

    # Computed parameters
    mongodb = None
    postgresql = None

    def __init__(self, db_type, db_name, username=None, password=None, collection_name=None):

        # Store user's parameters.
        self.db_type = db_type
        self.db_name = db_name
        self.username = username
        self.password = password
        self.collection_name = collection_name

        # Connect to the DB
        self.connect()

    def connect(self):
        if 'mongodb' in self.db_type:
            self.mongodb = DBMSMongoDB(self.db_name, self.collection_name)
        elif 'postgresql' in self.db_type:
            self.postgresql = DBMSPostgreSQL(self.db_name, self.username, self.password)

    def select_all(self, table_name=None):
        if 'mongodb' in self.db_type:
            return self.mongodb.find()
        elif 'postgresql' in self.db_type:
            return self.postgresql.select_all(table_name)

    def find_by_id(self, item_id):
        if 'mongodb' in self.db_type:
            return self.mongodb.find_by_id(item_id)

    def insert(self, item, table_name=None):
        if 'mongodb' in self.db_type:
            return self.mongodb.insert(item)
        if 'postgresql' in self.db_type:
            return self.postgresql.insert(table_name, item)