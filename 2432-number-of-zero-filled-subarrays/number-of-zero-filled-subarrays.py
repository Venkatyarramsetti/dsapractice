class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c, i = 0, 0
        for num in nums:
            if num == 0:
                i += 1
                c += i
            else:
                i = 0
        return c