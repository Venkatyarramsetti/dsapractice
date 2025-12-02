from collections import defaultdict

class Solution:
    def countTrapezoids(self, p: list[list[int]]) -> int:
        M = 10**9 + 7
        l = defaultdict(int)
        for x, y in p:
            l[y] += 1
        ll = []
        for c in l.values():
            if c >= 2:
                ll.append(c * (c - 1) // 2)
        r = s = 0
        for a in ll:
            r = (r + a * s) % M
            s = (s + a) % M
        return r
