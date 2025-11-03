class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        t, c = 0, 0
        for i in range(len(colors)):
            if colors[i] != colors[i - 1]:
                c = 0
            t += min(c, neededTime[i])
            c = max(c, neededTime[i])
        return t