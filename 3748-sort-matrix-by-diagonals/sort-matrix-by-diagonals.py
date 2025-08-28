import heapq
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        d = {}

        for i in range(n):
            for j in range(m):
                key = i - j
                if key not in d: d[key] = []
                if key < 0: heapq.heappush(d[key], grid[i][j])
                else: heapq.heappush(d[key], -grid[i][j])

        for i in range(n):
            for j in range(m):
                key = i - j
                if key < 0: grid[i][j] = heapq.heappop(d[key])
                else: grid[i][j] = -heapq.heappop(d[key])
        return grid