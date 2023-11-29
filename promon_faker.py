from faker import Faker


class Fake:

    def __init__(self, locale='ru_RU', count=10):
        self.locale = locale
        self.count = count
        self.faker = Faker(locale)

    def __str__(self):
        return self.locale

    def id(self):
        import uuid
        values = []
        for _ in range(self.count):
            values.append(str(uuid.uuid4()))
        return values

    def strim(self):
        values = []
        for _ in range(self.count):
            values.append(self.faker.company())
        return values

    def num_int(self):
        values = []
        for _ in range(self.count):
            values.append(self.faker.pyint())
        return values

    def num_float(self):
        values = []
        for _ in range(self.count):
            values.append(self.faker.pyfloat())
        return values

    def num_bool(self):
        values = []
        for _ in range(self.count):
            values.append(self.faker.pybool())
        return values
