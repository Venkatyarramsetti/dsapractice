class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = []
        o = 0
        for i in range(len(nums)):
            while l and l[-1] > nums[i]:
                l.pop()  
            if nums[i] == 0:
                continue
            if not l or l[-1] <nums[i]:
                o +=1
                l.append(nums[i])
        return o