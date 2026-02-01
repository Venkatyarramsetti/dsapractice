class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        l1 = nums[0]
        nums[1:] = sorted(nums[1:])
        return l1 + nums[1] + nums[2]