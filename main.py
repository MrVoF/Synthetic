from promon_postgre import PSQLConnect
from promon_faker import Fake

fake = Fake(locale='ru_RU', count=10)

ids = fake.id()
strims = fake.strim()

values = list(zip(ids, strims))

query = """INSERT INTO test.dict_strims (strim_id, strim) VALUES (%s, %s)"""

psql = PSQLConnect(host='localhost', username='mrvof', password='Dk@lbvbh', port='5432', dbname='testdb')
psql.connect()

psql.executemany_write_query_with_params(query, values)

result_query = psql.execute_read_query("SELECT * FROM test.dict_strims;")

print(result_query)

del psql
