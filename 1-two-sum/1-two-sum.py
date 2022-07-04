class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_compliment_idx = {}
        for idx, num in enumerate(nums):
            if num in num_to_compliment_idx:
                return [num_to_compliment_idx[num], idx]
            num_to_compliment_idx[target - num] = idx
        return [-1, -1]
