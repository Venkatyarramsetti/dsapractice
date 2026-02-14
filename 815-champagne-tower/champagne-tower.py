class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        l = [[0.0] * (i + 1) for i in range(101)]
        l[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if l[i][j] > 1:
                    overflow = l[i][j] - 1
                    l[i][j] = 1
                    l[i + 1][j] += overflow / 2
                    l[i + 1][j + 1] += overflow / 2
        return min(1, l[query_row][query_glass])