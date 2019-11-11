dataint = 8  # 整数
datafloat = 8.8  # 浮点数
datastr = "python3"  # 字符串
databool = True  # 布尔值

print(databool, datafloat, dataint, datastr)
print(type(databool), type(datafloat), type(dataint), type(datastr))

# 数据类型简单转换
# str to int
strtoint = int("123")  # 如果字符串中有数字(0-9)和正负号(+/-)以外的字符，就会报错。
print(type(strtoint), strtoint)

# float to int
floattoint = int(123.45)
print(type(floattoint), floattoint)  # 会去掉小数点及后面的数值，仅保留整数部分。

# str to float
strtofloat = float("1236.54")
print(type(strtofloat), strtofloat, float('-1209'), float('-0120.29023'))

# int to float
print(type(float(-1209)), float(-1209))  # int 转换为 float 时，会自动给添加一位小数。

# int to str
inttostr = str(dataint)
print(type(inttostr), inttostr)
