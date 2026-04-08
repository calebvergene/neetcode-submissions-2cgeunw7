class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## MY THOUGHT PROCESS: two points on either end of the list. 
        ## squeeze in the list with l and r going towards the middle. 
        ## if sum > target, then increase l, vice versa. 
        l, r = 0, len(numbers) - 1
        while True:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
            
