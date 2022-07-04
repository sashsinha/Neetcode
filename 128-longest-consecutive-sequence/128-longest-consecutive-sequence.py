class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen_nums = set(nums)
        longest_streak = 0
        for n in seen_nums:
            if n - 1 not in seen_nums:
                curr_n = n
                curr_streak = 1
                while curr_n + 1 in seen_nums:
                    curr_n += 1
                    curr_streak += 1
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak
