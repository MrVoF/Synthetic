from promon_postgre import PSQLConnect
from promon_faker import Fake
from promon_yaml import Yaml


def synthetic_data(file_name='data.yml', del_db=False):
    yaml = Yaml(file_name=file_name)
    host = yaml.get_data()['host']
    dbname = yaml.get_data()['database']
    schema = yaml.get_data()['schema']
    username = yaml.get_data()['username']
    password = yaml.get_data()['password']

    if yaml.get_data()['tables']:
        psql = PSQLConnect(host=host, dbname=dbname, schema=schema, username=username, password=password)
        psql.open_connection()
        for table in yaml.get_data()['tables']:
            psql.drop_table(table['name'])
            psql.create_table(table['name'], table['columns'])

            if yaml.get_data()['datacount'] > 0:
                fake = Fake()
                for _ in range(yaml.get_data()['datacount']):
                    columns = ''
                    values = ''
                    for column in table['columns']:
                        columns += '"' + column['name'] + '", '
                        values += str(fake.get_data(column['stype'])) + ', '
                    psql.insert_table(table['name'], columns[:-2], values[:-2])

        psql.close_connection()

    del psql
