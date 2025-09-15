class Solution:
    def canBeTypedWords(self, text: str, b: str) -> int:
        l = text.split()
        count = 0
        broken = set(b)
        
        for word in l:
            if all(ch not in broken for ch in word):
                count += 1
        return count