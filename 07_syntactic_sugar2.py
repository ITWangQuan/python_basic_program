# 多个装饰器
def makeBold(fn):
    def wrapped():
        print("----1----")
        return "<b>" + fn() +"</b>"
    return wrapped


def makeItalic(fn):
    def wrapped():
        print("----2-----")
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
@makeItalic  # 等价于 test3 = makeItalic(test3)
def test3():
    print("----3-----")
    return "hello world-3"

if __name__ == "__main__":
    ret = test3()
    print(ret)


"""
通过上面的运行结果，可以分析出，对于多个装饰器，从上往下，先装饰下面的
装饰器，在装饰上面的，如先装饰makeItalic，再装饰makeBold
@makeItalic 等价于 test3 = makeItalic(test3)
只要python解释器执行到了装饰器，那么就会自动进行装饰，而不是等到调用的时候
才装饰的，在调用test3时，就已经装饰了

"""
