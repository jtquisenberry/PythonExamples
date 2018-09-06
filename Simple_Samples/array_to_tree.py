import math

class Node():
    def __init__(self, value):
        self.value = 0
        self.left = None
        self.right = None

nodes = [1,2,3,4,5,6,7,8]
current_index = 0
unlinked_nodes = []
max_power = math.log(len(nodes) + 1, 2)
if max_power == int(max_power):
    # No change - already an integer.
    max_power = int(max_power)
else:
    max_power = int(max_power) + 1

for power_of_two in range(0,max_power):
    items_to_place = 2 ** power_of_two
    items_placed = 0
    current_list = []
    while (items_placed < items_to_place) and (current_index < len(nodes)):
        current_list.append(nodes[current_index])
        items_placed += 1
        current_index += 1
    unlinked_nodes.append(current_list)
    print(current_list)

print(unlinked_nodes)
for level in range(len(unlinked_nodes),-2,-1):
    #Start with the second-to-last level and work up.
    which_parent = 0

    for i in range(0, len(unlinked_nodes[-1])):
        node = Node(unlinked_nodes[-1][i])


