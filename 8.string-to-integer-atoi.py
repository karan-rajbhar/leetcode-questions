#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()

        if s=='':
            return 0
        
        sign=""
        numberList=[]
        
        if s[0] == '-' or s[0] == "+":
            sign=s[0]
        
        for index in range(0,len(s)):
            if sign!='' and index == 0:
                continue
            
            if not s[index].isnumeric() or s[index] == '+' or s[index]=='-':
                break
            
            numberList.append(s[index])
        if sign=="" and numberList:
            final_number = int(''.join(numberList))
        elif numberList and (sign== '+' or sign =='-') :        
            final_number = int(sign+''.join(numberList))
        else:
            return 0 
        if final_number > 2**31-1:
            final_number = 2**31-1
        if final_number < -2**31:
            final_number = -2**31
        return final_number
# @lc code=end

