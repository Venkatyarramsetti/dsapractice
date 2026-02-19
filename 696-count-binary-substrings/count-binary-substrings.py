class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c = 0
        i = 0
        c1 = 1
        for j in range(1, len(s)):
            if s[j] == s[j - 1]: c1 += 1
            else:
                i = c1
                c1 = 1
            if c1 <= i: c += 1
        return c