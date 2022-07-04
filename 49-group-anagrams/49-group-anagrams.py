import collections

class Solution:
    def get_char_counts_string(self, s: str) -> tuple[int, ...]:
        char_counts = [0] * 26
        for ch in s:
            char_counts[ord(ch) - ord('a')] += 1
        return tuple(char_counts)
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            groups[self.get_char_counts_string(s)].append(s)
        return groups.values()
