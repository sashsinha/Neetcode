public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        var insertIndex = m + n - 1;
        while (insertIndex >= 0) {
            if (m - 1 >= 0 && n - 1 >= 0) {
                if (nums1[m - 1] >= nums2[n - 1]) {
                    nums1[insertIndex--] = nums1[m - 1];
                    m--;
                } else {
                    nums1[insertIndex--] = nums2[n - 1];
                    n--;
                }
            } else if (m - 1 >= 0) {
                return;
            } else {
                nums1[insertIndex--] = nums2[n - 1];
                n--;
            }
        }
    }
}