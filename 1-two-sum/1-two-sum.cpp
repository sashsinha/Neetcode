#include <unordered_map>
#include <vector>

class Solution {
 public:
  std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> num_to_compliment_idx;
    for (int i = 0; i < nums.size(); i++) {
      if (num_to_compliment_idx.count(nums[i])) {
        return {num_to_compliment_idx[nums[i]], i};
      }
      num_to_compliment_idx[target - nums[i]] = i;
    }
    return {-1, -1};
  }
};
