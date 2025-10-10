class Solution {
public:
        void solve(vector<int>& nums,vector<int>& l,vector<vector<int>>& re,int m){
            if(m == nums.size()){
                re.push_back(l);
                return;
            }
            l.push_back(nums[m]);
            solve(nums,l,re,m+1);
            l.pop_back();
            solve(nums,l,re,m+1);
        }
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<int> l;
        vector<vector<int>> re;
        solve(nums,l,re,0);
        return re;
    }
};