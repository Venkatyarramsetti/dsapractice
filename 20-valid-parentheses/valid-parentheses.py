class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in m:
                t = st.pop() if st else '#'
                if m[char] != t:
                    return False
            else:
                st.append(char)
                
        return not st


        