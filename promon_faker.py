from faker import Faker


class Fake:

    def __init__(self, locale='ru_RU'):
        self.locale = locale
        self.faker = Faker(locale)

    def get_data(self, stype='TEXT'):
        stype = stype.upper()
        if stype == 'UUID': return self.uuid()
        if stype == 'TEXT': return self.text()
        if stype == 'STRIM': return self.strim()
        if stype == 'TEAM': return self.team()
        if stype == 'INT': return self.int()
        if stype == 'FLOAT': return self.float()
        if stype == 'BOOLEAN': return self.bool()
        if stype == 'DATE': return self.date()
        if stype == 'TIMESTAMP': return self.timestamp()
        if stype == 'NUMERIC': return self.numeric()
        return ''

    def __str__(self):
        return "locale: " + self.locale

    def uuid(self):
        '''Генерация случайных идентификаторов'''
        import uuid
        return "'" + str(uuid.uuid4()) + "'"

    def text(self):
        '''Генерация случайного текста'''
        return "'" + self.faker.text().replace("'", '`') + "'"

    def strim(self):
        '''Генерация случайных названий стримов'''
        return "'" + self.faker.company().replace("'", '`') + "'"

    def team(self):
        '''Генерация случайных названий команд'''
        return "'" + self.faker.bs().replace("'", '`') + "'"

    def int(self):
        '''Генерация случайных целых чисел'''
        return self.faker.pyint()

    def float(self):
        '''Генерация случайных чисел с плавающей запятой'''
        return self.faker.pyfloat()

    def numeric(self):
        '''Генерация случайных чисел с плавающей запятой'''
        return self.faker.pydecimal()

    def bool(self):
        '''Генерация случайных булевых значений'''
        return self.faker.pybool()

    def date(self):
        '''Генерация случайных дат'''
        return self.faker.date()

    def timestamp(self):
        '''Генерация случайных дат с временем'''
        return self.faker.date_time()
