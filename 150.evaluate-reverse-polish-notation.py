#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=["+","*","-","/"]
        stack=[]
        for token in tokens:            
            if token in operators:
                if token == "+":
                    stack.append(stack.pop()+stack.pop())
                    
                if token =="*":
                    stack.append(stack.pop()*stack.pop())
                    
                if token == "/":
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b/a))
                    
                if token == "-":
                    a,b=stack.pop(),stack.pop()
                    stack.append(b-a)
                    
            else:
                stack.append(int(token))
                
        return stack.pop()
        
                
# @lc code=end

