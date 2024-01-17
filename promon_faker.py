from faker import Faker


class Fake:

    def __init__(self, locale='ru_RU', count=10):
        self.locale = locale
        self.count = count
        self.faker = Faker(locale)

    def __str__(self):
        return "locale: " + self.locale + " count: " + str(self.count)

    def id(self):
        '''Генерация случайных идентификаторов'''
        import uuid
        values = []
        for _ in range(self.count):
            values.append(str(uuid.uuid4()))
        return values

    def strim(self):
        '''Генерация случайных названий стримов'''
        values = []
        for _ in range(self.count):
            values.append(self.faker.company())
        return values

    def team(self):
        '''Генерация случайных названий команд'''
        values = []
        for _ in range(self.count):
            values.append(self.faker.bs())
        return values

    def num_int(self):
        '''Генерация случайных целых чисел'''
        values = []
        for _ in range(self.count):
            values.append(self.faker.pyint())
        return values

    def num_float(self):
        '''Генерация случайных чисел с плавающей запятой'''
        values = []
        for _ in range(self.count):
            values.append(self.faker.pyfloat())
        return values

    def num_bool(self):
        '''Генерация случайных булевых значений'''
        values = []
        for _ in range(self.count):
            values.append(self.faker.pybool())
        return values
