import numpy as np
import time

src_list = np.random.randint(1, 100000, 50000).tolist()


# 在一个数据集中取个数作为参考点，大于该数的元素放在其右边；小于该数的元素放在其左边。
# 这样就将数据集分成两部分，大于参考值部分和小于参考值部分，递归该过程，直到序列中所有记录均有序。
def quick_sort(listt, left, right):
    if left >= right:
        return listt

    # 选择参考点，该调整范围的第1个值
    pivot = listt[left]
    low = left
    high = right

    while left < right:
        # 从右边开始查找大于参考点的值
        while left < right and listt[right] >= pivot:
            right -= 1
        # 这个位置的值先挪到左边
        listt[left] = listt[right]

        # 从左边开始查找小于参考点的值
        while left < right and listt[left] <= pivot:
            left += 1
        # 这个位置的值先挪到右边
        listt[right] = listt[left]

    # 写回改成的值
    listt[left] = pivot

    # 递归，并返回结果
    quick_sort(listt, low, left - 1)  # 递归左边部分
    quick_sort(listt, left + 1, high)  # 递归右边部分
    return listt


start = time.time()
result = quick_sort(src_list, 0, 1000)
end = time.time()
print("耗时：%d 毫秒" % int(round((end - start) * 1000)))
