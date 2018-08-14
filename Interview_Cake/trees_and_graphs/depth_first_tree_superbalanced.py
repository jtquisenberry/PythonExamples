import unittest


# https://www.interviewcake.com/question/python/balanced-binary-tree?section=trees-graphs&course=fc1
# Use DFS becasue may be fast because reach leaves faster.
# Create a nodes_to_visit stack.
# Traverse until a leaf is found.
# Add the depth of the leaf to the list of leaves and then examine depths.

def is_balanced(tree_root):
    # Determine if the tree is superbalanced
    # A tree is "superbalanced" if the difference between the depths of any two
    # leaf nodes is no greater than one.

    if (tree_root is None):
        return True

    nodes_to_visit = []
    nodes_to_visit.append((tree_root, 0))

    # Append the depths of leaves only.
    depths = []

    while len(nodes_to_visit) > 0:
        node, depth = nodes_to_visit.pop()

        if node.left is None and node.right is None:
            # Found a leaf
            if depth not in depths:
                depths.append(depth)

            if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                return False

        if node.left:
            nodes_to_visit.append((node.left, depth + 1))

        if node.right:
            nodes_to_visit.append((node.right, depth + 1))

    return True


# Tests

class Test(unittest.TestCase):
    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        tree = Test.BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = Test.BinaryTreeNode(1)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_linked_list_tree(self):
        tree = Test.BinaryTreeNode(1)
        right = tree.insert_right(2)
        right_right = right.insert_right(3)
        right_right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)