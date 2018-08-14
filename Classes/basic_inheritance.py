class Base(object):

    def __init__(self):
        self.alpha = 0
        self.bravo = 0

class DerivedA(Base):

    def __init__(self):
        self.charlie = 1
        super().__init__()



a = DerivedA()
print(a.__dict__)