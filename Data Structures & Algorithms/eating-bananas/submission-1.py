class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            hours = 0 
            for pile in piles:
                hours += math.ceil(pile/mid)
            # would take less hours than required, so rate is valid
            # rate too slow
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
        # whenever you binary search for a range, l ends up on the minimum right
        return l