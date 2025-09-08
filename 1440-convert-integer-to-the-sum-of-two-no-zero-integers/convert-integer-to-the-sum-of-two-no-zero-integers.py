class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def fun(n):
            l = list(str(n))
            m = l.count("0")
            if m>0:
                return False
            else:
                return True
        for i in range(1,n):
            a = i
            b = n-i
            if fun(a) and fun(b):
                return [a,b]
                break
        return -1