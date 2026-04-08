class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0 
        count = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                count += 1
                nums.pop(i)
                end -= 1
                continue
            i += 1
        
        for j in range(count):
            nums.append(0)
        
        return nums
