
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com//kata/55e4c52ad58df7509c00007e
'''

def validate(username, password):
    database = Database()
    return database.login(username, password)