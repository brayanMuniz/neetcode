from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_prof = 0
        while r < len(prices):
           profit = prices[r] - prices[l]
           if profit <= 0:
               l = r
               r = l + 1
           elif profit > max_prof:
               max_prof = profit
               r += 1
           else: 
               r += 1
               
        return max_prof

x = Solution()
print(x.maxProfit([7,1,5,3,6,4])) # 5
print(x.maxProfit([7,6,4,3,1])) # 0 
print(x.maxProfit([1,2])) # Supposed to be 1        