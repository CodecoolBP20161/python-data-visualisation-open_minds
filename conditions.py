from db_manage import Dbmanage


def all_clients(obj):
    client_list = obj.runner("""SELECT company_name, COUNT(id) FROM project GROUP BY company_name""")
    return client_list


