class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        for i in range(len(s) - len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False 
        return True
        