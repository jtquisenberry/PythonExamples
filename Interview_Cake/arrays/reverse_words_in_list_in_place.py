import unittest


# https://www.interviewcake.com/question/python/reverse-words?section=array-and-string-manipulation&course=fc1
# O(n) time
# O(1) space


def reverse_list(message, start, end):
    # print("start", start)
    # print("end", end)

    start_index = start
    end_index = end

    while start_index < end_index:
        message[start_index], message[end_index] = \
            message[end_index], message[start_index]

        start_index += 1
        end_index -= 1


def reverse_words(message):
    # print("message1",message)
    reverse_list(message, 0, len(message) - 1)
    # print("message2", message)

    start_index = 0
    end_index = 0

    for i in range(0, len(message)):
        if i == len(message) - 1:
            end_index = i
        elif message[i] == ' ':
            end_index = i - 1

        if i == len(message) - 1 or message[i] == ' ':
            reverse_list(message, start_index, end_index)
            start_index = i + 1
            # print("message3", message)

    '''
    output = []
    #print("message",message)

    start_index = 0
    end_index = len(message)


    for i in range(len(message)-1, -1, -1):
        #print(message[i])
        if message[i] == ' ' or i == 0:

            if i == 0:
                start_index = i
            else:
                start_index = i + 1
            #print ("word", message[start_index:end_index])

            output.extend(message[start_index:end_index])
            output.append(' ')
            end_index = i

    #print("output", output[:-1])       
    #print("output2", output[:len(output)-1])  
    #print(output[:-1])
    #return output[:-1]
    #message = ['xxxxxxxxx']
    #message[0] = 'z'
    #message[1] = 'z'
    for i in range(len(output)-1):
        message[i] = output[i]
    '''


# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)