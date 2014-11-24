from geobricks_dbms.core.dbms_core import DBMS


# Connect to the DB.
my_db = DBMS('postgresql', 'geobricks', 'my_username', 'my_password')

# Select all the items in the collection.
for row in my_db.select_all('tasks'):
    print row

# Insert a new item.
my_db.insert({'year': '2014', 'month': '11'}, 'tasks')