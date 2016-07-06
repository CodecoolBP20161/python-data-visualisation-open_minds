from db_manage import Dbmanage



def currency_change(target_list, currency):
    changed_list = []
    if currency == "gbp":
        div = 1.2
    elif currency == "usd":
        div = 0.9
    elif currency == "eur":
        div = 1.0
    for element in target_list:
        element[1] = round(float(element[1])/div, 2)
        changed_list.append(element)
    return changed_list




