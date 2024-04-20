#
# @lc app=leetcode id=1992 lang=python3
#
# [1992] Find All Groups of Farmland
#

# @lc code=start
class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        def get_start_end(i,j):
            prev_row=i
            prev_column=j
            result=[i,j]

            while j < len(land[i]) -1:
                j+=1
                if land[i][j] !=1:
                    j-=1
                    break

            while i < len(land)-1:
                i+=1
                if land[i][j] != 1:
                    i-=1
                    break

            for i in range(prev_row, i+1):
                for j in range(prev_column,j+1):
                    
                    land[i][j]="#"

            result.append(i)
            result.append(j)

            return result
        farm_land=[]

        for i in range(len(land)):
            for j in range(len(land[i])):
                if land[i][j] == 1:
                    farm_land.append(get_start_end(i,j))
                    
                    
        return farm_land
                     
# @lc code=end

