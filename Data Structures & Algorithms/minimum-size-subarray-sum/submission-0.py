class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # increment r pointer if less than target, l if greater than target 
        total = nums[0]
        min_len = float('inf')
        l, r = 0, 0 
        while r < len(nums):
            # r increments
            if total < target:
                r += 1
                if r < len(nums): total += nums[r]
            # l increments, so total is >= target
            else:
                # edge case: return if we hit minimum
                if l == r:
                    return 1
                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l += 1

        return min_len if min_len != float('inf') else 0
                