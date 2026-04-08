class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplist = []
        for num in nums:
            if num in duplist:
                return True
            duplist.append(num)
        return False 