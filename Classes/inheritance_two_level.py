class Base(object):

    def __init__(self):
        self.alpha = 8
        self.bravo = 0


class Derived(Base):

    def __init__(self):
        self.charlie = 1
        super().__init__()
        self.bravo = 9


if __name__ == '__main__':
    derived = Derived()
    print(derived.__dict__)
    # {'charlie': 1, 'alpha': 8, 'bravo': 9}
