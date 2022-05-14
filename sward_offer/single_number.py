from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = Counter(nums)
        ans = [key for key, value in dict.item() if value == 1][0]
        return ans

        