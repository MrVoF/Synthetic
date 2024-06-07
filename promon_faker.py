from faker import Faker
import random


class Fake:

    def __init__(self, locale='ru_RU'):
        self.fake = Faker(locale)
        self.dst = []
        self.infsys = []
        self.key = []        
        departments = []
        strims = []
        teams = []

        for _ in range(10):
            departments += [(self.uuid(), self.text(50))]

        for _ in range(50):
            strims += [(self.uuid(), self.text(50))]

        for _ in range(500):
            teams += [(self.uuid(), self.text(50))]

        for _ in range(500):
            self.infsys += [(self.int([1, 1000]), self.text(50))]

        for _ in range(500):
            self.key += [self.fake.word() + '-' + str(self.int([1, 9999]))]

        for i in range(500):
            rnddep = random.randint(0, 9)
            rndstrim = random.randint(0, 49)
            dep_id = departments[rnddep][0]
            dep = departments[rnddep][1]
            for val in self.dst:
                if val[2] == strims[rndstrim][0]:
                    dep_id = val[0]
                    dep = val[1]

            self.dst += [[dep_id, dep, strims[rndstrim][0], strims[rndstrim][1], teams[i][0], teams[i][1]]]

        with open("Python\\Synthetic\\logs\\departments.log", "w", encoding='utf-8') as f:
            for val in departments: f.write(val[0] + "; " + val[1] + "\n")
        with open("Python\\Synthetic\\logs\\strims.log", "w", encoding='utf-8') as f:
            for val in strims: f.write(val[0] + "; " + val[1] + "\n")
        with open("Python\\Synthetic\\logs\\teams.log", "w", encoding='utf-8') as f:
            for val in teams: f.write(val[0] + "; " + val[1] + "\n")
        with open("Python\\Synthetic\\logs\\dst.log", "w", encoding='utf-8') as f:
            for val in self.dst: f.write(val[0] + "; " + val[1] + "; " + val[2] + "; " + val[3] + "; " + val[4] + "; " + val[5] + "\n")

    def get_data(self, stype, rnd=None):
        import re

        if rnd == None:
            self.rnd = random.randint(0, 499)
        else:
            self.rnd = rnd

        self.stype = str(stype)

        if re.search('list\(', self.stype): return self.rndlist(list(re.findall(r"'(.*?)'", self.stype)))
        if stype == 'uuid': return self.uuid()
        if re.search('text\(', self.stype): return self.text(int(re.search(r'\d+', self.stype)[0]))
        if re.search('int\(', self.stype): return self.int(list(map(int, list(re.findall(r'[-+]?\d+', self.stype)))))
        if re.search('float\(', self.stype): return self.float(list(map(float, list(re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', self.stype)))))
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
        if stype == 'infsysid': return self.informationsystem_id()
        if stype == 'infsys': return self.informationsystem()
        if stype == 'key': return self.issuekey()

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
        return random.uniform(*params)

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
        return self.fake.date_between(start_date="-2y", end_date="today").strftime("%Y-%m-%d %H:%M:%S")

    def datetime(self):
        """Генерация случайных дат с временем"""
        return self.fake.date_between(start_date="-2y", end_date="today").strftime("%Y-%m-%d")

    def name(self):
        """Генерация случайных имен"""
        return self.fake.name().replace("'", '`')

    def sprint(self):
        """Генерация случайных суперспринтов"""
        import random
        from datetime import datetime

        sprint = (str(datetime.now().year) + '.' +
                       str(random.choice(['0.1', '0.2',
                                          '1.1', '1.2', '1.3', '1.4', '1.5', '1.6',
                                          '2.1', '2.2', '2.3', '2.4', '2.5', '2.6',
                                          '3.1', '3.2', '3.3', '3.4', '3.5', '3.6',
                                          '4.1', '4.2', '4.3', '4.4', '4.5', '4.6'])
                           )
                       )
        return sprint

    def supersprint(self):
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

    def informationsystem_id(self):
        """Генерация случайного id системы"""
        return self.infsys[self.rnd][0]

    def informationsystem(self):
        """Генерация случайной системы"""
        return self.infsys[self.rnd][1]

    def issuekey(self):
        """Генерация случайного issuekey"""
        return self.key[self.rnd]
