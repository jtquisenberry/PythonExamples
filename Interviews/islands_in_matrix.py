# Based on
# https://www.geeksforgeeks.org/find-number-of-islands/
# I adapted the solution in these key ways:
# * I replaced recursive method for depth-first with an iterative method.

# Use the long version of offsets, which is commented to include diagonals.
# Use the short version to include only horizontal and vertical adjacencies.

# Up, right, down, left
offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# Up, right, down , left, UL, DR, UR, DL
# offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

# This is the example matrix
graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

for graph_row in graph:
    print(graph_row)
print()

num_columns = len(graph)
num_rows = len(graph[0])
count = 0

visited = []
for i in range(num_rows):
    row = list([0] * num_columns)
    visited.append(row)
#print(visited)

def is_safe(i, j):
    if i >= 0 and i < num_rows and j >= 0 and j < num_columns:
        if visited[i][j] == 0:
            return True
    return False


def dfs(i, j):
    nodes = [(i, j)]

    while len(nodes):
        node = nodes.pop()
        visited[node[0]][node[1]] = 1
        # Check each neighbor
        for offset in offsets:
            # Check whether to add the node to the stack of nodes.
            if node == (2, 0):
                print(node[0] + offset[0], node[1] + offset[1])
                a = 9
            if is_safe(node[0] + offset[0], node[1] + offset[1]):
                if graph[node[0] + offset[0]][node[1] + offset[1]]:
                    # if (node[0] + offset[0], node[1] + offset[1]) not in nodes
                    nodes.append((node[0] + offset[0], node[1] + offset[1]))

        print(nodes)


if __name__ == '__main__':
    for i in range(num_rows):
        for j in range(num_columns):
            if graph[i][j] == 1 and visited[i][j] == 0:
                count += 1
                print(count)
                # Visit islands in the chain.
                dfs(i, j)
                b_breakpoint = 0
    print("Islands Count", count)







