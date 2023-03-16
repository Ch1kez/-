
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/merge-sorted-array/
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:


        l1 = 0
        l2 = 0

        result = []

        while l1 < m and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                result.append(nums1[l1])
                l1+=1
            else:
                result.append(nums2[l2])
                l2+=1
        while l2 < len(nums2):
            result.append(nums2[l2])
            l2+=1
        nums1 = result