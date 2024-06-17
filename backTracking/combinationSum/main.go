package main

func combinationSum(candidates []int, target int) [][]int {
	res := [][]int{}

	dfs := func(i int, cur []int, total int) {}
	dfs = func(i int, cur []int, total int) {

		// If the current total equals the target, add the current combination to the result
		if total == target {
			copySubset := make([]int, len(cur))
			copy(copySubset, cur)
			res = append(res, copySubset)
			return
		}

		// Edgecase
		if i >= len(candidates) || total > target {
			return
		}

		// Include the number again
		cur = append(cur, candidates[i])
		dfs(i, cur, total+candidates[i])

		// skip over and use the next number
		cur = cur[:len(cur)-1]
		dfs(i+1, cur, total)

	}

	cur := []int{}
	dfs(0, cur, 0)

	return res

}
