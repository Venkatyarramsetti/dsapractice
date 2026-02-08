class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        for i in range(n-1):
            k = nums[i+1:n]
            print(k)
            l=sum(k)//len(k)
            if nums[i] > l:
                c +=1
        return c