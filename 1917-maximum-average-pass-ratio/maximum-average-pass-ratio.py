class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n=len(classes)
        sum=0
        l=[]
        for p,q in classes:
            sum+=p/q
            l.append(((p-q)/(q*(q+1)), p, q))

        heapify(l)

        for _ in range(extraStudents):
            (r, p, q)=l[0]
            if r==0: break
            sum-=r 
            r2=(p-q)/((q +1.0)* (q + 2.0))
            heapreplace(l, (r2, p+1, q+1))
        return sum/n