class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a monotonic deque
        r, l = 0, 0
        q = collections.deque()
        res = []

        # go through nums. start incrementing l when r - l is the size of k. 
        # THE LARGEST WILL ALWAYS BE AT THE LEFT. 
        while r < len(nums):
            # pop while new num is bigger
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            r += 1
            if r - l >= k:
                # then we have the window. 
                res.append(q[0]) 
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
        return res        
            


        # need to:
        # increase l when gap is size k
        # remove l num from q when it gets passed by l 
        # process the largest number and add it to res 


