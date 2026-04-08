class Solution:
    def rob(self, nums: List[int]) -> int:
        # we want to take the max from the houses to the right of it excluding the neighbor. 
        most = nums[-1]
        for i in range(len(nums)-3, -1, -1):
            nums[i] += most
            most = max(nums[i+1], nums[i+2])
        return nums[0] if len(nums)<2 else max(nums[0], nums[1])