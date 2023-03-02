
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/583710f6b468c07ba1000017/train/python
'''


def proofread(string):
    string_rez = ''
    str_spl_list = string.lower().split('.')

    for el in str_spl_list:

        if len(str_spl_list) == 1:
            return el.lower().replace('ie', 'ei').capitalize()

        elif el != '':

            if el[0] == ' ':
                string_rez += el[0] + el[1:].lower().replace('ie', 'ei').capitalize() + '.'

            else:
                string_rez += el.lower().replace('ie', 'ei').capitalize() + '.'

    if str_spl_list[-1] != '':
        string_rez = string_rez[:-1]

    return string_rez
