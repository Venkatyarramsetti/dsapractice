class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(set(nums)) == 1 and 1 in set(nums):
            return len(nums)-1
        l = 0
        zero_count = 0
        max_len = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > 1: 
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len - 1