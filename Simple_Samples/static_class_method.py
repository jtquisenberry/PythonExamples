class Test(object):

    # regular instance method:
    def MyMethod(self):
        print('instance method')

    # class method:
    @classmethod
    def MyClassMethod(klass):
        print('class method')

    # static method:
    @staticmethod
    def MyStaticMethod():
        print('static method')

t = Test()
t.MyMethod()
t.MyClassMethod()
t.MyStaticMethod()


Test.MyMethod(None)
Test.MyMethod(t)
Test.MyClassMethod()
Test.MyStaticMethod()

