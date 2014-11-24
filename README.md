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

|Name|Value|Default|Example|
|----|-----|-------|-------|
|```db_type```||||

MongoDB
-------


PostgreSQL
----------
