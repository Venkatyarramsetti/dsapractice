class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        l = list(map(int,s))
        f = True
        for i in range(len(l)-1):
            if abs(l[i] - l[i+1]) > 2:
                f = False
                break
        return f