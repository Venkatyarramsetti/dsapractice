class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min((f:=Counter(text))['b'], f['a'], f['l']//2, f['o']//2, f['n'] )