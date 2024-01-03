#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    #BFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == newColor:
            return image

        queue = deque([(sr, sc)])
        while queue:
            row, col = queue.popleft()
            if image[row][col] == original_color:
                image[row][col] = newColor
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]):
                        queue.append((new_row, new_col))
        return image    

    # #DFS
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    #     original_color=image[sr][sc]
    #     def fill(original_color,image,sr,sc,color):
    #         if sr < 0 or sc < 0 or sr>=len(image) or sc>=len(image[0]) or image[sr][sc] != original_color or image[sr][sc]==color:
    #             return
            
    #         image[sr][sc]=color
    #         fill(original_color,image,sr+1,sc,color)
    #         fill(original_color,image,sr-1,sc,color)
    #         fill(original_color,image,sr,sc+1,color)
    #         fill(original_color,image,sr,sc-1,color)
    #     fill(original_color,image,sr,sc,color)
    #     return image
        
        
        
                
# @lc code=end

