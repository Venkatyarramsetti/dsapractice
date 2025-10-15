class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                l[i] = l[i - 1] + 1
        l1 = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                l1[i] = l1[i + 1] + 1
        c = 0
        for i in range(n - 1):
            k = min(l[i], l1[i + 1])
            c = max(c, k)
        return c