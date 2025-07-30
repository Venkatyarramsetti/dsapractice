class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = []
        l1 = []
        for i in range(len(s)):
            if s[i] == c:
                l.append(i)
        for i in range(len(s)):
            check=[]
            for j in l:
                check.append(abs(i-j))
            l1.append(min(check))

        return l1