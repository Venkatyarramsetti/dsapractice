class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        if k % 2 == 0 or k % 5 == 0:
            return -1
        c = 0
        for i in range(1, k + 1):
            c = (c * 10 + 1) % k
            if c == 0:
                return i
        
        return -1