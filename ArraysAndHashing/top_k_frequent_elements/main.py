from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go through the list, add their frequency count to a hashmap, sort the hashmap
        d = {}
        for num in nums: 
            if num not in d.keys():
                d[num] = 1
            else: 
                d[num] = d[num] + 1
        sorted_keys = [item[0] for item in sorted(d.items(), key=lambda item: item[1], reverse=True)]
        return sorted_keys[:k]
    
x = Solution()
print(x.topKFrequent([3,0,1,0], 1))