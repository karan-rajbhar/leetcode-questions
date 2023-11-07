#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) ==1 or len(num2) ==1:
            if ord(num1[0]) == 48 or ord(num2[0]) ==48:
                return "0"


        multi_array = []
        count = 0
        carry = 0
        for i in range(len(num1) - 1, -1, -1):
            multi_array.append([])
            if count > 0:
                for _ in range(count):
                    multi_array[count].append(str(0))
            for j in range(len(num2) - 1, -1, -1):
                multi = int(num1[i]) * int(num2[j])
                multi = multi + carry
                carry = 0
                if multi > 10:
                    carry = multi // 10
                    multi = multi % 10
                if j == 0:
                    multi_array[count].append(str(multi))
                    multi_array[count].append(str(carry))
                else:
                    multi_array[count].append(str(multi))

            multi_array[count].reverse()
            carry = 0
            count += 1

        last_len = len(multi_array[-1]) - 1

        for array in multi_array:
            current_len = len(array)
            required_len = last_len - current_len
            for i in range(required_len+1):
                array.insert(0,'0')
            
        
        result =[]
        carry = 0
        current_ans = 0
        for i in range(last_len ,-1,-1):
            if i == 0 and len(multi_array) !=1 and multi_array[-1][0] == 0:
                break
            for array in multi_array:
                current_ans = current_ans + int(array[i])

            current_ans = current_ans + carry
            carry = 0
            
            if current_ans >=10 and i != 0:
                
                carry = current_ans //10
                current_ans = current_ans % 10
            
            result.append(str(current_ans))
            current_ans = 0

            
        result.reverse()
        

        return ''.join(result).lstrip("0") 


# solution = Solution()
# print(solution.multiply("9", "9"))


# solution = Solution()
# print(solution.multiply("2", "3"))

# solution = Solution()
# print(solution.multiply("123", "456"))

# solution = Solution()
# print(solution.multiply("0", "0"))

# solution = Solution()
# print(solution.multiply("98", "9"))


# for i  in range(10,-1,-1):
#     for j in range(10,-1,-1):
#         print(i,j)
# @lc code=end

# 123
# *456
# -------
#   738
#  615X
# 492XX
# ------
# 56088

# 456
# x123
# ------
# 1368
# 912
# 456
