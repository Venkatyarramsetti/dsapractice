class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        l = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                for k in range(i + 1, j):
                    l[i][j] = min(l[i][j] if l[i][j] != 0 else float("inf"),
                        l[i][k] + values[i] * values[k] * values[j] + l[k][j])
        return l[0][n - 1]