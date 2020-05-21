import numpy as np
import time

src_list = np.random.randint(1, 100000, 50000).tolist()


# 冒泡排序是一种简单直观的排序算法。
# 它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
# 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
# 这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


start = time.time()
result = bubble_sort(src_list)
end = time.time()
print("耗时：%d 毫秒" % int(round((end - start) * 1000)))
