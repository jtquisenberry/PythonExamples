# Alternative solution at
# https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/

# Maze Runner

# 0 1 0 0 0
# 0 0 0 1 0
# 0 1 0 0 0
# 0 0 0 1 0

# 1 - is a wall
# 0 - an empty cell

# a robot - starts at (0,0)

# robot's moves: 1 step up/down/left/right

# exit at (N-1, M-1) (never 1)

# length(of the shortest path from start to the exit), -1 when exit is not reachable


# time: O(NM), N = columns, M = rows
# space O(n), n = size of queue


from collections import deque
import numpy as np

def run_maze(maze):
    rows = len(maze)
    cols = len(maze[0])

    row = 0
    col = 0
    distance = 1

    next_position = deque()
    next_position.append((row, col, distance))

    # successful_routes = list()

    while len(next_position) > 0:

        array2 = np.array(maze)
        print(array2)
        print()

        current_row, current_column, current_distance = next_position.popleft()

        if current_row == rows - 1 and current_column == cols - 1:
            return current_distance
            # successful_routes.append(current_distance)

        maze[current_row][current_column] = 8

        if current_row > 0:
            up = (current_row - 1, current_column, current_distance + 1)
            if maze[up[0]][up[1]] == 0:
                next_position.append(up)

        if current_row + 1 < rows:
            down = (current_row + 1, current_column, current_distance + 1)
            if maze[down[0]][down[1]] == 0:
                next_position.append(down)

        if current_column > 0:
            left = (current_row, current_column - 1, current_distance + 1)
            if maze[left[0]][left[1]] == 0:
                next_position.append(left)

        if current_column + 1 < cols:
            right = (current_row, current_column + 1, current_distance + 1)
            if maze[right[0]][right[1]] == 0:
                next_position.append(right)

    return -1


if __name__ == '__main__':
    maze = [
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0]]

    length = run_maze(maze)
    print(length)



