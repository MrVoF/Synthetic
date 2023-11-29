from faker import Faker
from promon_postgre import PSQLConnect


psql = PSQLConnect(host='localhost', username='mrvof', password='Dk@lbvbh', port='5432', dbname='testdb')
psql.connect()

fake = Faker('ru_RU')
num = 100

values = []

for _ in range(num):
    values.append((fake.ean(), fake.company()))

print(values)

query = """INSERT INTO test.dict_strims (strim_id, strim) VALUES (%s, %s)"""

psql.executemany_write_query_with_params(query, values)

result_query = psql.execute_read_query("SELECT * FROM test.dict_strims;")

print(result_query)

del psql