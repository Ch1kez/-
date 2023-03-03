
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/58c9322bedb4235468000019/train/python
'''


def is_very_even_number(n):
    summa = 0

    if n <= 9:
        if n % 2 == 0:
            return True
        else:
            return False
        
    else:
        
        for el in str(n):
            summa += int(el)
            
        while summa > 9:
            rez = 0
            for el in str(summa):
                print(el)
                rez += int(el)
            summa = rez
        
        if summa % 2 == 0:
            return True
        else:
            return False
       
