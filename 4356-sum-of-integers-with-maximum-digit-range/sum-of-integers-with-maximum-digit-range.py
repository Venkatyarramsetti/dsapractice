class Solution:
    def fun(self, num: int) -> int:
        if num == 0:
            return 0
        mx = 0
        mn = 9
        while num > 0:
            digit = num % 10
            mx = max(mx, digit)
            mn = min(mn, digit)
            num //= 10
        return mx - mn
    def maxDigitRange(self, nums: list[int]) -> int:
        mr = -1
        for num in nums:
            mr = max(mr, self.fun(num))
        t = 0
        for num in nums:
            if self.fun(num) == mr:
                t += num
        return t