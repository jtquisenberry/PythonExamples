import unittest


def find_unique_delivery_id(delivery_ids):
    # Find the one unique ID in the list

    unique_ids = []

    for delivery_id in delivery_ids:
        if delivery_id in unique_ids:
            unique_ids.remove(delivery_id)
        else:
            unique_ids.append(delivery_id)

    print(unique_ids)
    return unique_ids[0]


# Tests
if __name__ == '__main__':

    actual = find_unique_delivery_id([1])
    expected = 1
    print(actual == expected)

    actual = find_unique_delivery_id([1, 2, 2])
    expected = 1
    print(actual == expected)

    actual = find_unique_delivery_id([3, 3, 2, 2, 1])
    expected = 1
    print(expected == actual)

    actual = find_unique_delivery_id([3, 2, 1, 2, 3])
    expected = 1
    print(expected == actual)

    actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
    print(actual)
    expected = 8
    print(expected == actual)


