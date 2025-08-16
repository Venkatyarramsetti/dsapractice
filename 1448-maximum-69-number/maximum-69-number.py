class Solution:
    def maximum69Number (self, num: int) -> int:
        l = list(map(int, str(num)))
        i = 0
        ln = len(l)
        while(i<ln):
            if l[i] == 6:
                l[i] = 9
                n = int("".join(map(str, l)))
                return n
            i = i+1
        return num 