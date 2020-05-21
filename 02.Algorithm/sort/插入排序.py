import numpy as np
import time

src_list = np.random.randint(1, 100000, 50000).tolist()


# 插入排序是一种简单直观的排序算法。
# 它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
def insert_sort(alist):
    length = len(alist)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[i]
            else:
                break
    return alist


start = time.time()
result = insert_sort(src_list)
end = time.time()
print("耗时：%d 毫秒" % int(round((end - start) * 1000)))
