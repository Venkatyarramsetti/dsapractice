class Solution:
    def findFinalValue(self, nums: List[int], o: int) -> int:
        if o not in nums: return o
        else:
            while True:
                if o in nums:
                    o *= 2
                else:
                    break
            return o