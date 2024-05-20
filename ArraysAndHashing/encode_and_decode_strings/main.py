from typing import List
class Solution:

    # for every string, append to result, indicate end of string by -
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += string + "-"
        return result
    
    # for every letter in the string, have it as a new string until we hit -
    def decode(self, s: str) -> List[str]:
        result = []
        new_word = ""
        for char in s:
            if char == "-":
                new_word = new_word.replace("-", "")
                result.append(new_word)
                new_word = ""
            new_word += char
        return result

x = Solution()
encoded = x.encode(["neet","code","love","you"])
print(encoded)
print(x.decode(encoded))