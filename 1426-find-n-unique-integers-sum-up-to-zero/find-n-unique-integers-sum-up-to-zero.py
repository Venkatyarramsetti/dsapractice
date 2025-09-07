class Solution:
    def sumZero(self, n: int) -> List[int]:
        i,j = 0,n-1
        e=1
        l = [0]*(n)
        while i<j:
            l[i] = e
            l[j] = -e
            i += 1
            j -= 1
            e += 1
        return l