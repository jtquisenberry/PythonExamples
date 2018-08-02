import unittest


def is_balanced(tree_root):
    # Determine if the tree is superbalanced
    if tree_root == None:
        return True

    depths = []

    nodes = []
    nodes.append((tree_root, 0))
    print("nodes", [(i[0].value, i[1]) for i in nodes])

    while len(nodes):
        node, depth = nodes.pop()
        print("current node", node.value, depth)
        print("nodes2", [(i[0].value, i[1]) for i in nodes])

        if (node.left == None and node.right == None):
            # found a leaf
            print("found a leaf", node.value, depth)
            if depth not in depths:
                depths.append(depth)

            if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                return False

        else:
            # not a leaf
            if node.left != None:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))
            print("nodes3", [(i[0].value, i[1]) for i in nodes])

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

    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
       # result = is_balanced(tree)
       # self.assertFalse(result)


if __name__ == "__main__":
    # Perform tests.
    unittest.main()