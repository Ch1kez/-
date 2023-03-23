

'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/merge-nodes-in-between-zeros/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        chek = 0
        sum_left = 0
        sum_right = 0
        # print(head.val)
        while chek != 3:
            # print(head)
            if head.val == 0:
                chek += 1
            if head.val != 0 and chek == 1:
                sum_left += head.val
            if head.val != 0 and chek == 2:
                sum_right += head.val
            head = head.next

        return [sum_left, sum_right]