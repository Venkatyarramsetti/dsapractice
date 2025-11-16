class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        su = 0
        m = 0
        for char in s:
            if char == '1':
                m += 1
                su = (su + m) % mod
            else:
                m = 0
        return su
        