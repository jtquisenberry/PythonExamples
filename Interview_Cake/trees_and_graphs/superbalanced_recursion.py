import unittest

# Mutable default arguments.
# See https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument

# This program demonstrates the use of a shell program to prepare arguments for the main function.
# With previous recursion problems, I always used keyword arguments, specifying default values.
# For mutable objects, such as a list, a default value is preserved between function calls. In this example,
# if depths were set as depths=[], then the final depth of each unit test would be preserved, giving
# unexpected results.

# This alternative does not appear to work in the recursive case
# depths = None
# if depths = None:
#     depths = []

# Determined if the tree is such that no two leaf nodes differ in depth by more than one.
#https://www.interviewcake.com/question/csharp/balanced-binary-tree

def is_balanced(tree_root):
    depths = []
    output =  is_balanced_util(tree_root, 0, depths)
    return output


def is_balanced_util(tree_root, depth, depths):

    u = id(depths)

    # Determine if the tree is superbalanced
    current_depth = depth + 1

    if tree_root.left == None and tree_root.right == None:
        depths.append(current_depth)

    else:

        if tree_root.left != None:
            is_balanced_util(tree_root.left, current_depth, depths)

        if tree_root.right != None:
            is_balanced_util(tree_root.right, current_depth, depths)

    print('depths', depths)

    d2 = depths
    d2 = list(set(depths))
    if len(d2) > 2 or (len(d2) == 2 and abs(d2[0] - d2[1]) > 1):
        return False

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


if __name__ == '__main__':
    unittest.main(verbosity=2)