
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/middle-of-the-linked-list/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []

        while head:
            head_list.append(head.val)
            head = head.next

        mid = len(head_list) // 2
        mod = len(head_list) % 2

        head_list = head_list[mid:]

        head_list_node = ListNode(head_list[0])
        current = head_list_node
        head_list = head_list[1:]

        for el in head_list:
            current.next = ListNode(el)
            current = current.next

        return head_list_node
        ф