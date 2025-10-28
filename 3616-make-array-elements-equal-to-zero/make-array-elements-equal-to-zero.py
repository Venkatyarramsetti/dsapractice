class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        valid = 0
        n = len(nums)

        def fun(c, d):
            arr = nums[:]
            dir = d
            while 0 <= c < n:
                if arr[c] == 0:
                    c += dir
                else:
                    arr[c] -= 1
                    dir *= -1
                    c += dir
            return all(x == 0 for x in arr)

        for i in range(n):
            if nums[i] == 0:
                if fun(i, 1):
                    valid += 1
                if fun(i, -1):
                    valid += 1

        return valid
