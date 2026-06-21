class Solution {
    public int largestAltitude(int[] gain) {
        int temp = 0;
        int ans = 0;
        for(int i:gain){
            temp += i;
            ans = Math.max(ans,temp); 
        }
        return ans;
    }
}