package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type q struct {
	balanced bool
	height   int
}

func dfs(root *TreeNode) q {
	if root == nil {
		return q{balanced: true, height: 0}
	}

	left := dfs(root.Left)
	right := dfs(root.Right)
	balanced := (left.balanced == true && right.balanced == true) && (math.Abs(float64(left.height)-float64(right.height)) <= 1)

	return q{balanced: balanced, height: 1 + max(left.height, right.height)}
}

// get to the bottom of the tree
// propogate the heigh to of the tree on the way up
// use that to compare if the tree is balanced
func isBalanced(root *TreeNode) bool {

	return dfs(root).balanced

}
