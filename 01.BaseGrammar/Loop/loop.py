# Python 中的循环语句有 for 和 while。
# 循环遍历序列项目
sites = ["Baidu", "Google", "yahoo", "Taobao"]
for site in sites:
    if site == "Google":
        print("谷歌!")
        break           # 这里可以使用break跳出循环
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# continue 继续下一个循环
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue  # 这里可以使用continue继续下一个循环
    print(n)
print('循环结束。')

# 循环遍历数字序列
for i in range(len(sites)):
    print(i, sites[i])

for i in range(0, 10, 3):
    print(i)
