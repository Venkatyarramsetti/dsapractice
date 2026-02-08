class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        l = []
        for num in nums:
            l.append(num)
            while len(l) >= 2 and l[-1] == l[-2]:
                val = l.pop()
                l[-1] += val

        return l