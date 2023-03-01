
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com//kata/56e2f59fb2ed128081001328
'''

def print_array(arr):
    str_ = ''
    for el in arr:
        str_ += f'{el},'
    return str_[:-1]