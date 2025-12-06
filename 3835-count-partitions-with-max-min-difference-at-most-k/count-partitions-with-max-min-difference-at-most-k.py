from collections import deque
MOD = 10**9 + 7

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,ss = [0] * (n + 1),[0] * (n + 2)
        l[0],ss[1] = 1,1
        q1 = deque()
        q2 = deque()
        le = 0
        for ri in range(1, n + 1):
            m = nums[ri - 1]
            while q1 and m < q1[-1]:
                q1.pop()
            q1.append(m)
            while q2 and m > q2[-1]:
                q2.pop()
            q2.append(m)
            while q2[0] - q1[0] > k:
                if nums[le] == q1[0]:
                    q1.popleft()
                if nums[le] == q2[0]:
                    q2.popleft()
                le += 1
            l[ri] = (ss[ri] - ss[le]) % MOD
            ss[ri + 1] = (ss[ri] + l[ri]) % MOD
        return l[n]