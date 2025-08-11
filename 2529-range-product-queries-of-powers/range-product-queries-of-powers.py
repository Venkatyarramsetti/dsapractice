class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        l = []
        while n:
            lowBit = n & -n
            l.append(lowBit)
            n ^= lowBit

        size = len(l)
        l1 = [[0] * size for _ in range(size)]
        for row, val in enumerate(l):
            l1[row][row] = val
            for col in range(row + 1, size):
                l1[row][col] = (
                    l1[row][col - 1] * l[col] % (10**9 + 7)
                )

        return [l1[p][q] for p, q in queries]