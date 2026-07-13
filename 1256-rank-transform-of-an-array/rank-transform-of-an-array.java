import java.util.*;
class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int[] sorted = arr.clone();
        Arrays.sort(sorted);
        Map<Integer, Integer> l = new HashMap<>();
        int r = 1;
        for (int x : sorted) {
            if (!l.containsKey(x)) {
                l.put(x, r++);
            }
        }
        int[] ans = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            ans[i] = l.get(arr[i]);
        }

        return ans;
    }
}