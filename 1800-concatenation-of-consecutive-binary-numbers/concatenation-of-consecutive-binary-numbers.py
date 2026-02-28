mod = 10**9+7
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ""
        for i in range(1,n+1):
            s += bin(i)[2:]
        k = int(s,2) % mod
        return k