class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i) - ord(target) > 0:
                return i
                break
        return letters[0]