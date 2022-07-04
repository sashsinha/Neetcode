class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        longest = 0
        start = 0
        for i, ch in enumerate(s):
            if ch in last_seen:
                start = max(last_seen[ch] + 1, start)
            longest = max(longest, i - start + 1)
            last_seen[ch] = i
        return longest
