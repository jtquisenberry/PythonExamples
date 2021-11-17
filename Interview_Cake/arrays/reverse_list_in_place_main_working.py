import unittest
import pytest

def reverse_list_in_place(characters):

    if len(characters) == 0:
        return

    for i in range(len(characters) // 2):
        left_index = i
        right_index = len(characters) - 1 - i
        characters[left_index], characters[right_index] = characters[right_index], characters[left_index]

    return


if __name__ == '__main__':
    
    list_of_chars = []
    reverse_list_in_place(list_of_chars)
    expected = []
    print(list_of_chars==expected)

    list_of_chars = ['A']
    reverse_list_in_place(list_of_chars)
    expected = ['A']
    print(list_of_chars==expected)

    list_of_chars = ['A', 'B', 'C', 'D', 'E']
    reverse_list_in_place(list_of_chars)
    expected = ['E', 'D', 'C', 'B', 'A']
    print(list_of_chars==expected)
