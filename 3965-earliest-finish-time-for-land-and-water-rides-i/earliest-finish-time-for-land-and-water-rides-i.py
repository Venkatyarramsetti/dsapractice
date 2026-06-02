from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                l1 = landStartTime[i]
                l2 = l1 + landDuration[i]
                w1 = max(l2, waterStartTime[j])
                f1 = w1 + waterDuration[j]
                res = min(res, f1)
                w2 = waterStartTime[j]
                w3 = w2 + waterDuration[j]
                l3 = max(w3, landStartTime[i])
                f2 = l3 + landDuration[i]
                res = min(res, f2)
        return res
