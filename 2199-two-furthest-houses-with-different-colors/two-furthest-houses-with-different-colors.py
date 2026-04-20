class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        c = float('-inf')
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i] != colors[j]:
                    c = max(c,abs(i-j))
        return c