from db_manage import Dbmanage
from operator import itemgetter
import random


def value_sorter(target_list):
    # Order descending the target list according to number (2nd value of the nested list).
    target_list.sort(key=itemgetter(1), reverse=True)

    # This gives divider number for the nested lists.
    all_value = 0
    for i in target_list:
        all_value += i[1]
    one_percent = all_value/100

    # Unifies the length of nested lists.
    del target_list[60:]

    # Unifies the value (2nd member) of the nested lists.
    for i in target_list:
        divided_value = i[1]/one_percent
        i.pop(1)
        i.insert(1, round(divided_value))
    return target_list


def three_hex_to_rgb(target_list):
    six_digit_hex = ''
    for element in target_list:
        three_digit_hex = element[-1].lstrip('#')
        for j in three_digit_hex:
            six_digit_hex += j*2
        rgb_code = tuple(int(six_digit_hex[i:i + 2], 16) for i in (0, 2, 4))
        element.insert(-1, rgb_code)
        element.pop(-1)
        six_digit_hex = ''
    return target_list


def get_color(target_list):
    color_list = ['#2bb', '#2a9', '#2ba', '#1c7', '#642', '#42b', '#64c', '#786', '#f9a', '#852', '#fd9', '#aee', '#679']
    for element in target_list:
        element.append(random.choice(color_list))

    # R.I.P (Nice Try) :'(
    # (We don't have enough time finish the average color and the converter.)
    # for element in target_list:
    #     color_list = obj.runner("SELECT main_color from project WHERE company_name = '"+element[0]+"'")
    #     element.append(color_list)
        # print(element[2])
        # for i in element[2]:
        #     if None in i:
        #         i[0] = "#fff"
    # print(target_list)

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
        if element[2] is None:
            del element
        else:
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
