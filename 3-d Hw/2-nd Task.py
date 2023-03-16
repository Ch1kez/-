
'''
    Выполнил:   Курнаев Данила
    Группа:     М7О-406с-19
    link = https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/916493016/
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l+=1
                nums[l] = nums[r]

        return l+1