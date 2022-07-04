import java.util.HashMap;
import java.util.Map;

class Solution {
    public Map<Character, Integer> getCharCounts(String s) {
        Map<Character, Integer> charCounts = new HashMap<>();
        for (Character ch : s.toCharArray()) {
            charCounts.put(ch, charCounts.getOrDefault(ch, 0) + 1);
        }
        return charCounts;
    }
    
    public boolean isAnagram(String s, String t) {
        return getCharCounts(s).equals(getCharCounts(t));
    }
}