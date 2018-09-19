class Test(object):
    def __init__(self):
        self.__num = 100
    def setNum(self, newNum):
        self.__num = newNum
    def getNum(self):
        return self.__num
if __name__ == "__main__":
    t = Test()
    print(t.getNum())
    new_num = t.setNum(50)
    print(t.getNum())

