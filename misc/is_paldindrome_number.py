class Solution:
    def isPalindrome(self, x: int) -> bool:
        left_idx = 0
        right_idx = len(str(x)) -1
        while left_idx < right_idx:
            if str(x)[left_idx] != str(x)[right_idx]:
                return False
            left_idx += 1
            right_idx -= 1
        return True

x = Solution()
print(x.isPalindrome(727))
print(x.isPalindrome(12))
