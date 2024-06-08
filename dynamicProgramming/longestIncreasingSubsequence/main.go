package main

import (
	"slices"
)

func lengthOfLIS(nums []int) int {
	lis := make([]int, len(nums))
	for i := range lis {
		lis[i] = 1
	}

	for i := len(nums) - 1; i >= 0; i-- {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] < nums[j] {
				lis[i] = max(lis[i], lis[j]+1)
			}
		}
	}

	return slices.Max(lis)

}

func main() {
	test := []int{0, 1, 0, 3, 2, 3}
	lengthOfLIS(test)
}
