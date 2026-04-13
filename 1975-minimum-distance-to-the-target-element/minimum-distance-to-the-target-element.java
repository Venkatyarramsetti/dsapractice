class Solution {
    public int getMinDistance(int[] nums, int target, int start) {
        int k = Integer.MAX_VALUE;
        for(int i = 0;i<nums.length;i++)
        {
            if(nums[i] == target){
                k = Math.min(k,Math.abs(i-start));
            }
        }
        return k;
    }
}