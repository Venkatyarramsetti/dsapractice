from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        n, m = len(mat), len(mat[0])
        r, c = 0, 0
        up = True
        l = []

        while len(l) < n * m:
            if up:
                while r >= 0 and c < m:
                    l.append(mat[r][c])
                    r -= 1
                    c += 1
                if c == m:
                    r += 2
                    c -= 1
                else:
                    r += 1
            else:
                while c >= 0 and r < n:
                    l.append(mat[r][c])
                    r += 1
                    c -= 1
                if r == n:
                    c += 2
                    r -= 1
                else:
                    c += 1
            up = not up

        return l
