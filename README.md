Geobricks DBMS
==============

This project provides DBMS functionalities to Geobricks modules, enabling CRUD methods for different types of DB (e.g. [PostgreSQL](http://www.postgresql.org/), [MongoDB](http://www.mongodb.org/), etc). The main script is ```dbms_core.py``` which acts as a generic gateway to the class that implements specific methods for each data source.

Installation
============

The plug-in is distributed through PyPi and can be installed by typing the following command in the console:
```
pip install geobricksdbms
```

Examples
========
The main class is ```DBMS``` contained in ```dbms_core.py```. The initialization method of such class accepts the following arguments:

|Name|Description|Default|Example|
|----|-----|-------|-------|
|```db_type```|DB connector to use||<ul><li>```mongodb```</li><li>```postgresql```</li></ul>|
|```db_name```|Name of the DB||my_db|
|```username```|Username to access the DB|```None```|my_username|
|```password```|Password to access the DB|```None```|my_password|
|```collection_name```|Name of the collection (MongoDB only)|```None```|my_collection|

Once initialized the ```DBMS``` class provides a set of CRUD methods as discussed in the following sections.

MongoDB
-------
The example below shows how to connect to the _test_ data source and to the _posts_ collection:
```python
my_db = DBMS('mongodb', 'test', collection_name='posts')
```
Once the connection has been estabilished it is possible to query the DB. The ```select_all``` method retrieves all the items of the collection:
```python
for row in my_db.select_all():
    print row
```
It is also possible to select a single item by ID:
```python
item = my_db.find_by_id('547305f8f8cd671df13e6765')
```
The ```insert``` method allows the user to add new documents in the collection:
```python
new_id = my_db.insert({'my_field': 'my_value'})
print new_id
```

PostgreSQL
----------
The example below shows how to connect to the _geobricks_ data source:
```python
my_db = DBMS('postgresql', 'geobricks', 'my_username', 'my_password')
```
Once the connection has been estabilished it is possible to query the DB. The ```select_all``` method retrieves all the items of the collection, and takes the table name as argument:
```python
for row in my_db.select_all('tasks'):
    print row
```
To insert a new item in the DB you will have to specify the table name and provide a ```Dict``` where the keys represents the column names and the values are the values to be stored in the DB. As istance the following code:
```python
my_db.insert({'year': '2014', 'month': '11'}, 'tasks')
```
add the following record in the _tasks_ table:

|year|month|day|hour|second|
|----|-----|---|----|------|
|2014|11||||

Only the fields specified in the ```Dict``` have been stored in the _tasks_ table.
