class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 -1
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        if divisor == 0:
            return 0
        rev = False
        if divisor < 0:
            divisor = -divisor
            rev = not rev
        if dividend < 0:
            dividend = -dividend
            rev = not rev
        temp_list = divisor
        temp_res = 1
        res = 0
        while temp_list <= dividend:
            while temp_list <= dividend - temp_list:
                temp_list = temp_list + temp_list
                temp_res = temp_res + temp_res
            dividend = dividend - temp_list
            temp_list = divisor
            res += temp_res
            temp_res = 1
        return -res if rev else res