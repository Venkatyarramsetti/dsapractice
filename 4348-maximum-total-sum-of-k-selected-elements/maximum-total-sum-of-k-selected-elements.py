class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        s = 0
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if i<k and mul !=0:
                s += (nums[i] * mul)
                mul -=1
            elif i<k:
                s += nums[i]
        return s