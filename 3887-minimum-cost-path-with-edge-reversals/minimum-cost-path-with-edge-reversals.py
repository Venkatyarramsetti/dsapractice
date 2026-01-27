class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        l = defaultdict(list)
        ll = defaultdict(list)
        for u, v, w in edges:
            l[u].append((v, w))
            ll[v].append((u, w))
        
        INF = float("inf")
        d = [[INF, INF] for _ in range(n)] 
        d[0][0] = 0
        mo = [(0, 0, 0)]
        while mo:
            cost, u, flag = heapq.heappop(mo)
            if d[u][flag] < cost:
                continue
            if u == n - 1:
                return cost
            for v, w in l[u]:
                nc = cost + w
                if nc < d[v][0]:
                    d[v][0] = nc
                    heapq.heappush(mo, (nc, v, 0))
            for v, w in ll[u]:
                nc = cost + 2 * w
                if nc < d[v][1]:
                    d[v][1] = nc
                    heapq.heappush(mo, (nc, v, 1))
        return -1
