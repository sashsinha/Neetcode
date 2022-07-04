import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k for k, _ in collections.Counter(nums).most_common(k)]
