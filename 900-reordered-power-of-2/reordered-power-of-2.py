class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def fun(n):
            return ''.join(sorted(str(n)))
        t = fun(n)
        for i in range(31):
            if fun(1 << i) == t:
                return True
        return False