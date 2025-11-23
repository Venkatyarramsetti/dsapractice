class Solution:
    def maxSumDivThree(self, arr: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]

        for x in arr:
            temp = dp[:]  
            for r in range(3):
                nr = (r + x) % 3
                dp[nr] = max(dp[nr], temp[r] + x)

        return dp[0]
