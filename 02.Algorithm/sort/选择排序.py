import numpy as np
import time

src_list = np.random.randint(1, 100000, 50000).tolist()


# 选择排序是一种简单直观的排序算法。
# 它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
# 然后再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕。
def select_sort(alist):
    n = len(alist)
    for i in range(n):
        # 设置索引 i为最小值的索引
        min_idx = i
        # 通过比较，不断调整最小值的索引位置
        for j in range(i, n):
            if alist[j] < alist[min_idx]:
                min_idx = j
        # 交换第i个值与最小值
        alist[i], alist[min_idx] = alist[min_idx], alist[i]
    return alist


start = time.time()
result = select_sort(src_list)
end = time.time()
print("耗时：%d 毫秒" % int(round((end - start) * 1000)))
