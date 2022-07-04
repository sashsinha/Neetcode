import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            groups[''.join(sorted(s))].append(s)
        return groups.values()