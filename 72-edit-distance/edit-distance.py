class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1),len(word2)
        d = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            d[i][0] = i
        for i in range(m+1):
            d[0][i] = i
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = 1+min(d[i][j-1],d[i-1][j],d[i-1][j-1])
        return d[-1][-1]