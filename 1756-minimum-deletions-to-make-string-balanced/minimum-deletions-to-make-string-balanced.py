class Solution:
    def minimumDeletions(self, s: str) -> int:
        a,c = 0,0
        for i in s:
            if i == 'b':
                a += 1
            else:
                c = min(c+1,a)
        return c