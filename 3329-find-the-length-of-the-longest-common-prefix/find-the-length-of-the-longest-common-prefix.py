class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        l = set()
        for j in arr1:
            s = str(j)
            for i in range(1, len(s) + 1):
                l.add(s[:i])
        c = 0
        for j in arr2:
            s = str(j)
            for i in range(1, len(s) + 1):
                if s[:i] in l:
                    c = max(c, i)
        return c