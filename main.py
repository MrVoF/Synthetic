from promon_postgre import PSQLConnect
from promon_faker import Fake
from promon_yaml import Yaml

yaml = Yaml(file_name='data.yml')
host = yaml.get_data()['host']
dbname = yaml.get_data()['database']
schema = yaml.get_data()['schema']
username = yaml.get_data()['username']
password = yaml.get_data()['password']

# if yaml.get_data()['database']:
#     psql = PSQLConnect(host=host, dbname=dbname, schema=schema, username=username, password=password)
#     psql.open_connection()
#     # psql.drop_database(dbname)
#     psql.create_database(dbname)
#     psql.close_connection()

if yaml.get_data()['schema']:
    psql = PSQLConnect(host=host, dbname=dbname, schema=schema, username=username, password=password)
    psql.open_connection()
    psql.drop_schema(yaml.get_data()['schema'])
    psql.create_schema(yaml.get_data()['schema'])
    psql.close_connection()

if yaml.get_data()['tables']:
    psql = PSQLConnect(host=host, dbname=dbname, schema=schema, username=username, password=password)
    psql.open_connection()
    for table in yaml.get_data()['tables']:
        psql.drop_table(table['name'])
        psql.create_table(table['name'], table['columns'])

        if yaml.get_data()['datacount'] > 0:
            fake = Fake()
            for n in range(yaml.get_data()['datacount']):
                columns = ''
                values = ''
                for column in table['columns']:
                    columns += column['name'] + ', '
                    values += fake.get_data(column['stype']) + ', '
                psql.insert_table(table['name'], columns[:-2], values[:-2])

    psql.close_connection()

del psql
