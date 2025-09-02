class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        c = 0
        n = len(points)
        for i in range(n):
            uy = points[i][1]
            ly = float('-inf')
            for j in range(i + 1, n):
                cy = points[j][1]
                if cy <= uy and cy > ly:
                    c += 1
                    ly = cy
                    if cy == uy:
                        break
        return c