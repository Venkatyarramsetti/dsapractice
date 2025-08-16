class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        nums.sort(key = lambda x:x*10,reverse=True)
        r = ''.join(nums)
        return "0" if r[0] == '0' else r