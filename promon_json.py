import json
from promon_faker import Fake

class Json:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        with open(self.file_name, "rb", encoding='utf-8') as f:
            self.data = json.load(f)
            return self.data

    def save_data(self, data):
        with open(self.file_name, "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)


class Json_data:
    
    def __init__(self, count):
        self.fake = Fake()
        self.count = count
        
    def get_data(self, type, stype):
        self.stype = stype
        if type == 'string': return self.json_string()
        if type == 'bool': return self.json_bool()
        if type == 'numeric': return self.json_numeric()
        if type == 'array': return self.json_array()
        pass

    def json_string(self):
        return str(self.fake.get_data(self.stype))

    def json_bool(self):
        return self.fake.get_data('bool')

    def json_numeric(self):
        return self.fake.get_data(self.stype)

    def json_array(self):
        values = list()
        for _ in range(self.count):
                values.append(self.fake.get_data(self.stype))
        return values
