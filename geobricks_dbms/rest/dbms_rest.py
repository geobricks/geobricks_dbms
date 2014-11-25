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


@dbms.route('/postgresql/<db_name>/<table_name>/')
@cross_origin(origins='*')
def list_products_service(db_name, table_name):
    db = DBMS('postgresql', db_name, 'postgres', 'Ce09114238')
    out = db.select_all(table_name)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')