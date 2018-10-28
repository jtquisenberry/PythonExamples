# With multiple inheritance, calling super() calls __init__() in the order of the Method Resolution Order -- __mro__.


class Animal(object):
    def __init__(self):
        print("init Animal")
        super().__init__()


class GoodBoy(object):
    def __init__(self):
        print("They're all good dogs")
        super().__init__()


class Dog(Animal):
    def __init__(self):
        print("init Dog")
        super().__init__()


class GermanShepherd(Dog, GoodBoy):
    def __init__(self):
        print("init GermanShepherd")
        # Call the init method of all ancestors in MRO order
        super().__init__()
        # Call the init method of a specific ancestor using the type and passing self.
        GoodBoy.__init__(self)


if __name__ == '__main__':
    # View the method resolution order
    print("Method Resolution Order = {0}".format(GermanShepherd.__mro__))
    german_shepherd = GermanShepherd()