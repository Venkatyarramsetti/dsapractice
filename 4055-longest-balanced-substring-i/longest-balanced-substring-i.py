class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        c = 0
        for i in range(n):
            f = defaultdict(int)
            l = 0
            max_f = 0
            for j in range(i, n):
                if f[s[j]] == 0:
                    l += 1
                f[s[j]] += 1
                max_f = max(max_f, f[s[j]])
                length = j - i + 1
                if length == l * max_f:
                    c = max(c, length)
        return c