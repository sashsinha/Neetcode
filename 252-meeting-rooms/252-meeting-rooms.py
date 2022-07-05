class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda i: (i[0], i[1]))
        for prev, curr in zip(intervals[:-1], intervals[1:]):
            if curr[0] < prev[1]:
                return False
        return True
