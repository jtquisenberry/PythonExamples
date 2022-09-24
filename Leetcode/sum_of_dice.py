
def get_target_combinations(number_of_dice, number_of_sides, target):

    number_of_targets = 0

    def recurse(arr, index=0):
        # base case
        # The for loops provide a base case.

        # Recursive case.
        for i in range(1, number_of_sides + 1):
            arr[index] = i
            if index < number_of_dice - 1:
                recurse(arr, index=index+1)

            # This condition is necessary to prevent double-counting of combinations
            if index == number_of_dice-1:
                # print(arr)
                if sum(arr) == target:
                    print(arr)
                    nonlocal number_of_targets
                    number_of_targets += 1

    arr_in = [1] * number_of_dice
    recurse(arr_in, index=0)

    return number_of_targets


if __name__ == '__main__':
    num_targets = get_target_combinations(number_of_dice=4, number_of_sides=6, target=7)
    print(num_targets)
