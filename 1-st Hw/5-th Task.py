
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com//kata/57613fb1033d766171000d60
'''

def uefa_euro_2016(teams, scores):
    if scores[0] == scores[1]:
        return f'At match {teams[0]} - {teams[1]}, teams played draw.'
    else:
        if scores[0] > scores[1]:
            return f'At match {teams[0]} - {teams[1]}, {teams[0]} won!'
        else:
            return f'At match {teams[0]} - {teams[1]}, {teams[1]} won!'
