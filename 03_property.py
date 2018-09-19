# 装饰器property
class Test(object):
    def __init__(self):
        self.__num = 100

    @property             # 此时property 的名字就是 num ，property 就是对 num 的装饰
    def num(self):
        print("--------getter-------")
        return self.__num
    @num.setter
    def num(self, newNum):
        print("-------------setter-------------")
        self.__num = newNum
if __name__ == "__main__":
    t = Test()
    t.num = 200 # 相当于调用了 t.setNum(200)

    print(t.num)  # 相当于调用了 t.getNum()

    
