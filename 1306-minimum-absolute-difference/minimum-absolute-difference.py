class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        l = []
        arr.sort()
        m = min(abs(arr[i] - arr[i-1]) for i in range(1,len(arr)))
        for i in range(1,len(arr)):
            k = abs(arr[i] - arr[i-1])
            if k <= m:
                m = k
                l.append([arr[i-1],arr[i]])
        return l