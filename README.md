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


PostgreSQL
----------
