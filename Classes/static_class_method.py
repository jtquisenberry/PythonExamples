class Base():

    class_attribute = 9

    def __init__(self):
        self.instance_attribute = 10

    @staticmethod
    def add_numbers(a, b):
        # Static method calling static method
        # nothing represents the class, must specify it explicitly
        Base.print_static()

        # Static method calling class method
        # nothing represents the class, must specify it explicitly
        Base.print_class()  # Succeeds because cls is optional

        # Static method calling instance method
        Base.print_instance(None)  # Succeeds because None is a valid argument
        # Base.print_dogs()  # Fails because self is mandatory

        return a + b

    @classmethod
    def multiply_numbers(cls, a, b):
        # Class method calling static method
        # cls represents the class
        cls.print_static()

        # Class method calling class method
        # cls represents the class
        cls.print_class() # Succeeds because cls in optional

        # Class method calling instance method
        cls.print_instance(None)  # Succeeds because None is a valid argument

        return a * b

    # instance method
    def substract_numbers(self, a, b):
        self.print_static()
        self.print_class()
        self.print_instance()

        return a - b

    @staticmethod
    def print_static():
        print()
        print('Hello from Static Method')

    @classmethod
    def print_class(cls):
        print('Type passed to class method = {0}'.format(cls))
        print('Hello from Class Method')

    # Instance method
    def print_instance(self):
        print('Hello from Instance Method')
        # self.instance_attribute = 0  # Fails if called by a static or instance method

if __name__ == '__main__':

    # Static Method
    # Call static method by specifying the type.
    result = Base.add_numbers(2,4)
    print("Class attribute {0}".format(Base.class_attribute))
    # print("Instance attribute {0}".format(Base.instance_attribute))  # Fails
    print("Return from static method = {0}".format(result))
    print()


    # Class Method
    # Call static method by specifying the type.
    result = Base.multiply_numbers(2, 4)
    print("Class attribute {0}".format(Base.class_attribute))
    print("Return from class method = {0}".format(result))
    # print("Instance attribute {0}".format(Base.instance_attribute))  # Fails
    print()


    # Instance method
    # Call instance method by specifying an object of the type.
    base = Base()
    result = base.substract_numbers(2,4)
    # Can change class attribute
    base.class_attribute = 111
    print("Class attribute {0}".format(base.class_attribute))
    # Can change instance attribute
    base.instance_attribute = 222
    print("Instance attribute {0}".format(base.instance_attribute))
    print("Return from static method = {0}".format(result))
