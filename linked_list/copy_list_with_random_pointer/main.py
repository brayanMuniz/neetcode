from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Create a new node called copy, that will be the head
# Traverse the og list, make a copy it and put it in an array with its own array, [[node, null]]
# while you traverse, create the new linked list values and set the random value to null
# Also create the copy_arr
# Traverse the og list again, finding the idx of the value of random, update the randomValue
# Update the copy node and set that random value to the idx of the node in copy_arr 
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        copy = Node(head.val)
        copy_list = []
        og_list = []
        while head:
            new_node = Node(head.val)
            copy.next = new_node
            copy_list.append(new_node)
            og_list.append([head, None])
            head = head.next
            copy = copy.next

        for idx1, node in enumerate(og_list):
            random_node = node[0].random
            random_node_idx = 0
            if random_node != None:
                for idx, node in enumerate(og_list):
                    if node[0] == random_node:
                        random_node_idx = idx
                copy_list[idx1].random = copy_list[random_node_idx]
        
        return copy_list[0]

            
