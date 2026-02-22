class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        d = 0
        i = 0
        j = 1
        while i<len(s) and j<len(s):
            if s[i] != '1': 
                i += 1
                j = i + 1
            elif s[j] == '0':
                j += 1
            else:
                d = max(d, j - i)
                i = j
                j = i + 1  
        return d
