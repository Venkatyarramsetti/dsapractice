class Solution:
    def maximumEnergy(self, e: List[int], k: int) -> int:
        n = len(e)
        r = float("-inf")
        l = [0]*n
        for i in range(n-1,-1,-1):
            if i+k<n:
                l[i] = l[i+k]+e[i]
            else:
                l[i] = e[i]+0
            r = max(r,l[i])
        return r