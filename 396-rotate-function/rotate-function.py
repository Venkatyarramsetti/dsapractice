class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        s1 = 0
        for i in range(n):
            s += nums[i]
            s1 += i * nums[i]
        result = s1
        for k in range(1, n):
            s1 = s1 + s - n * nums[n - k]
            result = max(result, s1)
        
        return result