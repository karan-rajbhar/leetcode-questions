#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

from typing import List
# @lc code=start       
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Define the operators
        operators = ["+", "*", "-", "/"]
        
        # Initialize an empty stack
        stack = []
        
        # Iterate over each token in the list
        for token in tokens:
            # If the token is an operator
            if token in operators:
                # If the operator is '+', pop two elements from the stack, add them and push the result back to the stack
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                
                # If the operator is '*', pop two elements from the stack, multiply them and push the result back to the stack
                if token == "*":
                    stack.append(stack.pop() * stack.pop())
                
                # If the operator is '/', pop two elements from the stack, divide the second popped element by the first one and push the result back to the stack
                if token == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                
                # If the operator is '-', pop two elements from the stack, subtract the first popped element from the second one and push the result back to the stack
                if token == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
            
            # If the token is a number, convert it to an integer and push it to the stack
            else:
                stack.append(int(token))
        
        # At the end, the stack should contain only one element, which is the result of the expression. Pop and return it.
        return stack.pop()
                
# @lc code=end

