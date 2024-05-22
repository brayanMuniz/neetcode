from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Have 2 pointers, previous: null, current: head
# Advance current by 1, make node.next = previous, advance previous by 1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current != None:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp
        return previous