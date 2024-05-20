# Fails the testcase where the list is [-1, -1, -1 ...]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a list that is fixed to the value 1 and the size of the array 
        result = [1 for _ in nums]
        # for every num in nums, multiply the value of every number in the list except self using pointers that go outwards
        start_idx = -1
        end_idx = len(nums)
        pointer_idx = 0
        for idx, num in enumerate(nums): 
            pointer_idx = idx - 1
            while(pointer_idx > start_idx):
                result[pointer_idx] *= num
                pointer_idx -= 1

            pointer_idx = idx + 1
            while(pointer_idx < end_idx):
                result[pointer_idx] *= num
                pointer_idx += 1
        return result