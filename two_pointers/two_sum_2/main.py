# use 2 pointers, pointer l at left side and pointer r and end of list 
# if l + r > target, decrease r by 1
# if l + r < target, increase l by 1 
# 
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        solution = []
        while l < r: 
            if (numbers[l] + numbers[r]) < target: 
                l += 1
            elif (numbers[l] + numbers[r]) > target: 
                r -= 1
            else: 
                solution = [l + 1, r+1]
                break
        return solution
    
x = Solution()
print(x.twoSum([2,7,11,15], 9))