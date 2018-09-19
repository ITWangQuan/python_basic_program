# python 中的语法糖
"""
未使用语法糖
def w1(func):
    def inner():
        print("-----正在验证权限-----")
        func()
    return inner

def f1():
    print("----f1-----")


def f2():
    print("-----f2-----")


if __name__ == "__main__":
    # 未使用语法糖
    f1 = w1(f1)
    f1()
"""

# 使用语法糖
def w1(func):
    def inner():
        print("-----正在验证权限-----")
        func()
    return inner
@w1      #  这句 @w1 等价于 f1 = w1(f1)
def f1():
    print("----f1-----")

@w1      # 调用 f2
def f2():
    print("-----f2-----")


if __name__ == "__main__":
    f1()   # 调用 f1()
    f2()   # call f2()

