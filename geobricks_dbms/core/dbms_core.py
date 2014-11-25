from geobricks_dbms.core.dbms_mongodb import DBMSMongoDB
from geobricks_dbms.core.dbms_postgresql import DBMSPostgreSQL
from geobricks_dbms.config.dbms_config import config


class DBMS():

    # User's parameters.
    vendor = None
    db_name = None
    username = None
    password = None
    collection_name = None
    datasource = None

    # Computed parameters
    mongodb = None
    postgresql = None

    def __init__(self, vendor=None, db_name=None, datasource=None, username=None, password=None, collection_name=None):

        # Store user's parameters.
        self.vendor = vendor
        self.db_name = db_name
        self.username = username
        self.password = password
        self.collection_name = collection_name
        self.datasource = datasource

        # Connect to the DB
        self.connect()

    def connect(self):

        # Check whether the user provided the name of a specific datasource
        if self.datasource is not None:

            # Read the default datasource
            default = config['default_datasource']
            self.vendor = default['vendor']

            # Connect to PostgreSQL default datasource
            if 'postgresql' in self.vendor:

                # Find the datasource specified by the user by datasource name
                tmp = DBMSPostgreSQL(default['db_name'], default['username'], default['password'])
                sql = "SELECT * FROM " + default['table_name'] + " WHERE datasource = '" + self.datasource + "' "
                ds = tmp.query(sql)
                self.vendor = ds[0][2]

                # Connect to the datasource specified by the user
                if 'postgresql' in ds[0][2]:
                    self.postgresql = DBMSPostgreSQL(ds[0][3], ds[0][4], ds[0][5])
                elif 'mongodb' in ds[0][2]:
                    self.mongodb = DBMSMongoDB(ds[0][3], ds[0][6])

            # Connect to MongoDB default datasource
            elif 'mongodb' in self.vendor:

                # Find the datasource specified by the user by datasource name
                tmp = DBMSMongoDB(default['db_name'], default['collection'])
                sql = {'datasource': self.datasource}
                ds = tmp.find(sql)
                self.vendor = ds[0]['vendor']

                # Connect to the datasource specified by the user
                if 'postgresql' in ds[0]['vendor']:
                    self.postgresql = DBMSPostgreSQL(ds[0]['db_name'], ds[0]['username'], ds[0]['password'])
                elif 'mongodb' in ds[0]['vendor']:
                    self.mongodb = DBMSMongoDB(ds[0]['db_name'], ds[0]['collection'])

        # Check whether the user provided the parameters of the datasource
        else:

            # Connect to MongoDB
            if 'mongodb' in self.vendor:
                self.mongodb = DBMSMongoDB(self.db_name, self.collection_name)

            # Connect to PostgreSQL
            elif 'postgresql' in self.vendor:
                self.postgresql = DBMSPostgreSQL(self.db_name, self.username, self.password)

    def find_all(self, table_name=None):
        if 'mongodb' in self.vendor:
            return self.mongodb.find({})
        elif 'postgresql' in self.vendor:
            return self.postgresql.select_all(table_name)

    def find_by_id(self, item_id, table_name=None):
        if 'mongodb' in self.vendor:
            return self.mongodb.find_by_id(item_id)
        elif 'postgresql' in self.vendor:
            return self.postgresql.select_by_id(table_name, item_id)

    def find_by_field(self, field_name, field_value, table_name=None):
        if 'mongodb' in self.vendor:
            return self.mongodb.find_by_field(field_name, field_value)
        elif 'postgresql' in self.vendor:
            return self.postgresql.select_by_field(table_name, field_name, field_value)

    def insert(self, item, table_name=None):
        if 'mongodb' in self.vendor:
            return self.mongodb.insert(item)
        elif 'postgresql' in self.vendor:
            return self.postgresql.insert(table_name, item)

    def query(self, query):
        if 'postgresql' in self.vendor:
            return self.postgresql.query(query)
        elif 'mongodb' in self.vendor:
            return self.mongodb.find(query)