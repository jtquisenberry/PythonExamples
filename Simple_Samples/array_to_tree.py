import math
from collections import deque

class Node():
    def __init__(self, value, left_child = None, right_child = None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
       return str(self.value)

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
        current_list.append(Node(nodes[current_index]))
        items_placed += 1
        current_index += 1
    unlinked_nodes.append(current_list)
    print(current_list)

for level in unlinked_nodes:
    print([l.value for l in level])

for level_number in range(0, len(unlinked_nodes)):
    #Start with the second-to-last level and work up.
    print('level', level_number)
    if level_number < len(unlinked_nodes) - 1:
        level = unlinked_nodes[level_number]
        child_index = 0
        for node_number in range(0,len(level)):
            node = level[node_number]
            print('current_node_number', node_number)
            for child_node_number in [node_number * 2, node_number * 2 + 1]:
                print('child_node_number', child_node_number)

                #print(len(unlinked_nodes[level_number + 1]))
                if child_node_number < len(unlinked_nodes[level_number + 1]):
                    if child_node_number % 2 == 0:
                        print('even')
                        node.left = unlinked_nodes[level_number + 1][child_node_number]
                    else:
                        print('odd')
                        node.right = unlinked_nodes[level_number + 1][child_node_number]


root = unlinked_nodes[0][0]

print('root', root)
print('root.left', root.left)
print('root.right', root.right)
print('root.left.left', root.left.left)
print('root.left.right', root.left.right)
print('root.right.left', root.right.left)
print('root.right.right', root.right.right)
print('root.left.left.left', root.left.left.left)



# Print tree using bread-first search
visited_nodes = deque()
visited_nodes.append(root)
while len(visited_nodes) > 0:
    current_node = visited_nodes.popleft()
    print(current_node)
    node = current_node.left
    if node is not None:
        visited_nodes.append(node)
    node = current_node.right
    if node is not None:
        visited_nodes.append(node)




