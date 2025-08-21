class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[i][j] = 1 + (heights[i-1][j] if i > 0 else 0)
        c = 0
        for i in range(m):
            for j in range(n):
                if heights[i][j] > 0:
                    min_height = heights[i][j]
                    for k in range(j, -1, -1):
                        if heights[i][k] == 0:
                            break
                        min_height = min(min_height, heights[i][k])
                        c += min_height
        return c