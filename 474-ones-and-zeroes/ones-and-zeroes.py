class Solution:
    def findMaxForm(self, s: List[str], m: int, n: int) -> int:
        d = {}
        def fun(i,m,n):
            if i == len(s):
                return 0
            if (i,m,n) in d:
                return d[(i,m,n)]
            
            mc,nc = s[i].count("0"),s[i].count("1")
            d[(i,m,n)] = fun(i+1,m,n)
            if mc<=m and nc<=n:
                d[(i,m,n)] = max(d[(i,m,n)] ,1 + fun(i+1,m-mc,n-nc))
            return d[(i,m,n)]
        return fun(0,m,n)