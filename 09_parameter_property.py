# 含不定长参装饰器的使用
def func(func_name):
    print("---func1----")
    def func_in(*args, **kwargs):                # 如果a, b 没有定义，那么会导致16行调用失败
        print("---func_in_1-----")
        func_name(*args, **kwargs)               # 如果没有把 a,b 当做实参进行传递，那么会导致调用11 行的函数失败, 对于可变参数， *args 表示可以传递元组，而 **kwargs表示可以传递字典
        print("-----func_in_2------")
    print("-----func----2----")
    return func_in
@func    # 相当于 test = func(test)
def test(a, b, c):
    print("-----test---a={0}, b={1}, c={2}---".format(a, b,c))

@func    # 相当于 test2 = func(test2)
def test2(a, b, c, d):
    print("-----test---a={0}, b={1}, c={2}, d={3}---".format(a, b, c, d))

if __name__ == "__main__":
    test(11, 22, 33)
    test2(44, 55, 66, 77)
