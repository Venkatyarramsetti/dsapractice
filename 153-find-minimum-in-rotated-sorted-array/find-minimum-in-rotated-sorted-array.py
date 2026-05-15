class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums == nums.sort():
            return nums[0]
        k = 0
        l1 = nums[:]
        l = sorted(nums)
        for i in range(len(l1)):
            kk = l1[-i:]+l1[:-i]
            if kk == l:
                k = i
                break
        return nums[k]