import math
from typing import *

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        temp_list = []
        list_size = len(nums)
        temp_sum = 0
        res = math.inf
        for index_start in range(list_size):
            temp_sum = nums[index_start] + temp_sum
            temp_list.append(temp_sum)
            if temp_sum >= target:
                res = min(res, index_start + 1)
        if temp_list[-1] < target:
            return 0
        for index_s1 in range(1, list_size):
            for index_e1 in range(index_s1, list_size):
                if index_e1 == index_s1:
                    temp_list[index_e1] = nums[index_e1]
                else:
                    temp_list[index_e1] = temp_list[index_e1 - 1] + nums[index_e1]
                if temp_list[index_e1] >= target:
                    res = min(res, index_e1 - index_s1 + 1)
        return res
    def miniSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        start = 0
        end = 0
        sum = 0
        res = math.inf
        while end < len(nums):
            sum += nums[end]
            while sum >= target and start <= end:
                res = min(res, end - start + 1)
                sum -= nums[start]
                start += 1
            end += 1
        if start == 0 and end == len(nums):
            return 0
        return res



# leetcode submit region end(Prohibit modification and deletion)