class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        f = False
        for i in range(len(s)):
            s1 = s[-i:] + s[:-i]
            if s1 == goal:
                f = True
                break
        return f