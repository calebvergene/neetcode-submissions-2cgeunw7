class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        l = 0
        r = len(s) - 1

        for i in range(len(s)//2):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

