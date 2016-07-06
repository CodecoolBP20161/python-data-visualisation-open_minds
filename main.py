from db_manage import Dbmanage
from conditions import *


name = input("Please add your database name: ")
user = input("Please add your user name: ")
password = input("Please add your password: ")

obj = Dbmanage(name, user, password)
obj.connect()

# all_clients(obj)


