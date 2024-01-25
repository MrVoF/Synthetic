from faker import Faker


class Fake:

    def __init__(self, locale='ru_RU'):
        self.locale = locale
        self.fake = Faker(locale)

    def get_data(self, stype='text'):
        import re

        stype = stype.lower()
        num = int(re.search(r'\d+', stype)[0]) if re.search(r'\d+', stype) else 0

        if stype == 'uuid': return self.uuid()
        if re.search('text', stype): return self.text(num)
        if stype == 'int': return self.int()
        if stype == 'float': return self.float()
        if stype == 'boolean': return self.bool()
        if stype == 'percent': return self.percent()
        if stype == 'date': return self.date()
        if stype == 'datetime': return self.datetime()
        if stype == 'numeric': return self.numeric()
        if stype == 'name': return self.name()
        return ''

    def __str__(self):
        return "locale: " + self.locale

    def uuid(self):
        """Генерация случайных идентификаторов"""
        return "'" + self.fake.uuid4() + "'"

    def text(self, num=100):
        """Генерация случайного текста"""
        return "'" + self.fake.text(max_nb_chars=num).replace("'", '`') + "'"

    def int(self):
        """Генерация случайных целых чисел"""
        return self.fake.pyint()

    def float(self):
        """Генерация случайных чисел с плавающей запятой"""
        return self.fake.pyfloat()

    def numeric(self):
        """Генерация случайных чисел с плавающей запятой"""
        return self.fake.pydecimal()

    def bool(self):
        """Генерация случайных булевых значений"""
        return 1 if self.fake.pybool() is True else 0

    def percent(self):
        """Генерация случайных процентов"""
        return self.fake.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=1)

    def date(self):
        """Генерация случайных дат"""
        return "'" + self.fake.date() + "'"

    def datetime(self):
        """Генерация случайных дат с временем"""
        return "'" + str(self.fake.date_time()) + "'"

    def name(self):
        """Генерация случайных имен"""
        return "'" + self.fake.name().replace("'", '`') + "'"
