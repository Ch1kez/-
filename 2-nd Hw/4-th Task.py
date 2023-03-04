
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/909100641/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        head_list = [head.val]

        while head.next:
            if not head.val == head.next.val:
                head_list.append(head.next.val)

            head = head.next

        head_list_node = ListNode(head_list[0])
        current = head_list_node

        for el in head_list[1:]:
            current.next = ListNode(el)
            current = current.next

        return head_list_node
