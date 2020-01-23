def find_unique(numbers):

    unique_numbers = set()
    for number in numbers:
        if number in unique_numbers:
            unique_numbers.remove(number)
        else:
            unique_numbers.add(number)

    return list(unique_numbers)[0]

def find_unique2(numbers):

    unique_number = numbers[0]
    for number in numbers[1:]:
        unique_number = unique_number ^ number

    return unique_number




if __name__ == '__main__':
    numbers = [2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1]

    number = find_unique(numbers=numbers)
    print(number)

    number = find_unique2(numbers=numbers)
    print(number)