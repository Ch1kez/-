
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/middle-of-the-linked-list/
'''


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        mid = len(head_list) % 2
        if mid == 0:
            head_list = head_list[mid:]
            return head_list
        else:
            head_list = head_list[mid + 1:]
            return head_list