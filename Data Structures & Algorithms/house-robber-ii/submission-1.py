class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<= 2:
            return max(nums)
        def helper(houses):
            mx = houses[-1]
            for i in range(len(houses)-3, -1, -1):
                houses[i] += mx
                mx = max(houses[i+1], houses[i+2])
            return max(houses[0], houses[1])
        return max(helper(nums[1:]), helper(nums[:-1]))