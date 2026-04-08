class Solution:
    def hammingWeight(self, n: int) -> int:
        # count the number of farthest right bits each iteration
        count = 0
        while n:
            n = n & (n-1)
            print(n)
            count += 1
        return count
        