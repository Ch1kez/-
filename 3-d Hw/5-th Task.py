
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/move-zeroes/submissions/916471961/
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left_point, right_point = 0, 0

        while right_point < len(nums):
            if nums[left_point] == 0 and nums[right_point] != 0:
                nums[left_point], nums[right_point] = nums[right_point], nums[left_point]
                left_point += 1

            if nums[left_point] != 0:
                left_point += 1

            right_point += 1