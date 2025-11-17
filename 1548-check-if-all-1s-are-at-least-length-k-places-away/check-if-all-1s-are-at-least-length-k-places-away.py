class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0: return True
        l = []
        for i in range(len(nums)):
            if nums[i] == 1:
                l.append(i)
        if len(l) <= 1: return True
        c = 0
        for i in range(1,len(l)):
            if l[i] - l[i-1]-1 >= k:
                c += 1
        return c == len(l)-1