class Solution:
    def smallestNumber(self, n: int) -> int:
        def fun(i):
            b = list(bin(i)[2:])
            s = set(b)
            return (len(s) == 1 and s.pop() == '1')
        a = 0
        while True:
            if fun(n):
                a = n
                break
            else:
                n += 1
        return a