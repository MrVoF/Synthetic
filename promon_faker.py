from faker import Faker


class Fake:

    def __init__(self, locale='ru_RU'):
        self.locale = locale
        self.fake = Faker(locale)
        self.teams = []
        self.strims = []
        self.departments = []

        for _ in range(100):
            self.teams += [(self.uuid(), self.text(50))]

        for _ in range(100):
            self.strims += [(self.uuid(), self.text(50))]

        for _ in range(100):
            self.departments += [(self.uuid(), self.text(50))]

    def get_data(self, rnd=0, stype='text'):
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
        if stype == 'supersprint': return self.supersprint()
        if stype == 'sprint': return self.sprint()
        if stype == 'teamid': return self.team_id(rnd)
        if stype == 'team': return self.team(rnd)
        if stype == 'strimid': return self.strim_id(rnd)
        if stype == 'strim': return self.strim(rnd)
        if stype == 'departmentid': return self.department_id(rnd)
        if stype == 'department': return self.department(rnd)

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

    def supersprint(self):
        """Генерация случайных суперспринтов"""
        import random
        from datetime import datetime

        supersprint = (str(datetime.now().year) + '.' +
                       str(random.choice(['0.1', '0.2',
                                          '1.1', '1.2', '1.3', '1.4', '1.5', '1.6',
                                          '2.1', '2.2', '2.3', '2.4', '2.5', '2.6',
                                          '3.1', '3.2', '3.3', '3.4', '3.5', '3.6',
                                          '4.1', '4.2', '4.3', '4.4', '4.5', '4.6'])
                           )
                       )
        return "'" + supersprint + "'"

    def sprint(self):
        """Генерация случайных спринтов"""
        import random
        from datetime import datetime

        sprint = str(datetime.now().year) + '.' + str(random.randint(0, 4))
        return "'" + sprint + "'"

    def team_id(self, rnd):
        """Генерация случайного id команды"""
        return self.teams[rnd][0]

    def strim_id(self, rnd):
        """Генерация случайного id стрима"""
        return self.strims[rnd][0]

    def department_id(self, rnd):
        """Генерация случайного id департамента"""
        return self.departments[rnd][0]

    def team(self, rnd):
        """Генерация случайной команды"""
        return self.teams[rnd][1]

    def strim(self, rnd):
        """Генерация случайного стрима"""
        return self.strims[rnd][1]

    def department(self, rnd):
        """Генерация случайного департамента"""
        return self.departments[rnd][1]
