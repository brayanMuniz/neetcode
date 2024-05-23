class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a set (to be able to get the contains, operation in constant time)
        # have a left pointer
        # while s[r] not in the set, add to set
        # if new set is longer than current longest, update
        # else if its a repeating character, update l by increasing by one
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l +1)
        return res
x = Solution()
print("abcabcbb", x.lengthOfLongestSubstring("abcabcbb")) # 3
print("bbbb", x.lengthOfLongestSubstring("bbbb")) # 1
print("pwwkew", x.lengthOfLongestSubstring("pwwkew")) # 3
print("au", x.lengthOfLongestSubstring("au")) # 2
print("aab", x.lengthOfLongestSubstring("aab")) # 2
print("dvdf", x.lengthOfLongestSubstring("dvdf")) # 3