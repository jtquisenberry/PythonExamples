
# Calculate the sum of the left side and the right side

tree = [1,2,3,4,0,0,7,8,9,10,11,12,13,14,15,16]

#              1
#       2            3
#    4     5      6      7
#   8 9  10 11  12 13  14 15
# 16


left_side = 0
right_side = 0

power_of_two = 1
while len(tree) > 2**(power_of_two - 1):
    left_index = (2**power_of_two) -1
    right_index = (2**(power_of_two + 1)-1 -1)
    if left_index < len(tree):
        left_side += tree[left_index]
    if right_index < len(tree):
        right_side += tree[right_index]

    power_of_two += 1

print(left_side, right_side)