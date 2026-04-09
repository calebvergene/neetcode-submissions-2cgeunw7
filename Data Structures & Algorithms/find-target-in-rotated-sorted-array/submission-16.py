class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # start, pivot, and end. 
        # if we find a number on the left > than one on the right = pivot
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        
        def bsearch(l, r):
            while l <= r:
                mid = (l+r)//2
                # we know we past pivot if mid < l
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        # 1. find the two pivot numbers. 
        l, r = 0, len(nums)-1
        if nums[0] < nums[-1]:
            # n = 6, no pivot 
            return bsearch(l, r)
        else:
            while l <= r:
                mid = (l+r)//2
                # we know we past pivot if mid < l
                if nums[mid] < nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
            

        # 2. now we have the two seperated lists. binary search them. 
        print(r, l)
        if target >= nums[0] and target <= nums[r]:
            return bsearch(0, r)
        elif target <= nums[-1] and target >= nums[l]:
            return bsearch(l, len(nums)-1)
        return -1
