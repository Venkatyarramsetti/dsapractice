class Solution:
    def toggleLightBulbs(self, b: list[int]) -> list[int]:
        f = Counter(b)
        l = []
        for i,n in f.items():
            if n%2 != 0:
                l.append(i)
        l.sort()
        return l