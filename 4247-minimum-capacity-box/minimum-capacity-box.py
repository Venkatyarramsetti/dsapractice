class Solution:
    def minimumIndex(self, ca: list[int], it: int) -> int:
        ans = float('inf')
        ind = -1
        for i in range(len(ca)):
            if ca[i] >= it and ca[i] < ans:
                ans = ca[i]
                ind = i
        return ind 