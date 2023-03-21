
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/remove-element/submissions/919364688/
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        useful_result_point = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[useful_result_point], nums[i] = nums[i], nums[useful_result_point]
                useful_result_point += 1
        return useful_result_point