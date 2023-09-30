#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#


# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        is_negative = dividend < 0 or divisor <0
        dividend_and_divisor_negative= dividend < 0 and divisor <0

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            temp_divisor= divisor
            multiple = 1

            #if Condition fails multiply multiple by itself
            while dividend >= (temp_divisor <<1):
                temp_divisor=temp_divisor <<1
                multiple = multiple<<1
            
            dividend = dividend - temp_divisor
            result = result + multiple
        
        if dividend_and_divisor_negative:
            return  max(-2**31,min(2**31-1,result))

        if is_negative:
            return -1 * result
        
        return max(-2**31,min(2**31-1,result))






solution = Solution()
print(solution.divide(7,-3))
print(solution.divide(-1,-1))
print(solution.divide(-2147483648,-1))

# @lc code=end
