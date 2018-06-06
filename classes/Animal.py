"""
Author: Jacob Quisenberry
Title: LeadCrunch Python Exercise
Version: 1.0
Python Version: 3.6
"""


# The DRY principle suggests that duplicate attributes and methods
# should take advantage of inheritance and reside in a base class.
# Base class
class Animal:

    def __init__(self, name):
        self.name = name

        # Use of a list because it is mutable
        self.offspring = []

        # A reference for use in a linked list, where each Animal in a
        # pedigree is a node.
        self.parent = None

    def sleep(self):
        # This style of string formatting is more flexible
        # than the older % technique.
        print("{0} sleeps".format(self.name))

    def add_offspring(self, animal):
        # Use of self to compare calling type with argument type.
        if (type(self) == type(animal)):
            animal.parent = self
            self.offspring.append(animal)
        else:
            # Specifying the types of the arguments is more helpful than
            # raising a generic exception.
            raise TypeError("Exception: Attempted to add an offspring of an "
                             "incompatible species - Parent {0}, Child {1}".format(
                             type(self).__name__, type(animal).__name__))

    # Traverse the linked list.
    def print_pedigree(self):
        pedigree = []
        node = self
        while(node):
            pedigree.append(node.name)
            node = node.parent
        # Reverse the order so that the oldest generation is first.
        pedigree.reverse()
        print(', '.join(pedigree))


class Cat(Animal):
    def __init__(self, name, hair_color):

        # Use of super to avoid referring to the base class by name.
        # Useful for multiple inheritance.
        super(Cat, self).__init__(name)

        # Naming of an attribute with a leading underscore, according to
        # convention that indicates the attribute should be treated as
        # private.
        # I am aware of the practice of using a double-underscore to mangle
        # the name in order to make the attribute inaccessible, but I do not
        # normally use it because it is still accessible with
        # _<class><attribute>
        self._hair_color = hair_color

    # Use of a getter to return hair_color
    @property
    def hair_color(self):
        return self._hair_color

    # Use of a setter to throw AttributeError with a custom message.
    @hair_color.setter
    def hair_color(self, value):
        raise AttributeError("Property hair_color is read-only.")

    def meow(self):
        print("{0} meows".format(self.name))


class Dog(Animal):
    def __init__(self, name, breed):
        super(Dog, self).__init__(name)
        self._breed = breed

    # Use of a getter to return breed
    @property
    def breed(self):
        return self._breed

    # Use of a setter to throw AttributeError with a custom message.
    @breed.setter
    def breed(self, value):
        raise AttributeError("Property breed is read-only.")

    def bark(self):
        print("{0} barks".format(self.name))


'''
########### Part 1 #####################

fido = Dog('Fido', 'Golden Retriever')
fido.sleep() # prints 'Fido sleeps'
fido.bark() # prints 'Fido barks'
print (fido.breed) # prints 'Golden Retriever'

morris = Cat('Morris', 'orange')
morris.sleep() # prints 'Morris sleeps'
morris.meow() # prints 'Morris meows'
print (morris.hair_color) # prints 'orange'


########### Part 2 #####################

fido.add_offspring(Dog('Spot', 'Goldendoodle'))
fido.add_offspring(Dog('Rover', 'Goldendoodle'))
fido.offspring[0].sleep() # prints 'Spot sleeps'
fido.offspring[0].bark() # prints 'Spot barks'
print(fido.offspring[0].breed) # prints 'Goldendoodle'
fido.offspring[1].sleep() # prints 'Rover sleeps'
fido.offspring[1].bark() # prints 'Rover barks'
print(fido.offspring[1].breed) # prints 'Goldendoodle'

morris.add_offspring(Cat('Tiger', 'gray'))
morris.offspring[0].sleep() # prints 'Tiger sleeps'
morris.offspring[0].meow() # prints 'Tiger meows'
print(morris.offspring[0].hair_color) # prints 'gray'


########### Part 2a #####################

#fido.add_offspring(Cat('Seymour', 'black'))
#morris.add_offspring(Dog('Rex', 'Black Lab'))


########### Part 3 #####################

felix = Cat('Felix', 'black')
morris = Cat('Morris', 'orange')
tiger = Cat('Tiger', 'gray')
mongo = Cat('Mongo', 'white')

felix.add_offspring(morris)
morris.add_offspring(tiger)
tiger.add_offspring(mongo)

mongo.print_pedigree() # prints 'Felix, Morris, Tiger, Mongo'
'''
