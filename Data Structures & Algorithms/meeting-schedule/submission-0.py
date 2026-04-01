"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        meetings = []

        for obj in intervals:
            meetings.append((obj.start, obj.end))

        meetings.sort()

        for i in range(len(meetings)-1):
            start, end = meetings[i]
            next_start, next_end = meetings[i+1]

            # check overlap:

            if start < next_end and end > next_start:
                return False
        return True