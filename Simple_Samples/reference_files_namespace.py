from MyReferences.dog import Dog # Import class
from MyReferences.dog import print_hello # Import function

# Ensure that functions are unique.
# Examples: math.log10 and cmath.log10


if __name__ == '__main__':
    print(__name__)

    dog = Dog()
    print(dog.feet)

    print_hello()

