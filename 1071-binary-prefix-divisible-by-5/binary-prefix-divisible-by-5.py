class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        l = 0
        for i in range(len(nums)):
            l = ((l << 1) + nums[i]) % 5
            nums[i] = l == 0
        return nums