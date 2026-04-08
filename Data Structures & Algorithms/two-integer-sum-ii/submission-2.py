class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## MY THOUGHT PROCESS:  have pointers on either side of list
        ## squeeze into the list and until you find two nums that 
        ## will add up to target. This way, the l and r pointers 
        ## will always l < r.

        l, r = 0, len(numbers) - 1

        while (l < r):
            t = numbers[l] + numbers[r]
            if t == target:
                return [l+1,r+1]
            elif (t < target):
                l += 1
            else:
                r -= 1