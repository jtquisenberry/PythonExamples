import unittest
from collections import deque

# Breadth First Search (BFS) uses a queue.
# Add the first node to the queue.
# Add to list of visited nodes.
# Pop the left side of the queue.
# For each neighbor, if not in the list of visited nodes,
# add to nodes to visit and visited.

def reconstruct_path(visited, start_node, end_node):
    path = [] # reversed at this point
    current_node = end_node
    while current_node:
        path.append(current_node)
        current_node = visited[current_node]

    path.reverse()
    return path


def bfs_get_path(graph, start_node, end_node):

    # Find the shortest route in the network between the two users
    if start_node not in graph:
        raise ValueError('')

    if end_node not in graph:
        raise ValueError('')

    visited = {start_node: None}

    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()

        if current_node == end_node:
            return reconstruct_path(visited, start_node, end_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                nodes_to_visit.append(neighbor)
                visited[neighbor] = current_node

    return None


# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


# unittest.main(verbosity=2)
