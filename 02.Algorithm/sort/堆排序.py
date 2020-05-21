import numpy as np
import time

src_list = np.random.randint(1, 100000, 50000).tolist()


# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
# 堆是一个近似完全二叉树的结构，并同时满足堆的性质
# 即子结点的键值或索引总是小于（或者大于）它的父节点。
# 堆排序可以说是一种利用堆的概念来排序的选择排序。
# 调整堆的结构，使其父节点的值大于子节点的值
def max_heap(heap, heapsize, root):
    left = 2 * root + 1
    right = left + 1
    large = root
    if left < heapsize and heap[large] < heap[left]:
        large = left
    if right < heapsize and heap[large] < heap[right]:
        large = right
    # 若large=right或large=left，则说明，出现比父节点大的子节点，这时对调，使子节点变为父节点
    if large != root:
        heap[large], heap[root] = heap[root], heap[large]
        max_heap(heap, heapsize, large)


# 构造一个堆，对堆中数据重新排序
def build_max_heap(heap):
    length = len(heap)
    # 从后往前调整结构
    for i in range((length - 2) // 2, -1, -1):
        max_heap(heap, length, i)


# 将根节点取出与最后一位对调，对前面len-1个节点继续进行对调过程
def heap_sort(heap):
    build_max_heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heap(heap, i, 0)
    return heap


start = time.time()
result = heap_sort(src_list)
end = time.time()
print("耗时：%d 毫秒" % int(round((end - start) * 1000)))
