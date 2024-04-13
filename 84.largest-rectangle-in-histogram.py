#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def get_prev_smallest():
            stack=[]
            prev_smallest=[-1]*len(heights)
            for i in range(len(heights)):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    prev_smallest[i]=stack[-1]
                stack.append(i)

            return prev_smallest


        def get_next_smallest():
            stack=[]
            n = len(heights)
            next_smallest=[n]*len(heights)
            for i in range(len(heights)-1,-1,-1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    next_smallest[i]=stack[-1]
                stack.append(i)
            
            return next_smallest

    
        prev_smallest=get_prev_smallest()
        next_smallest=get_next_smallest()
        
        max_area=0
        for i in range(len(heights)):
            area = heights[i] * (next_smallest[i] - prev_smallest[i] - 1)
            max_area = max(max_area,  area )

        return max_area         
# @lc code=end

solution = Solution()
print(solution.largestRectangleArea([4,2,1,5,6,3,2,4,2]))
