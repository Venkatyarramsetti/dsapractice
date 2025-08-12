class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        s = sum(cost)
        s1 = 0
        for i in range(2,len(cost),3):
            s1 += cost[i]
        return s - s1