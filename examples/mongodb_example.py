from geobricks_dbms.core.dbms_core import DBMS


# Connect to the DB.
my_db = DBMS('mongodb', 'test', collection_name='posts')

# Select all the items in the collection.
for row in my_db.select_all():
    print row

# Select a single item by ID.
item = my_db.find_by_id('547305f8f8cd671df13e6765')

# Insert a new item.
new_id = my_db.insert({'my_field': 'my_value'})
print new_id