class Solution:
    def jump(self, nums: List[int]) -> int:
        n, m, k = 0, 0, 0
        for i in range(len(nums) - 1):
            k = max(k, i + nums[i])
            if i == m:
                n += 1
                m = k
        return n