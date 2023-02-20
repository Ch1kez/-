
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com//kata/5701800886306a876a001031
'''

def lineup_students(string):
    mass = string.split()
    mass.sort()
    return sorted(mass, key=len)[::-1]
