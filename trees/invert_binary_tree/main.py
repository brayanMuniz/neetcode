# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return [] 
        left = None
        if root.left:
            left = self.invertTree(root.left)
        right = None
        if root.right:
            right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root