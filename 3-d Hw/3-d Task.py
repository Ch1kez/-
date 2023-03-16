
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/valid-palindrome-ii/submissions/916498075/
'''


class Solution:

    def ispal_2(self, data, l, r):

        while l < r:

            if data[l] != data[r]:
                return False

            l += 1
            r -= 1

        return True

    def validPalindrome(self, data: str) -> bool:
        l = 0
        r = len(data) - 1

        while l < r:
            if data[l] != data[r]:
                return self.ispal_2(data, l + 1, r) or self.ispal_2(data, l, r - 1)

            l += 1
            r -= 1

        return True