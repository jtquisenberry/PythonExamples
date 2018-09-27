import unittest


# https://www.interviewcake.com/question/python/graph-coloring?section=trees-graphs&course=fc1

# We go through the nodes in one pass, assigning each node the first legal color we find.
# How can we be sure we'll always have at least one legal color for every node? In a graph with maximum degree DDD, each node has at most DDD neighbors. That means there are at most DDD colors taken by a node's neighbors. And we have D+1D+1D+1 colors, so there's always at least one color left to use.
# When we color each node, we're careful to stop iterating over colors as soon as we find a legal color.

# Space = O(D), where D is the number of colors. The only data structure is `used_nodes`, which contains
# at most D colors.
# Time = O(N + M) N because we must look at each node in the list. M is the number of edges
# because we must check the color of each neighbor. Each neighbor is at the end of an edge.
# We add the color of each neighbor to used_colors.


class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):
    # Create a valid coloring for the graph

    # Color one node at a time.
    # Hadle each node in the list, rather than traversing
    # the graph. This avoids problems with nodes with no
    # edges and cycles other than loops.
    for node in graph:
        # Check whether there is a loop. If there is a loop, then
        # a single node is at both ends of an edge. Then, the node
        # cannot have the same color as itself.
        if node in node.neighbors:
            raise Exception('A loop was encountered')

        # Create a list of used nodes - nodes that have already
        # been allocated to neighbors.
        used_nodes = set()
        for neighbor in node.neighbors:
            # Add the color of each neighbor to the set
            used_nodes.add(neighbor.color)

        # Apply the first available color to the current node.
        for color in colors:
            if color not in used_nodes:
                node.color = color
                break


# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.colors = frozenset([
            'red',
            'green',
            'blue',
            'orange',
            'yellow',
            'white',
        ])

    def assertGraphColoring(self, graph, colors):
        self.assertGraphHasColors(graph, colors)
        self.assertGraphColorLimit(graph)
        for node in graph:
            self.assertNodeUniqueColor(node)

    def assertGraphHasColors(self, graph, colors):
        for node in graph:
            msg = 'Node %r color %r not in %r' % (node.label, node.color, colors)
            self.assertIn(node.color, colors, msg=msg)

    def assertGraphColorLimit(self, graph):
        max_degree = 0
        colors_found = set()
        for node in graph:
            degree = len(node.neighbors)
            max_degree = max(degree, max_degree)
            colors_found.add(node.color)
        max_colors = max_degree + 1
        used_colors = len(colors_found)
        msg = 'Used %d colors and expected %d at most' % (used_colors, max_colors)
        self.assertLessEqual(used_colors, max_colors, msg=msg)

    def assertNodeUniqueColor(self, node):
        for adjacent in node.neighbors:
            msg = 'Adjacent nodes %r and %r have the same color %r' % (
                node.label,
                adjacent.label,
                node.color,
            )
            self.assertNotEqual(node.color, adjacent.color, msg=msg)

    def test_line_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')
        node_d = GraphNode('d')

        node_a.neighbors.add(node_b)
        node_b.neighbors.add(node_a)
        node_b.neighbors.add(node_c)
        node_c.neighbors.add(node_b)
        node_c.neighbors.add(node_d)
        node_d.neighbors.add(node_c)

        graph = [node_a, node_b, node_c, node_d]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_separate_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')
        node_d = GraphNode('d')

        node_a.neighbors.add(node_b)
        node_b.neighbors.add(node_a)
        node_c.neighbors.add(node_d)
        node_d.neighbors.add(node_c)

        graph = [node_a, node_b, node_c, node_d]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_triangle_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')

        node_a.neighbors.add(node_b)
        node_a.neighbors.add(node_c)
        node_b.neighbors.add(node_a)
        node_b.neighbors.add(node_c)
        node_c.neighbors.add(node_a)
        node_c.neighbors.add(node_b)

        graph = [node_a, node_b, node_c]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_envelope_graph(self):
        node_a = GraphNode('a')
        node_b = GraphNode('b')
        node_c = GraphNode('c')
        node_d = GraphNode('d')
        node_e = GraphNode('e')

        node_a.neighbors.add(node_b)
        node_a.neighbors.add(node_c)
        node_b.neighbors.add(node_a)
        node_b.neighbors.add(node_c)
        node_b.neighbors.add(node_d)
        node_b.neighbors.add(node_e)
        node_c.neighbors.add(node_a)
        node_c.neighbors.add(node_b)
        node_c.neighbors.add(node_d)
        node_c.neighbors.add(node_e)
        node_d.neighbors.add(node_b)
        node_d.neighbors.add(node_c)
        node_d.neighbors.add(node_e)
        node_e.neighbors.add(node_b)
        node_e.neighbors.add(node_c)
        node_e.neighbors.add(node_d)

        graph = [node_a, node_b, node_c, node_d, node_e]
        tampered_colors = list(self.colors)
        color_graph(graph, tampered_colors)
        self.assertGraphColoring(graph, self.colors)

    def test_loop_graph(self):
        node_a = GraphNode('a')

        node_a.neighbors.add(node_a)

        graph = [node_a]
        tampered_colors = list(self.colors)
        with self.assertRaises(Exception):
            color_graph(graph, tampered_colors)


unittest.main(verbosity=2)