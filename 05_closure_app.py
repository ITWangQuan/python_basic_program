# closure application

def test(a, b):
    def test_in(x):
        print(a * x + b)
    return test_in

if __name__ == "__main__":
    line1 = test(1, 1)
    line1(0)
    line2 = test(10, 4)
    line2(0)

#def createNum(a, b, x):
#    print(a * x + b)
#if __name__ == "__main__":
#    createNum(1, 1, 0)
"""
通过比较，看一看出闭包的使用可以减少函数传参的数量



"""
