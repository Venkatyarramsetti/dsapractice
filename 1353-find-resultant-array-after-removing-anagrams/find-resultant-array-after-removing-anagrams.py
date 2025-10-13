class Solution:
    def removeAnagrams(self, w: List[str]) -> List[str]:
        ans = [w[0]]   
        for i in range(1, len(w)):
            if Counter(w[i]) != Counter(ans[-1]):
                ans.append(w[i])
        return ans