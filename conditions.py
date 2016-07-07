from db_manage import Dbmanage
from operator import itemgetter


def value_sorter(target_list):
    # Order descending the target list according to number (2nd value of the nested list).
    target_list.sort(key=itemgetter(1), reverse=True)

    # This gives divider number for the nested lists.
    all_value = 0
    for i in target_list:
        all_value += i[1]
    one_percent = all_value/100

    # Unifies the length of nested lists.
    del target_list[14:]

    # Unifies the value (2nd member) of the nested lists.
    for i in target_list:
        divided_value = i[1]/one_percent
        i.pop(1)
        i.insert(1, round(divided_value))
    return target_list


def average_colour(target_list):
    return value_sorter(target_list)


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
    return value_sorter(changed_list)


def word_counter(target_list):
    for element in target_list:
        element.insert(1, len(element[0]))
    return value_sorter(target_list)


def manager(manager_list):
    summa_status = []
    for element in manager_list:
        summa_status.append(element[1])
    summa_status = sum(summa_status)
    for element in manager_list:
        element.insert(1, round(element[1]/summa_status, 3))
        element.pop()
    return value_sorter(manager_list)


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
    return value_sorter(final_list)
