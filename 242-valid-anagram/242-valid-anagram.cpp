#include <unordered_map>
#include <string>

class Solution {
 public:
  std::unordered_map<char, int> getCharCounts(const std::string& s) {
    std::unordered_map<char, int> char_counts;
    for (const char& c : s) {
      char_counts[c]++;
    }
    return char_counts;
  }

  bool isAnagram(std::string s, std::string t) {
    if (s.length() != t.length()) {
      return false;
    }
    return getCharCounts(s) == getCharCounts(t);
  }
};
