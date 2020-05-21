import re

# 如果string开始的0或者多个字符匹配到了正则表达式样式，就返回一个相应的匹配对象 。
# 如果没有匹配就返回 None ；注意它跟零长度匹配是不同的。
r1 = re.compile("a")
print(r1.match("aaa"))

# 扫描整个字符串找到匹配样式的第一个位置，并返回一个相应的匹配对象。
# 如果没有匹配，就返回一个 None ；
# 注意这和找到一个零长度匹配是不同的。
r2 = re.search("(?<=abc)def", "abcdef")
for i in r2.group():
    print(i)
