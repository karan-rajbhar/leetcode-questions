#
# @lc app=leetcode id=2718 lang=python3
#
# [2718] Sum of Matrix After Queries
#
from typing import List
# @lc code=start
class Solution:
    #Solution 2: Optimized
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        col_visited=set()
        row_visited=set()
        total_sum=0

        for i in reversed(range(len(queries))):

            type,index,val=queries[i]

            if type==0:
                if index not in row_visited:
                    row_visited.add(index)
                    total_sum +=val*(n-len(col_visited))
            if type==1:
                if index not in col_visited:
                    col_visited.add(index)
                    total_sum +=val*(n-len(row_visited))
        return total_sum



    #Solution 1: Brute Force
    def matrixSumQueries1(self, n: int, queries: List[List[int]]) -> int:
        init_matrix=[ [0]*n for i in range(n)]
        total_sum=0
        for query in queries:
            type,index,val=query[0],query[1],query[2]

            if type==0:
                total_sum -= sum(init_matrix[index])
                init_matrix[index]=[val]*n
                total_sum += val*n
            if type == 1:
                for i in range(n):
                    total_sum -= init_matrix[i][index]
                    init_matrix[i][index]=val
                    total_sum += val

        return total_sum      
        
# @lc code=end

