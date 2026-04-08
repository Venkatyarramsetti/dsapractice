class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for i in range(len(queries)):
            k = queries[i][0]
            while k<=queries[i][1]:
                nums[k] = (nums[k]*queries[i][3]) %((10**9)+7)
                k += queries[i][2]
        c = 0
        for i in nums:
            c ^= i
        return c