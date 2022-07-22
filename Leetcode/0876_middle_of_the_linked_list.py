# https://leetcode.com/problems/middle-of-the-linked-list/submissions/


from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        results = []

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

# Input
# [1,2,3,4,5]