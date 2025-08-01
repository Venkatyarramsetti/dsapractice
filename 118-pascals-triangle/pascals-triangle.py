from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list1 = [] 
        for i in range(numRows):
            list1.append([1])  
            for j in range(1, i):
                list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
            if i > 0:
                list1[i].append(1)
        return list1
