from promon_postgre import PSQLConnect
from promon_faker import Fake
from promon_yaml import Yaml


yaml = Yaml(file_name='data.yml')

if yaml.get_data()['database']:
    psql = PSQLConnect()
    psql.open_connection()
    psql.drop_database(yaml.get_data()['database'])
    psql.create_database(yaml.get_data()['database'])
    psql.close_connection()

if yaml.get_data()['schema']:
    psql = PSQLConnect()
    psql.open_connection()
    psql.drop_schema(yaml.get_data()['schema'])
    psql.create_schema(yaml.get_data()['schema'])
    psql.close_connection()

if yaml.get_data()['tables']:
    psql = PSQLConnect()
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
