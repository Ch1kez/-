
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com//kata/5bb904724c47249b10000131
'''


def points(games):
    points = 0

    for el in games:
        score = el.split(':')

        if score[0] > score[1]:
            points += 3

        elif score[0] < score[1]:
            continue

        elif score[0] == score[1]:
            points += 1
    return points