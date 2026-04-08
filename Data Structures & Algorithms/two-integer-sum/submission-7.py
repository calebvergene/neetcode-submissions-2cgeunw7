class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = {}
        for i, num in enumerate(nums):
            if target - num in hsh:
                return [hsh[target-num], i]
            hsh[num] = i
        
        