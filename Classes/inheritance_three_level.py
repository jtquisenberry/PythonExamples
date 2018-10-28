class Animal(object):
    def __init__(self):
        print("init Animal")


class Dog(Animal):
    def __init__(self):
        print("init Dog")
        super().__init__()
        #super(Dog, self).__init__()


class GermanShepherd(Dog):
    def __init__(self):
        print("init GermanShepherd")
        super().__init__()
        # super(GermanShepard, self).__init__()


if __name__ == '__main__':
    german_shepherd = GermanShepherd()