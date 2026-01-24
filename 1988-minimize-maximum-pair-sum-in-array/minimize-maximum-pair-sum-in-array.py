class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        m = 0
        while i<=j:
            if nums[i] + nums[j] > m:
                m = max(m,nums[i]+nums[j])
            i += 1
            j -=1
        return m