# Time: O(n log n) | Space: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        # sort alphabetically 
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        print(s)
        print(t)
        
        # have pointer for each, if it gets to the end, valid, else return False
        pointer = 0 
        while pointer < len(s):
            if s[pointer] != t[pointer]:
                return False
            pointer += 1
        return True
    
        # * Notice that when they are sorted, they are the same string
        # * So you can just do this all in one line 
        return sorted(s) == sorted(t)