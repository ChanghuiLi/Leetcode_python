class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        res = ""
        len_a = len(a) - 1
        len_b = len(b) - 1
        while len_a >= 0 and len_b >= 0 or carry != 0:
            digit_a = int[a[len_a]] if a[len_a] > 0 else 0
            digit_b = int[b[len_b]] if b[len_a] > 0 else 0
            carry = digit_b + digit_a + carry
            carry = 1 if carry >= 2 else 0
            sum = sum - 2 if sum >= 2 else sum
            res += str(sum)
            len_a -= 1
            len_b -= 1
        return res[::-1]

