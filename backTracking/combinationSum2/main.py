from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtracking(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target < 0:
                return

            prev = -1 # by skipping over i we have unique solutions
            # add all the elemtsn up to the end
            for i in range(pos, len(candidates)):
                # this is used to skip the element i to not include it again
                if candidates[i] == prev: 
                    continue

                cur.append(candidates[i])
                backtracking(cur, i + 1, target - candidates[i])

                cur.pop()

                prev = candidates[i]

        backtracking([], 0, target)

        return res

        
        

