
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/58c9322bedb4235468000019/train/python
'''


def is_very_even_number(n):
    summa = 0

    for el in str(n):
        summa += int(el)

    if len(str(summa)) == 1:
        if summa % 2 == 0:
            return True
        else:
            return False
    else:
        while len(str(summa)) > 1:
            for el in str(summa):
                summa += int(el)
        if summa % 2 == 0:
            return True
        else:
            return False

is_very_even_number(88)