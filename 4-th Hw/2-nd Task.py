'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/intersection-of-two-arrays/submissions/919326345/
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return list(set(nums1) & set(nums2))