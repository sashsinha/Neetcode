import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, count in collections.Counter(nums).items():
            buckets[count].append(val)
        ans = []
        for elements in reversed(buckets):
            if elements: 
                ans.extend(elements)
            if len(ans) >= k:
                return ans[:k]