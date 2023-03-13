
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
'''


def unique_in_order(sequence):

    res_list = []

    if sequence:
        res_list.append(sequence[0])
        left_point = 0
        print(sequence)

        for right_point in range(len(sequence)):

            if sequence[left_point] != sequence[right_point]:
                left_point = right_point
                res_list.append(sequence[left_point])

        return res_list
    return res_list