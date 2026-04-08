class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # basically you just have to find pairs of weights < limit

        # i can sort, then two pointer: O(nlogn)
        people.sort()
        # l = 0 (min) and r = len
        l, r = 0, len(people)-1

        # then find pairs that <= limit and track how many people you put on boat.
        # this ensures all possible pairs are made. two pointer perfect for this. 
        onboat = 0
        while l < r:
            # if weight > limit, move r down. 
            if people[l] + people[r] > limit:
                r -= 1
            # if weight < limit, add people and increment l and r. 
            else:
                onboat += 2
                l += 1
                r -= 1
            
        # need n boats for the n people left
        left = len(people) - onboat
        return left + onboat//2


