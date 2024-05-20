# Time: O(n) | Space O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap where I store the index and target - indexvalue
        # loop over hash when adding a new value, if the needed amount is 
        # the index_value, return the arr with those two indexes 
        d = {}
        for idx, num in enumerate(nums): 
            for key, value in d.items():
                if value == num: 
                    return [key, idx]
            d[idx] = target - num
        