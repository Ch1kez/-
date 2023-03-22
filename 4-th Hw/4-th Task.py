

'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/merge-two-sorted-lists/submissions/920368060/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        current = ListNode(0)
        head = current

        cur_1 = list1
        cur_2 = list2

        while cur_1 and cur_2:

            if cur_1.val < cur_2.val:
                current.next = cur_1
                cur_1 = cur_1.next
                current = current.next

            else:
                current.next = cur_2
                cur_2 = cur_2.next
                current = current.next

        while cur_1:
            current.next = cur_1
            cur_1 = cur_1.next
            current = current.next

        while cur_2:
            current.next = cur_2
            cur_2 = cur_2.next
            current = current.next

        return head.next