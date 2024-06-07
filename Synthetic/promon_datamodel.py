from promon_postgre import PSQLConnect
from promon_faker import Fake
from promon_yaml import Yaml
from promon_json import Json
from promon_json import Json_data
import random


def synthetic_data(file_name='data.yml'):
    yaml = Yaml(file_name=file_name)
    fake = Fake()
    host = yaml.get_data()['host']
    database = yaml.get_data()['database']
    schema = yaml.get_data()['schema']
    username = yaml.get_data()['username']
    password = yaml.get_data()['password']

    if yaml.get_data()['tables']:
        psql = PSQLConnect(host=host, database=database, schema=schema, username=username, password=password)
        psql.open_connection()
        for table in yaml.get_data()['tables']:
            psql.drop_table(table['name'])
            psql.create_table(table['name'], table['columns'])
            if yaml.get_data()['datacount'] > 0:
                data = ''
                for _ in range(yaml.get_data()['datacount']):
                    rnd = random.randint(0, 499)
                    data += '('
                    for column in table['columns']:
                        val = fake.get_data(column['stype'], rnd)
                        if type(val) == str:
                            data += str("'" + val + "'") + ','
                        else:
                            data += str(val) + ','
                    data = data[:-1]
                    data += '),'
                psql.insert_table(table['name'], data[:-1])
        psql.close_connection()
    del psql

def json_data(file_name='data.yml'):
    yaml = Yaml(file_name=file_name)
    json_data = Json_data(count=yaml.get_data()['arraycount'])

    if yaml.get_data()['parameters']:
        data = dict()
        for parameter in yaml.get_data()['parameters']:
            for column in parameter['columns']:
                data[column['name']] = json_data.get_data(column['type'], column['stype'])
            json = Json(file_name=f"Python\Synthetic\json\{parameter['name']}.json")
            json.save_data(data)
