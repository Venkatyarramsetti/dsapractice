class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        s = ""
        for i in words:
            total = 0
            for ch in i:
                total += weights[ord(ch) - ord('a')]
            mod = total % 26
            c = chr(ord('z') - mod)
            s += c
        return s