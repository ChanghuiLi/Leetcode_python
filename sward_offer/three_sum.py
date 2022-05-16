from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        dict_helper = {}
        i = 1
        for index in range(len(nums)):
            for index_next in range(index + 1, len(nums)):
                temp_sum = nums[index] + nums[index_next]
                dict_helper[i] = [index, index_next, temp_sum]
                i += 1
        for key in dict_helper.keys():
            start = dict_helper[key][0]
            mid = dict_helper[key][1]
            temp_sum = dict_helper[key][2]
            for index_end in range(mid + 1, len(nums)):
                if temp_sum + nums[index_end] == 0:
                    res.append([nums[start], nums[mid], nums[index_end]])
        return res
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        start = 0
        end = len(nums)


