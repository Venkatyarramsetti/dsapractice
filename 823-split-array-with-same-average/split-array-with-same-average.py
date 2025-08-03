class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(i, k, target):
            if k == 0:
                return target == 0
            if i >= n:
                return False
            if dfs(i + 1, k, target):
                return True
            if dfs(i + 1, k - 1, target - nums[i]):
                return True
            return False
        for k in range(1, n // 2 + 1):
            if (total_sum * k) % n == 0:
                target = (total_sum * k) // n
                if dfs(0, k, target):
                    return True

        return False