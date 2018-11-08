import unittest


# https://www.interviewcake.com/question/python/compress-url-list?section=system-design&course=fc1

# Encode string using a trie

# Space O(n**26) with 26 letters

class Trie(object):

    def __init__(self):
        self.root = {}

    def add_word(self, word):

        is_new_word = False

        current_node = self.root

        for character in word:
            if not character in current_node:
                is_new_word = True
                current_node[character] = {}

            current_node = current_node[character]

        if '*' not in current_node:
            is_new_word = True
            current_node['*'] = {}

        return is_new_word


# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


if __name__ == '__main__':
    unittest.main(verbosity=2)