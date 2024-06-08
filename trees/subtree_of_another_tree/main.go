package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// function to find the root
func findRoot(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil {
		return false
	}
	if isSame(root, subRoot) {
		return true
	}
	return findRoot(root.Left, subRoot) || findRoot(root.Right, subRoot)
}

// function to compare if the tree is the same
func isSame(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil && subRoot == nil {
		return true
	}
	if (root == nil || subRoot == nil) || (root.Val != subRoot.Val) {
		return false
	}
	return isSame(root.Left, subRoot.Left) && isSame(root.Right, subRoot.Right)
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if subRoot == nil {
		return true
	}
	if root == nil {
		return false
	}
	return findRoot(root, subRoot)
}
