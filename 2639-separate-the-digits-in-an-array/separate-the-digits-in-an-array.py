class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            for j in range(len(str(i))):
                l.append(int(str(i)[j]))
        return l