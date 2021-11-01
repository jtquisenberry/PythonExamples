# The sum of the numbers n1...n2

print("Triangular Series")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(numbers)
print(numbers)
print("sum", sum(numbers))
s = int((n ** 2 + n ) /2)
print("sum by triangular series", s)
print()

print("Number of Pairs")
numbers = [5, 10, 15, 20]
print(numbers)
first_plus_last = numbers[0] + numbers[-1]
number_of_pairs = len(numbers) / 2
print("sum", sum(numbers))
print("number of pairs method", int(first_plus_last * number_of_pairs))