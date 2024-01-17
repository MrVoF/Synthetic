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
    psql.close_connection()

if yaml.get_data()['datacount']:
    fake = Fake(locale='ru_RU', count=yaml.get_data()['datacount'])
    # strim_id = fake.id()
    # strim = fake.strim()
    # strims = list(zip(strim_id, strim))


# psql.drop_table('test.dict_strims')
# psql.create_table('test.dict_strims', 'strim_id VARCHAR(255), strim VARCHAR(255), val INT')
# psql.insert_table_with_params('test.dict_strims', 'strim_id, strim, val', values)
#
del psql
