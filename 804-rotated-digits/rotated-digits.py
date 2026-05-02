class Solution:
    def rotatedDigits(self, n: int) -> int:
        l = [0] * (n+1)
        c = 0
        for i in range(n+1):
            if i <10:
                if i in (0, 1, 8):
                    l[i] = 1
                elif i in (2,5,6,9):
                    l[i] = 2
                    c += 1
                else:
                    l[i] = 0
            else:
                a = l[i // 10]
                b = l[i % 10]
                if a == 1 and b == 1:
                    l[i] = 1
                elif a >= 1 and b >= 1:
                    l[i] = 2
                    c += 1
                else:
                    l[i] = 0
        return c