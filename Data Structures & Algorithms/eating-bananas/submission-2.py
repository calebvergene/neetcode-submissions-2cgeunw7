class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k is the l and r for binary search
        # function to simulate 


        # first, find l and r 
        # given infinite hours, you can have k = 1
        # given small # of hours, need k = biggest pile
        l, r = 1, max(piles)

        def simulate_koko(k):
            # return true or false if koko eats all bananase
            # at k rate within h hours 
            total = 0
            for p in piles:
                total += math.ceil(p/k)
            if total > h: 
                return False
            return True

        # now simulate l and r with binary search. 
        # end on the least k that works, so return l
        while l <= r:
            mid = (l+r)//2
            success = simulate_koko(mid) # ate all bananas?
            if success:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
