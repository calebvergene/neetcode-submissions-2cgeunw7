class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # min would be max weight, max would be total weights
        # min : we could use infinite ships, max: only 1 ship
        l, r = max(weights), sum(weights)

        while l <= r:
            # so we test this capacity 
            capacity = (l + r) // 2

            # test to see if this capacity works 
            curr, ships = 0, 0
            for weight in weights:
                # too heavy, need another ship
                if weight + curr > capacity:
                    curr = weight
                    ships += 1
                else:
                    curr += weight

            # now, we binary search based off number of ships we needed 
            if ships < days: 
                # cap too high
                r = capacity - 1
            else:
                l = capacity + 1
            
        return l