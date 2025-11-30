class Solution:
    def maxDistinct(self, s: str) -> int:
        ss=set(s)
        return len(ss)