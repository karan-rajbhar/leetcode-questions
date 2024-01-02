#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=0
        curr_string=""
        
        for char in s:
            if char.isdigit():
                num=num*10+int(char)
            elif char.isalpha():
                curr_string+=char
            elif char == '[':
                stack.append((num,curr_string))
                curr_string=""
                num=0
            elif char == ']':
                prev_num,prev_string=stack.pop()
                curr_string=prev_string+prev_num*curr_string
        return curr_string
                
        
                    
            
                
# @lc code=end

