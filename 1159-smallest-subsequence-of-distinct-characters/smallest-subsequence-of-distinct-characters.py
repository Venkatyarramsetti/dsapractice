class Solution:
    def smallestSubsequence(self, st: str) -> str:
        c = Counter(st)
        s = []
        se = set()
        for i in st:
            c[i] -= 1
            if i in se:
                continue
            while s and s[-1]>i and c[s[-1]]:
                se.remove(s.pop())
            s.append(i)
            se.add(i)
        return "".join(s)