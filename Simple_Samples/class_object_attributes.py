class Dog:

    feet = 2

    def __init__(self):
        self.feet = 4


dog = Dog()
print(Dog.feet)
print(dog.feet)

Dog_dict = Dog.__dict__
dog_dict = dog.__dict__
