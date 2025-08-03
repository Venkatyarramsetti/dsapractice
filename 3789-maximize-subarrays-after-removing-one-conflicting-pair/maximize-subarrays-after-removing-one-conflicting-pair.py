class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        ans = 0 
        le = [0, 0]
        li = [0] * (n + 1)
        for r in range(1, n + 1):
            for l in right[r]:
                if l > le[0]:
                    le = [l, le[0]]
                elif l > le[1]:
                    le = [le[0], l]
            ans += r - le[0]
            if le[0] > 0:
                li[le[0]] += le[0] - le[1]
        return ans + max(li)