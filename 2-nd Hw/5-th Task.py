
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = codewars.com/kata/5a1ee4dfffe75f0fcb000145/train/python
'''

def bingo(array): 
    ar = [2, 9, 14, 7, 15]
    print(ar,'\n',array)
    for el in ar:
        if el not in array:
            return 'LOSE'
    return 'WIN'
