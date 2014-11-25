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
|```datasource```|Name of a default datasource.|```None```|```my_datasource```||
|```vendor```|DB connector to use|```None```|<ul><li>```mongodb```</li><li>```postgresql```</li></ul>|
|```db_name```|Name of the DB|```None```|my_db|
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
Once the connection has been estabilished it is possible to query the DB. The ```find_all``` method retrieves all the items of the collection:
```python
for row in my_db.find_all():
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
Once the connection has been estabilished it is possible to query the DB. The ```find_all``` method retrieves all the items of the collection, and takes the table name as argument:
```python
for row in my_db.find_all('tasks'):
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

Connect by datasource name
--------------------------
It is possible to connect to a default datasource with no need to send the parameters to the init function. This is particularly useful when the DB must be accessed through the REST services and it is not safe, ot at least not recomendable, to embed usernames and/or password in the URL's. Available datasources are stored in a default DB that is configured in the ```config/dbms_config.py``` file. The default datasource can be PostgreSQL, MongoDB or any vendor supported by Geobricks DBMS. The following example shows the configuration for a PostgreSQL default DB:
```python
config = {
    "default_datasource": {
        "vendor": "postgresql",
        "db_name": "my_db",
        "table_name": "datasources",
        "username": "my_username",
        "password": "my_password"
    }
}
```
These are the required field to configure a PostgreSQL default datasource:

|Field Name|Field Description|Example|
|----------|-----------------|-------|
|```vendor```|Database vendor|```postgresql```|
|```db_name```|Name of the DB for the connection|```my_db```|
|```table_name```|Name of the table containing the default datasources|```datasources```|
|```username```|Username for the connection|```my_username```|
|```password```|Password for the connection|```my_password```|

Following an example for the configuration of a MongoDB default datasource:
```python
config = {
    "default_datasource": {
        "vendor": "mongodb",
        "db_name": "my_db",
        "collection": "datasources"
    }
}
```
The following are the required parameters:

|Field Name|Field Description|Example|
|----------|-----------------|-------|
|```vendor```|Database vendor|```postgresql```|
|```db_name```|Name of the DB for the connection|```my_db```|
|```collection```|Name of the table collection containing the default datasources|```datasources```|

The default datasource provides the details for a DB containing all the available datasources. Such datasources are identified by the ```datasource``` field. Each datasource must provide the following information:

|Field Name|Field Description|Example|Notes|
|----------|-----------------|-------|-----|
|```id```|Record ID|```123456```|SQL only|
|```datasource```|Unique identifier|```test_db```||
|```vendor```|DB vendor|```postgresql```||
|```db_name```|Name of the DB for the connection|```my_db```||
|```username```|Username for the connection|```my_username```|SQL only|
|```password```|Password for the connection|```my_password```|SQL only|
|```collection```|Name of the table collection containing thes default datasources|```posts```|NoSQL only|

Please note that the default DB is different from the datasources. It is possible to use a SQL DB as repository for the datasources and have only NoSQL DB's. The ```datasource``` field is used to fetch all the required parameters to connect to the specified datasource. The following example show how to list all the items contained in the ```tasks``` table by providing the datasource name:
```python
my_db = DBMS(datasource='test_postgresql')
for row in my_db.find_all('tasks'):
    print row
```
The ```test_postgresql``` datasource is stored in the default DB and, in the case of a SQL DB, it is described as follow:

|id    |datasource     |vendor    |db_name|username|password  |collection|
|------|---------------|----------|-------|--------|----------|----------|
|123456|test_postgresql|postgresql|test   |postgres|mypassword|```null```|

The document for the same datasource in a NoSQL default DB is the following:

```json
{
    "datasource": "test_postgresql",
    "vendor": "postgresql",
    "db_name": "test",
    "username": "postgres",
    "password": "mypassword"
}
```
