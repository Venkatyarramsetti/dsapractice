MOD = 1_000_000_007
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        l = []
        i = 1
        while True:
            p = pow(i, x)
            if p > n:
                break
            l.append(p)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1
        for p in l:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]