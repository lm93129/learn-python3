# 自定with的错误
class TestWith():
    # 自定义进入时候的操作
    def __enter__(self):
        pass

    # 自定义退出时候的操作
    # exc_type如果抛出异常, 这里获取异常的类型
    # exc_val如果抛出异常, 这里显示异常内容
    # exc_tb如果抛出异常,这里显示所在位置
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 判断是否有异常
        if exc_tb is None:
            print("正常结束")
        else:
            print("异常结束，错误为：%s" % exc_tb)


# 使用with来运行类
with TestWith():
    print("开始运行")
    # 制造一个错误
    raise NameError("名称错误")
