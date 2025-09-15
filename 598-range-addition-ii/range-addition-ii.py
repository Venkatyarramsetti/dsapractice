class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a = m
        b = n
        for x,y in ops:
            a = min(a,x)
            b = min(b,y)
        return a*b

        