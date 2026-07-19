class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m = max(nums)
        mi = min(nums)
        return math.gcd(m,mi)