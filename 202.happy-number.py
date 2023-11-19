#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        dict_nums={}
        num=n
        while True:

            if dict_nums.get(num,None):
                return False
            dict_nums[num]=True
            digits= self.getDigits(num)
            num= self.squared_sum(digits)
            
            if num ==1:
                return True
            
        
        
    
    def getDigits(self,n):
        digits=[]
        while True:
            digit=n%10
            digits.append(digit)
            n=n//10
            if n <=9:
                digits.append(n)
                break
        digits.reverse()
        return digits
    
    def squared_sum(self, digits):
        sum=0
        for num in digits:
            sum=sum+num*num
        
        return sum
    
# solution = Solution()
# print(solution.isHappy(19))        
# @lc code=end

