from promon_postgre import PSQLConnect
from promon_faker import Fake


fake = Fake(locale='ru_RU', count=100)

ids = fake.id()
strims = fake.strim()
val = fake.num_int()

values = list(zip(ids, strims, val))

psql = PSQLConnect(host='localhost', username='mrvof', password='Dk@lbvbh', port='5432', dbname='testdb')
psql.connect()

psql.drop_table('test.dict_strims')
psql.create_table('test.dict_strims', 'strim_id VARCHAR(255), strim VARCHAR(255), val INT')
psql.insert_table_with_params('test.dict_strims', 'strim_id, strim, val', values)

result_query = psql.read_table('test.dict_strims')

del psql
