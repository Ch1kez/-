
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/915893312/
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right_point = 0
        left_point = 0
        flag_count = 0
        while right_point < len(nums):

            if nums[left_point] != nums[right_point]:
                flag_count = 1
                left_point = right_point
                right_point += 1

            elif nums[left_point] == nums[right_point] and flag_count < 2:
                flag_count += 1

                right_point += 1
            elif nums[left_point] == nums[right_point] and flag_count >= 2:

                nums.pop(right_point)
