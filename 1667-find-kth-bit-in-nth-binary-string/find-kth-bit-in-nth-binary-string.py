class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev(s):
            return s[::-1]
        def inv(s):
            s1 = ""
            for i in s:
                if i == '1':
                    s1 += '0'
                else:
                    s1 += '1'
            return s1
        s1 = "0"
        i = 1
        while i < n:
            s2 = s1 + "1" + rev(inv(s1))
            s1 = s2
            i += 1
        
        return s1[k - 1]