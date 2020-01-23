

def reverse_list_in_place(characters):

    if len(characters) == 0:
        return

    start_index = 0
    end_index = len(characters) - 1
    while start_index < end_index:
        characters[start_index], characters[end_index] = characters[end_index], characters[start_index]
        start_index += 1
        end_index -= 1

if __name__ == '__main__':
    list_of_chars = ['A', 'B', 'C', 'D', 'E']
    print(list_of_chars)
    reverse_list_in_place(list_of_chars)
    print(list_of_chars)
