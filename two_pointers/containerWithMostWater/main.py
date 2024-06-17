from typing import List

class Solution:
    def getArea(self, h1, h2, b, a) -> int:
        height = min(h1, h2)
        return height * (b - a)

    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        most = 0

        while l < r:
            area = self.getArea(height[l], height[r], r, l) 
            most = max(most, area)

            # The bottleneck here is the height of the two, so we compare those
            if height[l] > height[r]:
                r -= 1
                 
            else:
                l -= 1

        return most
        
        
