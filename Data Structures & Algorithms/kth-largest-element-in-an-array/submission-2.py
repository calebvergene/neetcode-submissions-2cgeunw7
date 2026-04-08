class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l, r):
            pivot = (l + r) // 2
            # move pivot to the end
            nums[r], nums[pivot] = nums[pivot], nums[r]
            mid = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[mid], nums[i] = nums[i], nums[mid]
                    mid += 1
            # now pivot in the correct sorted position
            nums[mid], nums[r] = nums[r], nums[mid]

            if mid == len(nums)-k:
                return nums[mid]
            elif mid < len(nums)-k:
                return quickSelect(mid+1, r)
            else:
                return quickSelect(l, mid-1)
        return quickSelect(0, len(nums)-1)
