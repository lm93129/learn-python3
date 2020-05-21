import numpy as np
import time

src_list = np.random.randint(1, 100000, 50000).tolist()


# 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。
# 但希尔排序是非稳定排序算法。希尔排序的基本思想是：
# 先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
# 待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for i in range(gap,n):
            while (i - gap) >= 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i = i - gap
                else:
                    break
        gap = gap // 2
    return alist


start = time.time()
result = shell_sort(src_list)
end = time.time()
print ("耗时：%d 毫秒" % int(round((end - start) * 1000)))
