
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com//kata/5a651865fd56cb55760000e0
'''

def array_leaders(numbers):
    rez = []
    print(numbers)
    for el in numbers:
        sum = 0

        for summand in numbers[numbers.index(el) + 1:]:
            sum += summand

        if sum < el:
            rez.append(el)

    return rez


array_leaders([16,17,4,3,5,2])
