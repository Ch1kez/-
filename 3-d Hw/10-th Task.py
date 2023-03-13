
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/55467aaf72494e3bdc00007f/train/python
'''


def is_rotation(s1,s2):
    print(s1, s2)
    if s1 + s2 == '':
        return True
    for i in range(len(s2)):
        if s1 == s2[i:] + s2[:i]:
            return True
    return False