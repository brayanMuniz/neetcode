package diameterofbinarytree

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(root *TreeNode, diameter *int) int {
	if root == nil {
		return -1
	}
	left := dfs(root.Left, diameter)
	right := dfs(root.Right, diameter)
	*diameter = max(*diameter, 2+left+right)
	return 1 + max(left, right)
}

func diameterOfBinaryTree(root *TreeNode) int {
	diameter := 0
	dfs(root, &diameter)
	return diameter
}
