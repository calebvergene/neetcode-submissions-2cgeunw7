class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def isPeak(index, nums):
            if index <= 0 or nums[index-1] < nums[index]:
                if index+1 >= len(nums) or nums[index+1] < nums[index]:
                    return 0
                return 1
            return -1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if isPeak(mid, nums) == 0:
                return mid
            elif isPeak(mid, nums) == 1:
                l = mid + 1
            else:
                r = mid - 1
          
