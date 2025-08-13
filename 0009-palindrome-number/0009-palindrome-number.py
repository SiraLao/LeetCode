class Solution:
    def isPalindrome(self, x: int) -> bool:
        ip = str(x)
        rev = ip[::-1]
        return ip == rev