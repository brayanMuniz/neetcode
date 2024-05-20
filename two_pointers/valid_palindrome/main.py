class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx = 0
        right_idx = len(s) -1
        while left_idx < right_idx: 
            
            while left_idx < right_idx and self.isAlphaNum(s[left_idx]) is not True:
                left_idx += 1
                
            while left_idx < right_idx and self.isAlphaNum(s[right_idx]) is not True:
                right_idx -= 1
                
            if s[left_idx].lower() != s[right_idx].lower():
                return False  
            
            left_idx += 1
            right_idx -= 1
            
        return True
        
    def isAlphaNum(self, c) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or 
                ord("0") <= ord(c) <= ord("9") or
                ord("a") <= ord(c) <= ord("z"))
