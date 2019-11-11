# 字符串、列表、元组都是序列类型。
arrstr = "abc"
lists = ["a", "b", "c"]
tuples = ("a", "b", "c")  # 元组的元素不能更改，其它的和列表差不多
# 元组中只包含一个元素时，需要在元素后面添加逗号tup1 = (50,)
print(type(arrstr), type(lists), type(tuples))
print(arrstr[1], arrstr[-1], arrstr[0:3])

# 字符串拼接
print(arrstr+"def")
# 判断字符串中是否包含
print("a" not in arrstr, "a" in arrstr)  # 列表也可以使用该方法判断
# 字符串格式化
print("My name is %s and weight is %d kg!" % ("Zara", 21))

# 更新列表
lists.append("d")
print(lists)
# 删除列表元素
del lists[2]
lists.remove("d")
print(lists, lists*2, lists+lists)  # 列表重复和列表相加
# 迭代列表
for x in lists:
    print(x)
# 比较两个列表
print(lists == lists)  # 列表可以直接比较
# 查看列表的长度
print(len(lists))  # 字典、元组等都可以用这个方法查看长度


# 字典类型 d = {key1 : value1, key2 : value2 } 由键值对组成，键有唯一性
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
dict = {'a': 1, 'b': 2, 'b': '3', 'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict["a"], dict["Name"])  # 如果字典中没有的键，则会报错
# 修改字典中的元素
dict["Age"] = 25
print(dict["Age"])
# 删除字典中的元素
del dict["b"]  # 删除键“b”
# dict.clear #清空字典
# del dict #删除整个字典
