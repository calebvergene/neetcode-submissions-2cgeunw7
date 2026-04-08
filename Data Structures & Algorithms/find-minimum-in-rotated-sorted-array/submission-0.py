class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## two cases:
        # 1. min is at the start, and rotated = 0 or len
        # 2. more likely: need to find the split where l > r

        # case 1:
        if nums[0] <= nums[len(nums)-1]:
            return nums[0]

        # case 2:
        # find the split then return split + 1
        l, r = 0, len(nums)-1
        mid = (r + l) // 2
        print(mid)
        while (nums[mid] <= nums[mid + 1]):
            mid = (r + l) // 2
            if nums[0] <= nums[mid]:
                l = mid
            elif nums[0] > nums[mid]:
                r = mid
        return nums[mid + 1]
