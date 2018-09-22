# 含参装饰器的使用
def func(func_name):
    print("---func1----")
    def func_in(a, b):                # 如果a, b 没有定义，那么会导致16行调用失败
        print("---func_in_1-----")
        func_name(a, b)               # 如果没有把 a,b 当做实参进行传递，那么会导致调用11 行的函数失败
        print("-----func_in_2------")
    print("-----func----2----")
    return func_in
@func    # 相当于 test = func(test)
def test(a, b):
    print("-----test---a={0}, b={1}---".format(a, b))


if __name__ == "__main__":
    test(11, 22)
