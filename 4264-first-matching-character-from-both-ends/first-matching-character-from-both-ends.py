class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        f = float('inf')
        n = len(s)
        for i in range(n):
            if s[i] == s[n-i-1]:
                f = min(f,i)
        return -1 if f==float('inf') else f
