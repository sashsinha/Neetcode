class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        product = nums[0]
        for i in range(1, len(nums)):
            result[i] *= product
            product *= nums[i]
  
        product = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result
