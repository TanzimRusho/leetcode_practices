from typing import List
from collections import deque

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # each row traverse
        n = len(matrix)
        count = 0
        min_ = 100001
        sum_ = 0
        
        for i in range(0, n):
            for j in range(0, n):
                if matrix[i][j] < 0:
                    count += 1
                
                x = abs(matrix[i][j])
                if x < min_: 
                    min_ = x
                sum_ +=  x
        
        print(min_)
        
        if count % 2 == 0:
            return sum_
        else:    
            return sum_ - 2*min_ 
        

sn = Solution()    
print(sn.maxMatrixSum([[-56261,-15288,-59083,-14357,-15751],
[-48494,-32094,-87818,-33356,-16991],
[-72395,-48735,-21856,-30471,-80400],
[-33852,-17577,-88317,-59620,-94630],
[-69472,-40030,-26429,-69577,-31498]]))


