import json
from flask import Blueprint
from flask import Response
from flask.ext.cors import cross_origin
from geobricks_dbms.core.dbms_core import DBMS


dbms = Blueprint('dbms', __name__)


@dbms.route('/discovery/')
@cross_origin(origins='*')
def discovery():
    """
    Discovery service available for all Geobricks libraries that describes the plug-in.
    @return: Dictionary containing information about the service.
    """
    out = {
        'name': 'DBMS',
        'description': 'Geobricks DB management system core functionalities and services.',
        'type': 'SERVICE'
    }
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@dbms.route('/<datasource>/<table_name>/find/all/')
@cross_origin(origins='*')
def find_all(datasource, table_name):
    db = DBMS(datasource=datasource)
    out = db.find_all(table_name)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@dbms.route('/<datasource>/<table_name>/find/id/<item_id>')
@cross_origin(origins='*')
def find_by_id(datasource, table_name, item_id):
    db = DBMS(datasource=datasource)
    out = db.find_by_id(item_id, table_name)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@dbms.route('/<datasource>/<table_name>/find/field/<field_name>/<field_value>/')
@cross_origin(origins='*')
def find_by_field(datasource, table_name, field_name, field_value):
    db = DBMS(datasource=datasource)
    out = db.find_by_field(field_name, field_value, table_name)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')