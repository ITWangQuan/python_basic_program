# 闭包操作

def test(number):
    '''
    在函数内部在定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数
    以及用到的变量称之为闭包

    '''
    def test_in(number_in):
        print("in test_in 函数，number_in is %d" % (number_in,))
        print(number + number_in)       # 可以看到 number 为外部函数的变量

    # 其实这里返回的就是闭包的结果

    return test_in


if __name__ == "__main__":
    ret = test(100)
    print("-" * 30)
    ret(1)
    ret(100)
    ret(200)
