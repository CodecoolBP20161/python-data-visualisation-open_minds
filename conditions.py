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


def word_counter(target_list):
    for element in target_list:
        element.insert(1, len(element[0]))
    return(target_list)

def manager(manager_list):
    summa_status = []
    for element in manager_list:
        summa_status.append(element[1])
    summa_status = sum(summa_status)
    for element in manager_list:
        element.insert(1, round(element[1]/summa_status, 3))
        element.pop()
    return manager_list

def first_letter_counter(target_list):
    letter_amount = {}
    final_list = []
    for element in target_list:
        if element[0] is None:
            pass
        else:
            if element[0][0] in letter_amount:
                letter_amount[element[0][0]] += 1
            else:
                letter_amount[element[0][0]] = 1

    for element in letter_amount:
        final_list += [[element, letter_amount[element]]]
    return final_list
