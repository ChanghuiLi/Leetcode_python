# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math

from typing import *
from collections import Counter

def findRepeatNumber(nums) -> int:
    print(range(len(nums)))
    for i in range(len(nums)):
        while i != nums[i]:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
    return -1
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2 ** 32, 2 ** 31 -1
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
        list = [divisor]
        listres = [1]
        res = 0
        while list[-1] < dividend:
            while list[-1] <= dividend - list[-1]:
                list.append(list[-1] + list[-1])
                listres.append(listres[-1] + listres[-1])
            dividend = dividend - list[-1]
            list.append(divisor)
            res += listres[-1]
            listres.append(1)
        return -res if rev else res
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temp_list2 = [[1,2]]
    print(temp_list2.remove(temp_list2[0]))
    print(temp_list2)
    dict_helper = {"311":5,"123":3}
    print(-124//123)
    print([0] * 26)
    temp = 1 << 2
    print(temp<<2)
    temp_list = ["heloo", "hi"]
    print(temp_list.index("hi"))
    del temp_list[0]
    print(temp_list)
    print(temp_list.pop(0))
    print(10%2)
    print()
    str1 = "doajsodjaojsd"
    str2 = "doajsodja1ojsd"
    print(str1[0:1])
    dict_helper = Counter(str1)
    dict_helper2 = Counter(str2)
    print(dict_helper2 == dict_helper)
    print(dict_helper)
    print(2//3)
    matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
    for i in range(101,100):
        print(i)
    if (-10000000 < -math.inf):
        print("hel")
    word = "hello"
    mask = 0
    mask |= 1 << (ord(word[1]) - ord('a'));
    print(ord(word[1]) - ord('a'))
    print(mask | 1 << 4)
    str = "hello 123"
    print(bin(2))
    print(bin(1))
    print(bin(2 & 1))
    print(2 % 1)
    print(3 % 2)
    print_hi('PyCharm')
    list = [2, 3, 1, 0, 2, 5, 3]
    print(findRepeatNumber(list))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
