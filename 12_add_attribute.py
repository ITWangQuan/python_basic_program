class ML(object):
    def __init__(self, name, place):
        self.name = name
        self.place = place
    def print_result(self):
        print("{0} is the most interseting field".format(self.name))
        print("{0} is the most beautiful place".format(self.place))

if __name__ == "__main__":
    ret = ML("NLP", "BeiJing")
    ret.print_result()
    ret.author = "WQ"       # add instance attribute 
    print("the author is {0}".format(ret.author))
    ML.author = "wq"        # add class attribute
    print("ML author is {0}".format(ret.author))
    


