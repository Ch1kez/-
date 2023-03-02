
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/52ecde1244751a799b00018a/train/python
'''


def sqrt_approximation(number):
    if number > 10:
        nuber_range = number // 2
    else:
        nuber_range = number

    for k in range(1, nuber_range):
        sq = k * k
        sq_plus_1 = (k + 1) * (k + 1)

        if sq == number:
            return k

        elif sq < number and number < sq_plus_1:
            return [k, k + 1]
