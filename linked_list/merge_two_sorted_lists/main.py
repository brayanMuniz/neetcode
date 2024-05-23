# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # To deal with edgecases
        dummy = ListNode()
        tail = dummy
        
        # Traversing the list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Edgecase assignment
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # returns the head of list 1 or 2
        return dummy.next
    
# list 1: [5], list: [1,2,4] => [1,2,4,5]