#include <unordered_set>
#include <vector>

class Solution {
 public:
  bool containsDuplicate(std::vector<int>& nums) {
    std::unordered_set<int> nums_set;
    for (int x : nums) {
      if (nums_set.count(x)) {
        return true;
      }
      nums_set.insert(x);
    }
    return false;
  }
};
