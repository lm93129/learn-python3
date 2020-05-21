# 文件操作之前都要打开，之后都必须要关闭
# 文件打开默认为只读权限
file1 = open("name.txt", "a")
file1.write("hello word !\n")
file1.close()  # 写入是在close之后才生效的
file2 = open("name.txt")  # 默认为只读权限

for line in file2.readlines():
    print(line)

# 使用with来打开文件可以自动处理错误和关闭文件
with open("name.txt", "a") as f:
    print(f)
    # 手动产生一个错误
    raise NameError("名称错误")
