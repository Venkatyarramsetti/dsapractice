class Solution:
    def sortColors(self, nums: List[int]) -> None:
        k =0
        l = [0]*(len(nums))
        for i in range(len(nums)):
            if nums[i] == 0:
                l[k] = 0
                k+=1
        for i in range(len(nums)):
            if nums[i] == 1:
                l[k] = 1
                k+=1
        for i in range(len(nums)):
            if nums[i] == 2:
                l[k] = 2
                k+=1
        for i in range(len(l)):
            nums[i] = l[i]
        """
        Do not return anything, modify nums in-place instead.
        """
        