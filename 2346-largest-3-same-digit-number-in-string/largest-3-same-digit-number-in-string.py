class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = ("999","888","777","666","555","444","333","222","111","000")
        t = -1
        for i in range(len(num)):
            k = num[i:i+3]
            if k in l:
                t = max(t,int(k))
        if t != -1:
            if t == 0:
                return str(t) + "00"
            return str(t)
        else:
            return ""