class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []
        nums.sort()
        def backtrack_sum(current, list_sum, nums):
            # base case
            if list_sum == target:
                sums.append(current[:])
                return
            elif list_sum > target:
                return

            for i in range(len(nums)):
                current.append(nums[i])
                list_sum += nums[i]

                backtrack_sum(current, list_sum, nums[i:])
                sub = current.pop()
                list_sum -= sub
        backtrack_sum([], 0, nums)
        return sums
            
            
