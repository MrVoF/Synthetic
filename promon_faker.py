from faker import Faker


class Fake:

    def __init__(self, locale='ru_RU'):
        self.locale = locale
        self.faker = Faker(locale)

    def get_data(self, stype='TEXT'):
        stype = stype.upper()
        if stype == 'UUID': return self.uuid()
        if stype == 'TEXT': return self.text()
        if stype == 'INT': return self.int()
        if stype == 'FLOAT': return self.float()
        if stype == 'BOOLEAN': return self.bool()
        if stype == 'PERCENT': return self.percent()
        if stype == 'DATE': return self.date()
        if stype == 'DATETIME': return self.datetime()
        if stype == 'NUMERIC': return self.numeric()
        if stype == 'STRIM': return self.strim()
        if stype == 'TEAM': return self.team()
        if stype == 'TEAM': return self.team()
        if stype == 'TEAM': return self.team()
        if stype == 'NAME': return self.name()

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

    def percent(self):
        '''Генерация случайных процентов'''
        return self.faker.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=1)

    def date(self):
        '''Генерация случайных дат'''
        return "'" + self.faker.date() + "'"

    def datetime(self):
        '''Генерация случайных дат с временем'''
        return "'" + str(self.faker.date_time()) + "'"

    def strim(self):
        '''Генерация случайных названий стримов'''
        return "'" + self.faker.company().replace("'", '`') + "'"

    def team(self):
        '''Генерация случайных названий команд'''
        return "'" + self.faker.bs().replace("'", '`') + "'"

    def name(self):
        '''Генерация случайных имен'''
        return "'" + self.faker.name().replace("'", '`') + "'"