class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = 0
        for i, n in enumerate(nums):
            xorr ^= i ^ n
        xorr ^= len(nums)
        return xorr