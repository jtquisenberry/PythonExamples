

my_list = [1,2,3,4,5,6,7,8,9]

comprehension = [1 if i%3 == 0 else -1 for i in my_list if i > 3 ]
print(comprehension)
# [-1, -1, 1, -1, -1, 1]