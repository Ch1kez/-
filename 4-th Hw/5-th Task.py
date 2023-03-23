

'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/reverse-linked-list/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:

            result_node = ListNode(head.val)
            cur = head

            cur = cur.next
            while cur:
                # print(cur, '\n', cur.val)

                next_ = cur.next
                cur.next = result_node
                result_node = cur
                cur = next_
                print(result_node)

            return result_node