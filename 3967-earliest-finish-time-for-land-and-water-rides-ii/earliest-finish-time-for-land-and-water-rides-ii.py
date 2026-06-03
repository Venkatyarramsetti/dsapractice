from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def f(a, b, c, e):
            n, m = len(a), len(c)
            if n == 0 or m == 0:
                return float('inf')
            u = sorted(zip(c, e))
            z = [0] * m
            z[-1] = u[-1][0] + u[-1][1]
            for i in range(m - 2, -1, -1):
                z[i] = min(z[i + 1], u[i][0] + u[i][1])
            y = [0] * m
            y[0] = u[0][1]
            for i in range(1, m):
                y[i] = min(y[i - 1], u[i][1])
            r = float('inf')
            for i in range(n):
                x = a[i] + b[i]
                l, h = 0, m
                while l < h:
                    j = (l + h) // 2
                    if u[j][0] > x:
                        h = j
                    else:
                        l = j + 1
                k = l
                if k > 0:
                    r = min(r, x + y[k - 1])
                if k < m:
                    r = min(r, z[k])
            return r

        return min(f(landStartTime, landDuration, waterStartTime, waterDuration),
                   f(waterStartTime, waterDuration, landStartTime, landDuration))
