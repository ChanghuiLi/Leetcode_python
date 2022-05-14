from typing import *
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in nums:
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    temp = nums[nums[i]]
                    nums[nums[i]] = nums[i]
                    nums[i] = temp
        return -1
