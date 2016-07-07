import random
# from db import Database

class Database():
    # still need a script that updates this list dynamically
    # with new data
    text_list = [['R', 7], ['I', 1], ['T', 3], ['N', 3], ['M', 7], ['H', 3], ['L', 7], ['R', 11], ['I', 333], ['T', 3],
                 ['N', 3], ['R', 7], ['I', 1], ['T', 3], ['N', 3], ['M', 7], ['H', 3]]

    @classmethod
    def coord_assign(cls):
        for raw_text in cls.text_list:
            x = random.randrange(0, 640)
            y = random.randrange(0, 640)
            raw_text.append(x)
            raw_text.append(y)

    @classmethod
    def get_texts(cls):
        from wordgen import Words
        return [Words(raw_text) for raw_text in cls.text_list]

Database.coord_assign()
# print(Database.text_list)
