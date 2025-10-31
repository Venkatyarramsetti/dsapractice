class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l =[]
        c = Counter(nums)
        for a,i in c.items():
            if i > 1:
                l.append(a)
        return l
        