class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        an = []
        for num in nums:
            found = False
            for ans in range(num + 1):
                if ans | (ans + 1) == num:
                    an.append(ans)
                    found = True
                    break
            if not found:
                an.append(-1)
        return an