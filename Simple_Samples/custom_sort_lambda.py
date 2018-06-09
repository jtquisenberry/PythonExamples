class Dog:
    def __init__(self, name, feet):
        self.name = name
        self.feet = feet

    def toString(self):
        return self.name + " " + str(self.feet)


dog1 = Dog("Mike", 4)
dog2 = Dog("Alpha", 9)
dog3 = Dog("Zulu", 5)

dogs = [dog1, dog2, dog3]
dogs.sort(key = lambda x: x.name)
for dog in dogs:
    print(dog.toString())

print(list(map(Dog.toString, dogs)))