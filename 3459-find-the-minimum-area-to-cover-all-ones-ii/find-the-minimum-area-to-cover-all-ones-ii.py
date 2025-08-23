class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        points = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 1]

        def rect_area(points):
            if not points: 
                return float('inf')
            min_r = min(r for r, _ in points)
            max_r = max(r for r, _ in points)
            min_c = min(c for _, c in points)
            max_c = max(c for _, c in points)
            return (max_r - min_r + 1) * (max_c - min_c + 1)

        best = float('inf')

        for c1 in range(m - 2):
            for c2 in range(c1 + 1, m - 1):
                g1 = [(r, c) for r, c in points if c <= c1]
                g2 = [(r, c) for r, c in points if c1 < c <= c2]
                g3 = [(r, c) for r, c in points if c > c2]
                if not g1 or not g2 or not g3: 
                    continue
                best = min(best, rect_area(g1) + rect_area(g2) + rect_area(g3))

        for r1 in range(n - 2):
            for r2 in range(r1 + 1, n - 1):
                g1 = [(r, c) for r, c in points if r <= r1]
                g2 = [(r, c) for r, c in points if r1 < r <= r2]
                g3 = [(r, c) for r, c in points if r > r2]
                if not g1 or not g2 or not g3:
                    continue
                best = min(best, rect_area(g1) + rect_area(g2) + rect_area(g3))

        for r in range(n - 1):
            top = [(rr, cc) for rr, cc in points if rr <= r]
            bottom = [(rr, cc) for rr, cc in points if rr > r]
            if not top or not bottom: 
                continue
            for c in range(m - 1):
                g2 = [(rr, cc) for rr, cc in bottom if cc <= c]
                g3 = [(rr, cc) for rr, cc in bottom if cc > c]
                if not g2 or not g3:
                    continue
                best = min(best, rect_area(top) + rect_area(g2) + rect_area(g3))
        for r in range(n - 1):
            top = [(rr, cc) for rr, cc in points if rr <= r]
            bottom = [(rr, cc) for rr, cc in points if rr > r]
            if not top or not bottom: 
                continue
            for c in range(m - 1):
                g2 = [(rr, cc) for rr, cc in top if cc <= c]
                g3 = [(rr, cc) for rr, cc in top if cc > c]
                if not g2 or not g3:
                    continue
                best = min(best, rect_area(bottom) + rect_area(g2) + rect_area(g3))
        for c in range(m - 1):
            left = [(rr, cc) for rr, cc in points if cc <= c]
            right = [(rr, cc) for rr, cc in points if cc > c]
            if not left or not right: 
                continue
            for r in range(n - 1):
                g2 = [(rr, cc) for rr, cc in right if rr <= r]
                g3 = [(rr, cc) for rr, cc in right if rr > r]
                if not g2 or not g3:
                    continue
                best = min(best, rect_area(left) + rect_area(g2) + rect_area(g3))
        for c in range(m - 1):
            left = [(rr, cc) for rr, cc in points if cc <= c]
            right = [(rr, cc) for rr, cc in points if cc > c]
            if not left or not right: 
                continue
            for r in range(n - 1):
                g2 = [(rr, cc) for rr, cc in left if rr <= r]
                g3 = [(rr, cc) for rr, cc in left if rr > r]
                if not g2 or not g3:
                    continue
                best = min(best, rect_area(right) + rect_area(g2) + rect_area(g3))

        return best