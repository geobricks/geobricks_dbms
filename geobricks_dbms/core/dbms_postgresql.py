import simplejson
import psycopg2
from types import DictType


class DBMSPostgreSQL:

    # User's parameters
    db_name = None
    username = None
    password = None
    host = None
    port = None
    schema = None

    # Computed variables.
    connection = None

    def __init__(self, db_name, username, password, host='localhost', port=5432, schema="public"):

        # Store user parameters.
        self.db_name = db_name
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.schema = schema

        # Connect to the DB
        self.connect()

    def __init__(self, db_settings):

        # Store user parameters.
        self.db_name = db_settings["dbname"]
        self.username = db_settings["username"]
        self.password = db_settings["password"]
        self.host = "localhost" if "host" not in db_settings else db_settings["host"]
        self.port = 5432 if "port" not in db_settings else db_settings["port"]
        self.schema = "public" if "schema" not in db_settings else db_settings["schema"]

        # Connect to the DB
        self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(self.get_connection_string())
            self.connection.autocommit = True

            # set search_path to a specific schema
            if self.schema is not "public" and self.schema is not None:
                search_path = "SET search_path TO %s, public" % self.schema
                self.connection.cursor().execute(search_path)
                self.connection.commit()
        except Exception, e:
            raise Exception('Unable to connect to the DB. ' + str(e))

    def query(self, sql, output_json=False):
        if self.check_query(sql):
            cur = self.connection.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            if output_json:
                return simplejson.dumps(rows)
            return rows
        else:
            raise Exception("Query not allowed: " + sql)

    def query_extented(self, select, table, where, output_json=False):
        sql = "SELECT " + select + " FROM " + table
        if where is not None:
            sql += " WHERE " + where
        if self.check_query(sql):
            cur = self.connection.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            if output_json:
                return simplejson.dumps(rows)
            return rows
        else:
            raise Exception("Query not allowed: " + sql)

    def select_all(self, table_name, output_json=False):
        cur = self.connection.cursor()
        cur.execute('SELECT * FROM ' + table_name)
        rows = cur.fetchall()
        if output_json:
            return simplejson.dumps(rows)
        return rows

    def select_by_id(self, table_name, item_id, output_json=False):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM " + table_name + " WHERE id = '" + item_id + "' ")
        rows = cur.fetchall()
        if output_json:
            return simplejson.dumps(rows)
        return rows

    def select_by_field(self, table_name, field_name, field_value, output_json=False):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM " + table_name + " WHERE " + field_name + " = '" + field_value + "' ")
        rows = cur.fetchall()
        if simplejson:
            return simplejson.dumps(rows)
        return rows

    def insert(self, table_name, item):
        sql = ''
        if type(item) is DictType:
            sql += "INSERT INTO " + table_name + " ("
            for key in item:
                sql += key + ','
            sql = sql[0:len(sql) - 1]
            sql += ") VALUES ("
            for key in item:
                sql += "'" + item[key] + "',"
            sql = sql[0:len(sql) - 1]
            sql += ")"
        else:
            sql = item
        cur = self.connection.cursor()
        return cur.execute(sql)

    def get_connection_string(self, add_pg=False):
        db_connection_string = ""
        if add_pg is True:
            db_connection_string += "PG:"
            db_connection_string += "schemas='public,%s' " % self.schema
        db_connection_string += "host='%s' port=%s dbname='%s' user='%s' password='%s'" % (self.host, self.port, self.db_name, self.username, self.password)
        return db_connection_string

    # blacklist methods not allowed
    def check_query(self, query):
        q = query.lower()
        if "insert" in q or "update" in q or "delete" in q:
            return False
        return True

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()

    def __del__(self):
        self.close_connection()

    def __exit__(self):
        self.close_connection()