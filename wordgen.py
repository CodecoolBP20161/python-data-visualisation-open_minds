import random
# from  db_manage import Dbmanage


class Words():
    def __init__(self, raw_data):
        self.text = raw_data[0]
        self.weight = raw_data[1]
        self.x = raw_data[2]
        self.y = raw_data[3]

    @staticmethod
    def get_all():
        from db import Database
        return Database.get_texts()

    # def __str__(self):
    #     return "text: {} // weight: {} // x: {} // y: {}".format(self.text, self.weight, self.x, self.y)

    @classmethod
    def check(cls):
        return[{"text": data.text, "weight": data.weight, "x": data.x, "y": data.y} for data in cls.get_all()]
