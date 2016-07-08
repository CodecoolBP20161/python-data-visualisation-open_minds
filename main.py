from db_manage import Dbmanage
from conditions import *


name = input("Please add your database name: ")
user = input("Please add your user name: ")
password = input("Please add your password: ")
obj = Dbmanage(name, user, password)

obj.connect()


# FIRST ------------

number_project_list = obj.runner("""SELECT company_name, count(id) from project GROUP BY company_name""")
x = get_color(number_project_list)
first_list = value_sorter(three_hex_to_rgb(x))


# SECOND ------------
usd_currency_list = obj.runner\
    (""" SELECT company_name, budget_value, main_color FROM project WHERE budget_currency = 'USD'""")
gbp_currency_list = obj.runner\
    (""" SELECT company_name, budget_value, main_color FROM project WHERE budget_currency = 'GBP'""")
eur_currency_list = obj.runner\
    (""" SELECT company_name, budget_value, main_color FROM project WHERE budget_currency = 'EUR'""")

second_list_one = currency_change(usd_currency_list, "usd")
second_list_two = currency_change(gbp_currency_list, "gbp")
second_list_three = currency_change(eur_currency_list, "eur")


# THIRD -----------
company_name_list = obj.runner("""SELECT company_name FROM project GROUP BY company_name""")
third_list = word_counter(company_name_list)


# FOURTH -----------
manager_list = obj.runner("""SELECT company_name,SUM(status) FROM project GROUP BY company_name""")
fourth_list = manager(manager_list)


# FIFTH-----------
manager_letter_list = obj.runner("""SELECT manager from project order by manager asc""")
fifth_list = first_letter_counter(manager_letter_list)
