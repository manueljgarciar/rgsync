from rgsync import RGWriteBehind, RGWriteThrough
from rgsync.Connectors import PostgreSqlConnector, PostgreSqlConnection, InfluxDbConnector, InfluxDbConnection
import os, sys

if 'LD_LIBRARY_PATH' not in os.environ:
    repeated = False
    while(True):
        # To link libs of Postgresql:
        os.environ['LD_LIBRARY_PATH'] = '/var/opt/redislabs/modules/rg/python3_1.0.0/lib/python3.7/psycopg2_binary.libs/'
        try:
            os.execv(sys.argv[0], sys.argv)
        except Exception:
            if repeated == True:
                sys.exit(1)
            else:
                repeated = True


host_redis = '10.0.2.15:5432'
user = 'iot'
password = 'hola1234'
db = 'iot'
table_name = 'persons'
primary_key = 'id'  
variablesMappings = {
	'first_name': 'first',
	'last_name': 'last',
	'age': 'age'
}

connection = PostgreSqlConnection(user, password, host_redis + '/' + db)
test_variables_connector = PostgreSqlConnector(connection, table_name, primary_key)

# Sync mode:
#RGWriteThrough(GB,  keysPrefix='person', mappings=variablesMappings, connector=test_variables_connector, name='VariablesWriteThrough',  version='99.99.99')

# Async mode:
RGWriteBehind(GB,  keysPrefix='person', mappings=variablesMappings, connector=test_variables_connector, name='VariablesWriteBehind',  version='99.99.99', batch=1)
