class Solution:
    def tribonacci(self, n: int) -> int:

        #cache = [0,1,1] + [-1] * (n-2)
        if n == 2 or n==1: return 1
        elif n == 0: return 0

        # dont need a cache for this because we only need past 3 nums
        num0, num1, num2 = 0, 1, 1
        for _ in range(n-2):
            temp2 = num0 + num1 + num2
            
            num0 = num1
            num1 = num2
            num2 = temp2
        
        return num2



        