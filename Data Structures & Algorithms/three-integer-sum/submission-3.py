class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## basically, i need 3 pointers
        ## 1 pointer will be a for loop
        ## then do 2 pointer with the rest of the right side
        ## this is possible because you already checked everything from
        ## ...the left side 

        check = lambda num: set(num)
        final = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while (l < r):
                if nums[i] + nums[l] + nums[r] == 0:
                    if set([nums[i], nums[l], nums[r]]) not in map(check, final):
                        final.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return final
            


        
                
