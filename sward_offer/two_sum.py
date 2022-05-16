# sorted array
# 排序数组的性质（双指针变化）
from typing import *
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        res = []
        for index in range(len(numbers)):
            if numbers[index] in d:
                return [d[numbers[index]], index]
            d[target - numbers[index]] = index
        return []
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        pointer_start = 0;
        pointer_end = len(numbers) - 1
        while pointer_start < pointer_end:
            sum = numbers[pointer_start] + numbers[pointer_end]
            if sum == target:
                return [pointer_start, pointer_end]
            elif sum > target:
                pointer_end -= 1
            else:
                pointer_start += 1
        return []