class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 1
        max_freq = 1

        window = 0
        while r < len(nums):
            # for each window, track how many increments needed for all nums to be r
            # if it exceeds k, then increment l (subtract r-l from total)
            window += (nums[r] - nums[r-1]) * (r-l)
            while window > k:
                window -= nums[r] - nums[l]
                l += 1
            # at this point, we have a legal window
            max_freq = max(max_freq, r - l + 1)
            r += 1
        
        return max_freq
