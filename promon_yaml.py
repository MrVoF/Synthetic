import yaml


class Yaml:

    def __init__(self, file_name):
        with open(file_name, "rb") as f:
            self.data = yaml.safe_load(f)

    def get_data(self):
        return self.data
