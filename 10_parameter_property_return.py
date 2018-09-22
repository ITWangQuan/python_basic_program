# 带有返回值的装饰器的使用

def func(func_name):
    print("-----func---1---")
    def func_in():
        print("---func_in---1-----")
        x = func_name()      # 保存  返回来的haha
        print("----func_in---2----")
        return x
    return func_in        # 把haha返回到20行的调用


@func
def test():
    print("----test----")
    return "haha"


if __name__ == "__main__":
    ret = test()   # 对于return的返回，需要传递给一个变量来存储
    print("test return value is {0}".format(ret))
