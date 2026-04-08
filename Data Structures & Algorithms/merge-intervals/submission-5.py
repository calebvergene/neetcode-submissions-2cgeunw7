class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals by start
        intervals.sort(key=lambda interval: interval[0])

        res = []

        # overlap if end of before > start of next
        # each iteration, comparing interval you are about to add with interval[i]
        new = intervals[0]
        for i in range(len(intervals)):
            # bounds check and overlap
            if i+1 < len(intervals) and new[1] >= intervals[i+1][0]:
                new[1] = max(new[1], intervals[i+1][1])
            # doesn't overlap, then add to result
            else:
                res.append(new)
                if i+1 < len(intervals): 
                    new = intervals[i+1]
        
        return res



