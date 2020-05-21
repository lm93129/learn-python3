import numpy as np
import time

src_list = np.random.randint(1, 100000, 50000).tolist()


# 把数组a划分为n个大小相同子区间（桶），每个子区间各自排序，最后合并。
# 桶排序要求数据的分布必须均匀，不然可能会失效。
# 计数排序是桶排序的一种特殊情况，可以把计数排序当成每个桶里只有一个元素的情况。
def bucket_sort(alist):
    min_num = min(alist)
    max_num = max(alist)
    # 设置桶的大小
    bucket_size = (max_num - min_num) / len(alist)
    # 创建桶数组
    bucket_list = [[] for i in range(len(alist) + 1)]
    # 向桶数组填数
    for num in alist:
        bucket_list[int((num - min_num) // bucket_size)].append(num)
    alist.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in bucket_list:
        for j in sorted(i):
            alist.append(j)
    return alist


start = time.time()
result = bucket_sort(src_list)
end = time.time()
print("耗时：%d 毫秒" % int(round((end - start) * 1000)))


# 原理：
# (1) 设置一个定量的数组当作空桶
# (2) 遍历输入数据，并且把数据一个一个放到对应的桶里去
# (3) 对每个不是空的桶进行排序
# (4) 从不是空的桶里把排好序的数据拼接起来
