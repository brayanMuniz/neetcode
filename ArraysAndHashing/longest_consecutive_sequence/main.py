# Create an empty hashmap 
# loop over the array 
#   when traversing the hashmap and find the before value, update the before value with a pointer to current value
#   if you find the afterValue, add the afterValue value: afterValue, else value: -inf
# create empty groupings [[]]
# loop over hashmap 
#   if arr beggining or arr end are the values that we are looking for, merge
#   if not found, add to end of list 
# return largest set
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for n in nums: 
            if (n -1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
                
x = Solution()
nums = [9,1,4,7,3,-1,0,5,8,-1,6] # expect 7
# 9 8 , 3 4 5 6 7 8 9 , -1 0 1 
print(x.longestConsecutive(nums=nums))