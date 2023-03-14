
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while j > i:
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
            i += 1
            j -= 1
        return s