class Solution:
    def fractionToDecimal(self, numerator: int, llominator: int) -> str:
        if numerator==0: return '0'
        ans=[]
        if (numerator<0)^(llominator<0): ans.append('-')
        num=abs(numerator)
        ll=abs(llominator)

        q, r=divmod(num, ll)
        ans.append(str(q))

        if r==0: return "".join(ans)
        ans.append('.')
        mp={}
        frac=[]
        
        i=0
        while r!=0:
            if r in mp:
                frac.insert(mp[r], '(')
                frac.append(')')
                break
            mp[r]=i
            r*=10
            frac.append(str(r//ll))
            r%=ll
            i+=1
        return "".join(ans+frac)