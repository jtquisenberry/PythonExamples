

def reverse_list_in_place(characters):

    characters_reversed = list(reversed(characters))
    for index, character in enumerate(characters_reversed):
        characters[index] = character





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
