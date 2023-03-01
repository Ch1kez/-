
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/palindrome-linked-list/
'''


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next

        for el, back_el in zip(head_list, head_list[::-1]):
            if el != back_el:
                return False

            head_list = head_list[:-1]
            continue

        return True