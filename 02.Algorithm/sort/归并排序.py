import numpy as np
import time

src_list = np.random.randint(1, 100000, 50000).tolist()


# 归并排序(mergesort)是创建在归并操作上的一种有效的排序算法，
# 该算法是采用分治法的一个非常典型的应用。分治法：
# 分割：递归地把当前序列平均分割成两半
# 集成：在保持元素顺序的同时将上一步得到的子序列集成到一起(归并)
def merge_sort(alist):
    if len(alist) < 2:
        return alist
    # 将列表分成更小的两个列表
    mid = int(len(alist) / 2)
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


start = time.time()
result = merge_sort(src_list)
end = time.time()
print("耗时：%d 毫秒" % int(round((end - start) * 1000)))
