class Solution {
    public int minimumDistance(int[] nums) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }

        int ans = Integer.MAX_VALUE;
        for (List<Integer> list : map.values()) {
            if (list.size() >= 3) {
                for (int i = 0; i <= list.size() - 3; i++) {
                    int p = list.get(i);
                    int r = list.get(i + 2);

                    ans = Math.min(ans, 2 * (r - p));
                }
            }
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}