class Solution:
    def maxFrequency(self, nums: List[int], k: int, op: int) -> int:
        a = sorted(nums)
        z = Counter(nums)
        return max(max(min(bisect_right(a,v+k)-bisect_left(a,v-k)-z[v],op)+z[v],
        min(bisect_right(a,v+2*k)-i,op)) for i,v in enumerate(a))