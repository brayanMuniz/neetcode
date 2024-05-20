from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a list that is fixed to the value 1 and the size of the array 
        result = [1 for _ in nums]
        # traverse to the right, creating the prefix list 
        counter = 0
        while counter < len(nums):
            if counter == len(nums) -1: 
                result[counter] *= nums[counter -2]
            else: 
                result[counter + 1] = nums[counter] * nums[counter + 1]   
            print(result)
            print(counter)
            counter += 1         
        # traverse to the left, creating the postfix result
        counter = len(nums) -1
        while counter > 0:
            result[counter - 1] = nums[counter - 1] * nums[counter]
            print(result)
            counter -= 1
        return result
    
x = Solution()
print(x.productExceptSelf([1,2,3,4]))
