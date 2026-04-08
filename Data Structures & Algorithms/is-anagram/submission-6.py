class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sort_list(stg):
            lst = []
            for letter in stg:
                lst.append(letter)
            return lst
        x = sort_list(s)
        y = sort_list(t)
        if sorted(x) == sorted(y):  # sorted() returns a new sorted list
            return True
        else:
            return False