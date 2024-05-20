# Time: O(n) | Space: O(n)
from typing import List
class Solution:
    def __init__(self):
        print("init")
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums: 
            if(num in hashset):
                return True
            hashset.add(num)
        return False
    
nums = [1,2,3]
x = Solution()
print(x.containsDuplicate(nums=nums))