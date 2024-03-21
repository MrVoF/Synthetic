from faker import Faker
import random


class Fake:

    def __init__(self, locale='ru_RU'):
        self.fake = Faker(locale)
        self.rnd = 0
        self.dst = []
        departments = []
        strims = []
        teams = []


        for _ in range(10):
            departments += [(self.uuid(), self.text(50))]

        for _ in range(50):
            strims += [(self.uuid(), self.text(50))]

        for _ in range(500):
            teams += [(self.uuid(), self.text(50))]

        rnddep = random.randint(0, 9)
        rndstrim = random.randint(0, 49) 

        for i in range(500):
            dep_id = departments[rnddep][0]
            dep = departments[rnddep][1]
            for val in self.dst:
                if val[2] == strims[rndstrim][0]:
                    dep_id = val[0]
                    dep = val[1]

            self.dst += [[dep_id,
                dep,
                strims[rndstrim][0],
                strims[rndstrim][1],
                teams[i][0],
                teams[i][1]]]

            rnddep = random.randint(0, 9)
            rndstrim = random.randint(0, 49)

    def get_data(self, rnd, stype):
        import re

        self.rnd = rnd

        if re.search('list\(', stype): return self.rndlist(list(re.findall(r"'(.*?)'", stype)))
        if stype == 'uuid': return self.uuid()
        if re.search('text\(', stype): return self.text(int(re.search(r'\d+', stype)[0]))
        if re.search('int\(', stype,): return self.int(list(map(int, list(re.findall(r'\d+', stype)))))
        if re.search('float\(', stype,): return self.float(list(map(float, list(re.findall(r'\d+', stype)))))
        if stype == 'bool': return self.bool()
        if stype == 'boolean': return self.boolean()
        if stype == 'percent': return self.percent()
        if stype == 'date': return self.date()
        if stype == 'datetime': return self.datetime()
        if stype == 'numeric': return self.numeric()
        if stype == 'name': return self.name()
        if stype == 'supersprint': return self.supersprint()
        if stype == 'sprint': return self.sprint()
        if stype == 'teamid': return self.team_id()
        if stype == 'team': return self.team()
        if stype == 'strimid': return self.strim_id()
        if stype == 'strim': return self.strim()
        if stype == 'departmentid': return self.department_id()
        if stype == 'department': return self.department()

        print(f"Тип {stype} не найден.")

    def __str__(self):
        return "locale: " + self.locale

    def rndlist(self, params):
        data = self.fake.random_sample(params)
        return data[random.randint(0, len(data)-1)]

    def uuid(self):
        """Генерация случайных идентификаторов"""
        return self.fake.uuid4()

    def text(self, num=100):
        """Генерация случайного текста"""
        return self.fake.text(max_nb_chars=num).replace("'", '`')

    def int(self, params):
        """Генерация случайных целых чисел"""
        return self.fake.random_int(*params)

    def float(self, params):
        """Генерация случайных чисел с плавающей запятой"""
        return random.randrange(*params)

    def numeric(self):
        """Генерация случайных чисел с плавающей запятой"""
        return self.fake.pydecimal()

    def bool(self):
        """Генерация случайных булевых значений (True/False)"""
        return self.fake.pybool()

    def boolean(self):
        """Генерация случайных булевых значений (1/0)"""
        return 1 if self.fake.pybool() is True else 0

    def percent(self):
        """Генерация случайных процентов"""
        return self.fake.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=1)

    def date(self):
        """Генерация случайных дат"""
        return self.fake.date()

    def datetime(self):
        """Генерация случайных дат с временем"""
        return str(self.fake.date_time())

    def name(self):
        """Генерация случайных имен"""
        return self.fake.name().replace("'", '`')

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
        return supersprint

    def sprint(self):
        """Генерация случайных спринтов"""
        import random
        from datetime import datetime

        sprint = str(datetime.now().year) + '.' + str(random.randint(0, 4))
        return sprint

    def department_id(self):
        """Генерация случайного id департамента"""
        return self.dst[self.rnd][0]

    def department(self):
        """Генерация случайного департамента"""
        return self.dst[self.rnd][1]

    def strim_id(self):
        """Генерация случайного id стрима"""
        return self.dst[self.rnd][2]

    def strim(self):
        """Генерация случайного стрима"""
        return self.dst[self.rnd][3]               

    def team_id(self):
        """Генерация случайного id команды"""
        return self.dst[self.rnd][4]

    def team(self):
        """Генерация случайной команды"""
        return self.dst[self.rnd][5]
