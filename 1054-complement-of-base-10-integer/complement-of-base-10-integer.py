class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        s = ""
        for i in b:
            if i == "1":
                s += "0"
            else:
                s += "1"
        return int(s,2)