class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        c = 0
        while any(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):
            s = float('inf')
            mi = -1
            for i in range(len(nums) - 1):
                iss = nums[i] + nums[i + 1]
                if iss < s:
                    s = iss
                    mi = i
            nums[mi] = s
            del nums[mi + 1]
            c += 1
        return c