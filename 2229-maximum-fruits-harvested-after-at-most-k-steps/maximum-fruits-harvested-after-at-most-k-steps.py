class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        l = total = c = 0
        for right in range(len(fruits)):
            total += fruits[right][1]
            while l <= right and min(
                abs(startPos - fruits[l][0]) + fruits[right][0] - fruits[l][0],
                abs(startPos - fruits[right][0]) + fruits[right][0] - fruits[l][0]
            ) > k:
                total -= fruits[l][1]
                l += 1
            c = max(c, total)
        return c