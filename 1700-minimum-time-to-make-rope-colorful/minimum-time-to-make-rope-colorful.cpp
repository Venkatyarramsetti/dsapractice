class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int t = 0;
        int m = neededTime[0];
        for(int i=1;i<colors.length();i++){
            if(colors[i] != colors[i-1]){
                m = neededTime[i];
            }
            else{
                t += min(m,neededTime[i]);
                m = max(m,neededTime[i]);
            }
        }
        return t;
    }
};