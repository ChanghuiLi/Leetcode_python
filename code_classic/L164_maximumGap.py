import math
from typing import *
# 排序数组分桶，可以加速搜索效率和计算gap的效率。
class Solution:
    def maximumGap(self, nums:List[int]) -> int:
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return max(nums[0] - nums[1], nums[1] - nums[0])
        nums_buckets = []
        min_num = min(nums)
        max_num = max(nums)
        buck_len = (max_num - min_num) // len(nums) + 1
        for i in range(nums):
            if i == 0 or i == nums - 1:
                nums_buckets.append([nums[i],nums[i]])#[min,max]pair
            else:
                nums_buckets.append([math.inf,-math.inf])
        for index, item in enumerate(nums):
            if index == 0 or index == len(nums) - 1:
                continue
            temp_sum_index = (item - min_num) // buck_len
            if len(nums_buckets[temp_sum_index]) == 0:
                nums_buckets[temp_sum_index].append(item)
                nums_buckets[temp_sum_index].append(item)
            if item >= nums_buckets[temp_sum_index][1]:
                nums_buckets[temp_sum_index][1] = item
            if item <= nums_buckets[temp_sum_index][0]:
                nums_buckets[temp_sum_index][0] = item
        res = 0
        for pair_item in nums_buckets:
            res = max(res, pair_item[1] - pair_item[0])
        return res