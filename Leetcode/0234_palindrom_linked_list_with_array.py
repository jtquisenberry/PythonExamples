#https://leetcode.com/problems/palindrome-linked-list/solution/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        midpoint = 0

        current_node = head
        next_node = head.next

        results = [current_node.val]

        while current_node.next is not None:
            current_node = current_node.next
            results.append(current_node.val)

        left_index = 0
        right_index = len(results) - 1
        while left_index < right_index:
            if results[left_index] != results[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True