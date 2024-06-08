package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	result := []int{}

	if root == nil {
		return result
	}

	queue := []*TreeNode{root}

	for len(queue) > 0 {

		rightSide := false
		rightSideVal := 0
		qLength := len(queue)

		for i := 0; i < qLength; i++ {

			node := queue[0]
			queue = queue[1:]
			if node != nil {
				rightSide = true
				rightSideVal = node.Val
				queue = append(queue, node.Left)
				queue = append(queue, node.Right)
			}
		}

		if rightSide == true {
			result = append(result, rightSideVal)
		}

	}

	return result

}
