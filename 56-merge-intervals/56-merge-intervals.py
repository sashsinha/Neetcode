class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: i[0])
        merged = [intervals[0]]
        for interval in intervals[1:]:
            start, end = interval
            if start > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
