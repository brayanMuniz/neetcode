from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       # traverse the list, set each value to inf
       # if the next value is inf, return true
       # if next is None, return false
       while head:
           if head.val == float('inf'):
               return True
           head.val = float('inf')
           head = head.next
       return False
           