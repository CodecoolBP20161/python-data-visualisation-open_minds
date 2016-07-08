from db_manage import Dbmanage
from conditions import *


name = input("Please add your database name: ")
user = input("Please add your user name: ")
password = input("Please add your password: ")
obj = Dbmanage(name, user, password)

obj.connect()


"""FIRST ------------
Text size is based on the number of projects from the client, the color of the text should
be the mix of the project colors from the client
"""

number_project_list = obj.runner("""SELECT company_name, count(id) from project GROUP BY company_name""")
x = get_color(number_project_list)
first_list = three_hex_to_rgb(x)


"""SECOND ------------
Text size is based on the budget (care of the different currencies)  and the color of the text should come
from the database.
"""

usd_currency_list = obj.runner\
    (""" SELECT company_name, budget_value, main_color FROM project WHERE budget_currency = 'USD'""")
gbp_currency_list = obj.runner\
    (""" SELECT company_name, budget_value, main_color FROM project WHERE budget_currency = 'GBP'""")
eur_currency_list = obj.runner\
    (""" SELECT company_name, budget_value, main_color FROM project WHERE budget_currency = 'EUR'""")

second_list_one = three_hex_to_rgb(currency_change(usd_currency_list, "usd"))
second_list_two = three_hex_to_rgb(currency_change(gbp_currency_list, "gbp"))
second_list_three = three_hex_to_rgb(currency_change(eur_currency_list, "eur"))


""" THIRD -----------
Text size is based on the length of the company names. The word got bigger weight if it is longer.
"""

company_name_list = obj.runner("""SELECT company_name FROM project GROUP BY company_name""")
third_list = word_counter(company_name_list)


""" FOURTH -----------
Text size is based on the status of project.
"""

manager_list = obj.runner("""SELECT company_name,SUM(status) FROM project GROUP BY company_name""")
fourth_list = manager(manager_list)


""" FIFTH-----------
Text size is based on the sum of initial of the manager name.
"""

manager_letter_list = obj.runner("""SELECT manager from project order by manager asc""")
fifth_list = first_letter_counter(manager_letter_list)
