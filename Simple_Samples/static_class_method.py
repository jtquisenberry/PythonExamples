class Test(object):

    # regular instance method:
    def MyMethod(self):
        print('instance method')

    # class method:
    @classmethod
    def myClassMethod(cls):
        print('class method')

    # static method:
    @staticmethod
    def MyStaticMethod():
        print('static method')

t = Test()
t.MyMethod()
t.myClassMethod()
t.MyStaticMethod()


# Test.MyMethod() # Exception
Test.MyMethod(None)
Test.MyMethod(t)
Test.myClassMethod()
Test.MyStaticMethod()

