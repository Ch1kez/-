
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/valid-palindrome/
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_point = 0
        right_point = len(s) - 1
        s = s.lower()
        while left_point < right_point:
            while left_point < right_point and not s[left_point].isalpha():
                left_point += 1
            while left_point < right_point and not s[right_point].isalpha():
                right_point -= 1
            if s[left_point] != s[right_point]:
                return False
            left_point += 1
            right_point -= 1
        return True