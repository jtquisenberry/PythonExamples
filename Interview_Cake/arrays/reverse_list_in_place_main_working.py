

def reverse_list_in_place(characters):

    if len(characters) == 0:
        return

    left_index = 0
    right_index = len(characters) - 1

    while right_index > left_index:
        characters[left_index], characters[right_index] = characters[right_index], characters[left_index]
        left_index += 1
        right_index -= 1





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
