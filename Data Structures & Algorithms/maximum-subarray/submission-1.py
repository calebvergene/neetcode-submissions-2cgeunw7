class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # just two pointer thru the array and if the total sum
        # becomes negative, then increment the left pointer because
        # it doesn't benefit you at all. 
        max_sum = nums[0]
        window = 0
        for i in nums:
            window += i
            max_sum = max(max_sum, window)
            if window < 0:
                window = 0

        return max_sum
                