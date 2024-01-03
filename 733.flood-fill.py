#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
from typing import List
# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color=image[sr][sc]
        def fill(original_color,image,sr,sc,color):
            if sr < 0 or sc < 0 or sr>=len(image) or sc>=len(image[0]) or image[sr][sc] != original_color or image[sr][sc]==color:
                return
            
            image[sr][sc]=color
            fill(original_color,image,sr+1,sc,color)
            fill(original_color,image,sr-1,sc,color)
            fill(original_color,image,sr,sc+1,color)
            fill(original_color,image,sr,sc-1,color)
        fill(original_color,image,sr,sc,color)
        return image
        
        
        
                
# @lc code=end

