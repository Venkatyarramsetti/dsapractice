class Solution:
    def successfulPairs(self, s: List[int], p: List[int], su: int) -> List[int]:
        p.sort()
        n = len(p)
        l = []

        for i in s:
            m = (su + i - 1) // i
            idx = bisect_left(p, m)
            l.append(n - idx)

        return l