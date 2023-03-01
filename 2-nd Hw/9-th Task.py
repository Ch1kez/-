
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/583710f6b468c07ba1000017/train/python
'''


def proofread(string):
    string_cap = ''
    str_spl_list = string.lower().split('.')
    print(str_spl_list)
    for el in string.lower().split('. '):

        print(el.capitalize())
        if el == '':
            break
        elif len(str_spl_list) == 1:
            string_cap += el.capitalize()
        else:
            string_cap += el.capitalize() + '.'
    return string_cap.replace('ie', 'ei')
