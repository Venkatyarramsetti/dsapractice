class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        t = c = 0
        for i in target:
            if i > c:
                t += i - c
            c = i
        return t