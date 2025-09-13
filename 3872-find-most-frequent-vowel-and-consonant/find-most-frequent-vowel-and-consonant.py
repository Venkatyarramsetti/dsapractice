from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        f = Counter(s)
        m1,m2 = 0,0
        s1 = {'a','e','i','o','u'}
        for i,n in f.items():
            if i in  s1:
                if n>m1:
                    m1 = n
            else:
                if n>m2:
                    m2 = n
        return m1+m2