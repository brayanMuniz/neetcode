# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Traverse the whole array, make a list of it
        arr = []
        while head:
            arr.append(head)
            head = head.next
        
        l = 0
        r = len(arr) - 1
        while l < r:
            arr[l].next = arr[r]
            l += 1
            if l == r:
                break
            arr[r].next = arr[l]
            r -= 1
        arr[l].next = None    