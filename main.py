# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math


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
