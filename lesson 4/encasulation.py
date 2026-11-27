class myClass:
    __privetVar = 27;
    def __privtmeth(self):
        print("im inside class my class")
    def hello(self):
        print("privet variable value:", myClass.__privetVar)
    def accessprivmeth(self):
        self.__privmeth()
foo = myClass()
foo.hello()
foo.accessprivmeth()