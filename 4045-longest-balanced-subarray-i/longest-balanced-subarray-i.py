class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ec = set()
            oc = set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    ec.add(nums[j])
                else:
                    oc.add(nums[j])

                if len(ec) == len(oc):
                    ans = max(ans, j - i + 1)

        return ans