class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        result = n
        for i in range(n):
            l = nums[i]
            low, high = i, n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= l * k:
                    low = mid + 1
                else:
                    high = mid - 1
            result = min(result, i + (n - (high + 1)))
        return result
