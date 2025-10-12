from functools import lru_cache
MOD = 10**9 + 7
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        pn = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                pn[i][j] = pn[i][j - 1] * nums[i] % MOD
        C = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
        @lru_cache(None)
        def fun(pos, carry, used, ones):
            if pos == n:
                extra = bin(carry).count('1')
                return 1 if used == m and ones + extra == k else 0
            ans = 0
            for cnt in range(m - used + 1):
                total = carry + cnt
                bit = total & 1
                ncarry = total >> 1
                nones = ones + bit
                sub = fun(pos + 1, ncarry, used + cnt, nones)
                if not sub: 
                    continue
                ways = C[m - used][cnt]
                prod = pn[pos][cnt]
                ans = (ans + sub * ways % MOD * prod) % MOD
            return ans
        return fun(0, 0, 0, 0)