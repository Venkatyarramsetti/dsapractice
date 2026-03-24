class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        l = [[0]*m for _ in range(n)]
        suffix = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                l[i][j] = suffix
                suffix = (suffix * (grid[i][j] % MOD)) % MOD
        prefix = 1
        for i in range(n):
            for j in range(m):
                l[i][j] = (l[i][j] * prefix) % MOD
                prefix = (prefix * (grid[i][j] % MOD)) % MOD
        return l