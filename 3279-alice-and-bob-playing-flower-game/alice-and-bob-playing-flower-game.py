class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        en = n//2
        on = (m+1)//2
        c1 = en*on
        em = m//2
        om = (n+1)//2
        c2=em*om
        return c1+c2