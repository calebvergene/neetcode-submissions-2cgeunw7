class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        l = 0
        while l < len(nums)-2:
            # now two pointer 
            m, r = l + 1, len(nums)-1
            while m < r:
                res = nums[l] + nums[m] + nums[r]
                if res == 0:
                    final.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m-1]:
                        m += 1
                elif res < 0:
                    m += 1
                    while m < r and nums[m] == nums[m-1]:
                        m += 1
                else:
                    r -= 1
            # increase l until new number
            l += 1
            while l < len(nums)-2 and nums[l] == nums[l-1]:
                l += 1
        return final
                
