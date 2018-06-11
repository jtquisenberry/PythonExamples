class Foo:

    def __init__(self, attribute1, attribute2):
        self._attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self, arg1, arg2):
        return [arg1, arg2]

    def _method2(self, arg1):
        print('aaa')
        pass

    def method3(self, arg1):
        return int(arg1)

    def __method4(self):
        print('bbb')


foo = Foo(0, 1)
foo._attribute1 = 9
print(foo._attribute1)
foo._method2(0)
foo._Foo__method4()
