from db_manage import Dbmanage
from conditions import *


# name = input("Please add your database name: ")
# user = input("Please add your user name: ")
# password = input("Please add your password: ")
# obj = Dbmanage(name, user, password)

obj = Dbmanage('postgres', 'postgres', '12345678')

obj.connect()


# FIRST ------------
all_client_list = obj.runner("""SELECT company_name, COUNT(id) FROM project GROUP BY company_name""")

# print(all_client_list)


# SECOND ------------
usd_currency_list = obj.runner\
    (""" SELECT company_name, budget_value, main_color FROM project WHERE budget_currency = 'USD'""")
gbp_currency_list = obj.runner\
    (""" SELECT company_name, budget_value, main_color FROM project WHERE budget_currency = 'GBP'""")
eur_currency_list = obj.runner\
    (""" SELECT company_name, budget_value, main_color FROM project WHERE budget_currency = 'EUR'""")

# print(currency_change(usd_currency_list, "usd"))
# print(currency_change(gbp_currency_list, "gbp"))
# print(currency_change(eur_currency_list, "eur"))


# THIRD -----------
company_name_list = obj.runner("""SELECT company_name FROM project GROUP BY company_name""")
# print(company_name_list)
print(word_counter(company_name_list))


# FOURTH -----------
manager_list = obj.runner("""SELECT company_name,SUM(status) FROM project GROUP BY company_name""")

# print(manager(manager_list))

