from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # hashmap to keep track of visited and return reference to original
        visited = {} 
        
        def dfs(node):
            if node in visited:
                return visited[node]

            copy = Node(node.val) # creating new node
            visited[node] = copy  # adding reference to new node in hashmap

            # add the created neighbors, if not created create and add
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node) if node else None

            
        
