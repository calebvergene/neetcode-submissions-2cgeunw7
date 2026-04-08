class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suff = [], []

        for i in range(len(nums)):
            if i == 0:
                pref.append(1) 
                continue
            pref.append(nums[i-1]*pref[i-1])
        
        i = len(nums)-1
        suff = [0] * len(nums)
        while i >= 0:
            if i == len(nums)-1:
                suff[i] = 1 
                i -= 1
                continue
            suff[i] = nums[i+1]*suff[i+1]
            i -= 1

        final = []
        for i in range(len(nums)):
            final.append(pref[i] * suff[i])
        return final