import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        li = []
        m = -1
        for i in nums:
            m = max(m, i)
            li.append(math.gcd(i, m))
        li.sort()
        l, r = 0, n - 1
        c = 0
        while l < r:
            c += math.gcd(li[l], li[r])
            l += 1
            r -= 1
        return c