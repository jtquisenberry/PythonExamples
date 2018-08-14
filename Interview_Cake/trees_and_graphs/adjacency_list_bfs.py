import unittest
from collections import deque

# Breadth First Search (BFS) uses a queue.
# Add the first node to the queue.
# Add to list of visited nodes.
# Pop the left side of the queue.
# For each neighbor, if not in the list of visited nodes,
# add to nodes to visit and visited.

def reconstruct_path(previous_nodes, start_node, end_node):
    reversed_shortest_path = []

    # Start from the end of the path and work backwards
    current_node = end_node
    while current_node:
        reversed_shortest_path.append(current_node)
        current_node = previous_nodes[current_node]

    # Reverse our path to get the right order
    reversed_shortest_path.reverse()  # flip it around, in place
    return reversed_shortest_path  # no longer reversed


def bfs_get_path(graph, start_node, end_node):
    # Find the shortest route in the network between the two users

    if start_node not in graph:
        raise ValueError('Enter a start node in the graph')

    if end_node not in graph:
        raise ValueError('Enter an end node in the graph')

    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    # Keep track of how we got to each node
    # We'll use this to reconstruct the shortest path at the end
    # We'll ALSO use this to keep track of which nodes we've
    # already visited
    how_we_reached_nodes = {start_node: None}

    while len(nodes_to_visit) > 0:

        print("nodes_to_visit", nodes_to_visit)
        print("how_we_reached_nodes", how_we_reached_nodes)

        current_node = nodes_to_visit.popleft()

        # Stop when we reach the end node
        print("current_node", current_node)
        print("end_node", end_node)
        if current_node == end_node:
            return reconstruct_path(how_we_reached_nodes, start_node, end_node)

        for neighbor in graph[current_node]:
            if neighbor not in how_we_reached_nodes:
                nodes_to_visit.append(neighbor)
                how_we_reached_nodes[neighbor] = current_node

    # If we get here, then we never found the end node
    # so there's NO path from start_node to end_node
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


unittest.main(verbosity=2)
