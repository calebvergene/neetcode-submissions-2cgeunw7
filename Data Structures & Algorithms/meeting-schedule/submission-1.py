"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # SORT FIRST 
        intervals.sort(key=lambda x : x.start)
        for m in range(len(intervals)-1):
            if intervals[m].end > intervals[m+1].start:
                return False
        return True
