from typing import *
class Solution:
    # Soltuion1:
    # dp[i] = dp[i - 1] + 1, 当 i = 奇数;
    # dp[i] = dp[i / 2], 当 i = 偶数;
    # Solution2:
    # dp[i] = dp[i/2] + (i & 1)或(i % 2)
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for num in range(1, n + 1):
            res.append(res[num - 1] + num%2)

