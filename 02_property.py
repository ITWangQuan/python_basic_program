class Test(object):
    def __init__(self):
        self.__num = 100
    def setNum(self, newNum):
        print("--------setter----------")
        self.__num = newNum
    def getNum(self):
        print("-----------getter------------")
        return self.__num
    num = property(getNum, setNum)
if __name__ == "__main__":
    t = Test()
    '''
    print(t.getNum())
    new_num = t.setNum(50)
    print(t.getNum())
    '''
    print("-"  * 50)
    t.num = 200           # 相当于调用了 t.setNum(200)
    print(t.num)          # 相当于调用了 t.getNum()



"""

注意点：

t.num 到底是调用 getNum() 还是 setNum()，要根据实际的场景来判断，

1.如果是给 t.num 赋值，那么一定调用 setNum()

2. 如果是获取 t.num 的值，那么就一定调用getNum()

property 的作用： 相当于把方法进行了封装，开发者在对属性设置数据的时候
                 更方便





"""

