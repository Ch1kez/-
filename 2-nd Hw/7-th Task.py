
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/56b97b776ffcea598a0006f2/train/python
'''


def bubblesort_once(l):
    flag = 0
    array = []
    array += l

    for i in range(len(array) - 1):
        if flag == 1:
            break
        for j in range(len(array) - i - 1):
            print(array[j], array[j + 1])
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        flag = 1

    return array
