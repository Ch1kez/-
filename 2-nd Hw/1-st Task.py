
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com//kata/59c8b38423dacc7d95000008
'''

def isValid(formula):
    flag = None
    f1 = 7 in formula
    f2 = 8 in formula

    if f1 == True or f2 == True:
        flag = None
    else:
        flag = False

    if flag == False:
        return flag
    else:
        flag = None

    for el in formula:

        if flag == False:
            return flag

        elif el == 1:
            if 2 in formula:
                print('не прошла', el)
                flag = False
            continue

        elif el == 2:
            if 1 in formula:
                print('не прошла', el)
                flag = False
            continue

        elif el == 3:
            if 4 in formula:
                print('не прошла', el)
                flag = False
            continue

        elif el == 4:
            if 3 in formula:
                print('не прошла', el)
                flag = False
            continue

        elif el == 5:
            if 6 not in formula:
                print('не прошла', el)
                flag = False
            continue

        elif el == 6:
            if 5 not in formula:
                print('не прошла', el)
                flag = False
            continue

    else:
        return True


