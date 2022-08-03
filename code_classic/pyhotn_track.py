import bisect
import heapq
# 二分插入，相同值放左边
temp_list = [11,12,443,1222]
pos = bisect.bisect_left(temp_list, 100, 0, len(temp_list))
print(pos)

# 堆
