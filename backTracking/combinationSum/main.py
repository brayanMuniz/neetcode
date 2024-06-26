from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i > len(candidates) - 1 or total > target:
                return

            # include candidate
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # remove the previous candidate and dont include it
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res
