from rgsync import RGWriteBehind, RGWriteThrough
from rgsync.Connectors import PostgreSqlConnector, PostgreSqlConnection, InfluxDbConnector, InfluxDbConnection
import os, sys


host_redis = '10.0.2.15:8086'
user = 'iot'
password = 'hola1234'
db = 'events'
table_name = 'persons2'  
primary_key = 'id' 
variablesMappings = {
	'first_name': 'first',
	'last_name': 'last',
	'age': 'age'
}

connection = InfluxDbConnection(user, password, host_redis, db)
test_variables_connector = InfluxDbConnector(connection, table_name, primary_key)

# Sync mode:
#RGWriteThrough(GB,  keysPrefix='person', mappings=variablesMappings, connector=test_variables_connector, name='VariablesWriteThrough',  version='99.99.99')

# Async mode:
RGWriteBehind(GB,  keysPrefix='person', mappings=variablesMappings, connector=test_variables_connector, name='VariablesWriteBehind',  version='99.99.99', batch=1)

