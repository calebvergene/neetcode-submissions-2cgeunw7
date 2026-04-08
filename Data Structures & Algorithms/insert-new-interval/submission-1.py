class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not len(intervals): return [newInterval]
        # problem is basically merging intervals

        i = 0
        result = []
        # find all intervals before that do not overlap with new
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # stopped at interval with overlap. now start merging
        # can stop after merging, because we know there are no original overlaps.
        if i < len(intervals): newInterval[0] = min(newInterval[0], intervals[i][0])
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result


        
