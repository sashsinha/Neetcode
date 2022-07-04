import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numToComplimentIdx = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (numToComplimentIdx.containsKey(nums[i])) {
                return new int[] {numToComplimentIdx.get(nums[i]), i};
            }   
            numToComplimentIdx.put(target - nums[i], i);
        }
        return new int[]{-1, -1};
    }
}