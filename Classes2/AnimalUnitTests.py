import unittest  # PyUnit
import io
import sys
from Animal import Dog
from Animal import Cat


class AnimalTestCase(unittest.TestCase):

    # Perform setup common to multiple tests - DRY
    def setUp(self):

        # Redirect standard out to captured_output.
        # Since methods sleep(), bark(), and meow() print output, rather than
        # merely returning a string, it is necessary to capture standard out.
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

        # Setup Dogs
        self.fido = Dog('Fido', 'Golden Retriever')
        self.fido.add_offspring(Dog('Spot', 'Goldendoodle'))
        self.fido.add_offspring(Dog('Rover', 'Goldendoodle'))

        # Setup Cats
        self.morris = Cat('Morris', 'orange')
        self.morris.add_offspring(Cat('Tiger', 'gray'))
        self.felix = Cat('Felix', 'black')
        self.morris = Cat('Morris', 'orange')
        self.tiger = Cat('Tiger', 'gray')
        self.mongo = Cat('Mongo', 'white')
        self.felix.add_offspring(self.morris)
        self.morris.add_offspring(self.tiger)
        self.tiger.add_offspring(self.mongo)

    # Cleanup
    def tearDown(self):
        self.fido = None
        self.morris = None
        self.felix = None
        self.tiger = None
        self.mongo = None

    def test_dog_sleep(self):
        self.fido.sleep()
        # Append \n because print() writes \n to standard out.
        self.assertEqual(self.captured_output.getvalue(), 'Fido sleeps\n')

    def test_dog_bark(self):
        self.fido.bark()
        self.assertEqual(self.captured_output.getvalue(), 'Fido barks\n')

    def test_dog_breed(self):
        self.assertEqual(self.fido.breed, 'Golden Retriever')

    def test_cat_sleep(self):
        self.morris.sleep()
        # Append \n because print() writes \n to standard out.
        self.assertEqual(self.captured_output.getvalue(), 'Morris sleeps\n')

    def test_cat_meow(self):
        self.morris.meow()
        self.assertEqual(self.captured_output.getvalue(), 'Morris meows\n')

    def test_cat_hair_color(self):
        self.assertEqual(self.morris.hair_color, 'orange')

    def test_dog_offspring_sleep_0(self):
        self.fido.offspring[0].sleep()
        self.assertEqual(self.captured_output.getvalue(), 'Spot sleeps\n')

    def test_dog_offspring_sleep_1(self):
        self.fido.offspring[1].sleep()
        self.assertEqual(self.captured_output.getvalue(), 'Rover sleeps\n')

    def test_dog_offspring_bark_0(self):
        self.fido.offspring[0].bark()
        self.assertEqual(self.captured_output.getvalue(), 'Spot barks\n')

    def test_dog_offspring_bark_1(self):
        self.fido.offspring[1].bark()
        self.assertEqual(self.captured_output.getvalue(), 'Rover barks\n')

    def test_dog_offspring_breed_0(self):
        self.assertEqual(self.fido.offspring[0].breed, 'Goldendoodle')

    def test_dog_offspring_breed_1(self):
        self.assertEqual(self.fido.offspring[1].breed, 'Goldendoodle')

    def test_cat_offspring_sleep(self):
        self.morris.offspring[0].sleep()
        self.assertEqual(self.captured_output.getvalue(), 'Tiger sleeps\n')

    def test_cat_offspring_meow(self):
        self.morris.offspring[0].meow()
        self.assertEqual(self.captured_output.getvalue(), 'Tiger meows\n')

    def test_cat_offspring_hair_color(self):
        self.assertEqual(self.morris.offspring[0].hair_color, 'gray')

    def test_cat_pedigree_0(self):
        self.mongo.print_pedigree()
        self.assertEqual(self.captured_output.getvalue(), 'Felix, Morris, Tiger, Mongo\n')

    ##############################
    #  Exceptions and edge cases
    ##############################

    # Exception: Parent Dog given offspring Cat
    def test_animal_offspring_value_error_0(self):
        self.assertRaises(TypeError, self.fido.add_offspring, Cat('Salem', 'black'))

    # Exception: Parent Cat given offspring Dog
    def test_animal_offspring_value_error_1(self):
        self.assertRaises(TypeError, self.morris.add_offspring, Dog('Lassie', 'Collie'))

    # Exception: Attempt to set Dog.breed
    def test_dog_readonly_0(self):
        with self.assertRaises(AttributeError):
            self.fido.breed = 'Belgian Malinois'

    # Exception: Attempt to set Cat.hair_color
    def test_cat_readonly_0(self):
        with self.assertRaises(AttributeError):
            self.morris.hair_color = 'white'

    # Edge Case: Ensure there is not an error when the pedigree has only one member.
    def test_animal_pedigree_1(self):
        self.fido.print_pedigree()
        self.assertEqual(self.captured_output.getvalue(), 'Fido\n')


if __name__ == "__main__":
    # Perform tests.
    unittest.main()
