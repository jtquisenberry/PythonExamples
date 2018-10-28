class Dog:

    feet = 2

    def __init__(self):
        self.feet = 4


dog = Dog()
print(Dog.feet)
print(dog.feet)
print(type(dog).feet)

Dog_dict = Dog.__dict__
dog_dict = dog.__dict__

print(Dog_dict)
print(dog_dict)