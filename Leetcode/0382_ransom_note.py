# https://leetcode.com/problems/ransom-note/submissions/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom_dict = dict()
        magazine_dict = dict()

        for character in ransomNote:
            ransom_dict[character] = ransom_dict.get(character, 0) + 1

        for character in magazine:
            magazine_dict[character] = magazine_dict.get(character, 0) + 1

        for key in ransom_dict.keys():
            if magazine_dict.get(key, 0) < ransom_dict[key]:
                return False
        return True

"""
"a"
"b"
"aa"
"ab"
"aa"
"aab"
"""
