package binarytreelevelordertraversal

import "container/list"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// implement a queue using container/list and perfrom bfs

func levelOrder(root *TreeNode) [][]int {
	arr := [][]int{}
	queue := list.New()
	queue.PushBack(root)

	for queue.Len() > 0 {
		qLength := queue.Len()
		level := []int{}

		for i := 0; i < qLength; i++ {
			element := queue.Front()
			node := element.Value.(*TreeNode)
			queue.Remove(element)
			if node != nil {
				level = append(level, node.Val)
				queue.PushBack(node.Left)
				queue.PushBack(node.Right)
			}
		}

		if len(level) > 0 {
			arr = append(arr, level)
		}
	}

	return arr
}
