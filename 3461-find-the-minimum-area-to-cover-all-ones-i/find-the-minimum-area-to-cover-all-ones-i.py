class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        min_r, max_r = R, -1
        min_c, max_c = C, -1
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    min_r = min(min_r, r); max_r = max(max_r, r)
                    min_c = min(min_c, c); max_c = max(max_c, c)
        if max_r == -1:
            return 0
        return (max_r - min_r + 1) * (max_c - min_c + 1)