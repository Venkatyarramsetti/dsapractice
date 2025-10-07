class Solution:
    def avoidFlood(self, r: List[int]) -> List[int]:
        answer, l, l1 = [-1]*len(r), {}, SortedList()
        for i, n in enumerate(r):
            if n == 0:
                l1.add(i)
                answer[i] = 1
            elif n in l:
                j = l1.bisect_right(l[n])
                if j == len(l1):
                    return []
                answer[l1[j]] = n
                l1.pop(j)
                l[n] = i
            else:
                l[n] = i
        return answer