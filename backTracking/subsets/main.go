package main

func subsets(nums []int) [][]int {
	res := [][]int{}
	subset := []int{}

	dfs := func(int) {}
	dfs = func(i int) {

		if i >= len(nums) {
			copySubset := make([]int, len(subset))
			copy(copySubset, subset)
			res = append(res, copySubset)
			return
		}

		// decision to include nums[i]
		subset = append(subset, nums[i])
		dfs(i + 1)

		// decision NOT to include nums[i]
		subset = subset[:len(subset)-1]
		dfs(i + 1)
	}

	dfs(0)
	return res
}
