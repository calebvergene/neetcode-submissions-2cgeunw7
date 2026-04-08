class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up. 
        # find the maximum subsequence of each number from right to left
        tab = {len(nums)-1: 1} # add last num as base case
        final_max = 1
        for i in range(len(nums)-1, -1, -1):
            largest = 0
            for j in range(i+1, len(nums)):
                # iterate thru elements after i in the list
                if nums[i] < nums[j]:
                    largest = max(largest, tab[j])
                # if nothing larger after it, then default to 1
                tab[i] = largest + 1
                # always track the largest increasing subsequence
                final_max = max(final_max, largest + 1)
        return final_max
        