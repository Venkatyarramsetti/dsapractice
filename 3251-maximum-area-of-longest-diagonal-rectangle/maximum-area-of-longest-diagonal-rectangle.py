import math
from typing import List

class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
        l, a = 0, 0
        for i in range(len(d)):
            k = math.sqrt(d[i][0] * d[i][0] + d[i][1] * d[i][1])
            m = d[i][0] * d[i][1]
            if k > l:  
                l = k
                a = m
            elif k == l:
                a = max(a, m)
        return a
