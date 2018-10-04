import unittest

def multiply(num1, num2):

    len1 = len(num1)
    len2 = len(num2)

    # Simulate Multiplication Like this
    #   1234
    #    121
    #   ----
    #   1234
    #  2468
    # 1234
    #
    # Notice that the product is moved one space to the left each time a digit
    # of the top number is multiplied by the next digit from the right in the
    # bottom number. This is due to place value.

    # Create an array to hold the product of each digit of `num1` and each
    # digit of `num2`. Allocate enough space to move the product over one more
    # space to the left for each digit after the ones place in `num2`.
    products = [0] * (len1 + len2 - 1)

    # The index will be filled in from the right. For the ones place of `num`
    # that is the only adjustment to the index.
    products_index = len(products) - 1
    products_index_offset = 0

    # Get the digits of the first number from right to left.
    for i in range(len1 -1, -1, -1):
        factor1 = int(num1[i])

        # Get the digits of the second number from right to left.
        for j in range(len2 - 1, -1, -1):
            factor2 = int(num2[j])

            # Find the product
            current_product = factor1 * factor2

            # Write the product to the correct position in the products array.
            products[products_index + products_index_offset] += current_product
            products_index -= 1

        # Reset the index to the end of the array.
        products_index = len(products) -1;
        # Move the starting point one space to the left.
        products_index_offset -= 1;

    for i in range(len(products) - 1, -1, -1):
        # Get the ones digit
        keep = products[i] % 10
        # Get everything higher than the ones digit
        carry = products[i] // 10

        products[i] = keep

        # If index 0 is reached, there is no place to store a carried value.
        # Instead retain it at the current index.
        if i > 0:
            products[i-1] += carry
        else:
            products[i] += (10 * carry)

    # Convert the list of ints to a string.
    #print(products)
    output = ''.join(map(str,products))
    return output



class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_small_product(self):
        expected = "1078095"
        actual = multiply("8765", "123")
        self.assertEqual(expected, actual)

    def test_large_product(self):
        expected = "41549622603955309777243716069997997007620439937711509062916"
        actual = multiply("654154154151454545415415454", "63516561563156316545145146514654")
        self.assertEqual(expected, actual)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


