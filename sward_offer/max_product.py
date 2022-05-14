from typing import *
# 计算ASDII码ord()
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        mask= []
        for index in range(len(words)):
            temp2 = 0
            for c in words[index]:
                temp = 1 << ord(c) - ord('a')
                temp2 |= temp
            mask.append(temp2)
        for index in range(len(words)):
            for index2 in range((index + 1), len(words)):
                if mask[index] & mask[index2] == 0:
                    res = max(res, len(words[index]) * len(words[index2]))
        return res
