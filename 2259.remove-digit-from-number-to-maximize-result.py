#
# @lc app=leetcode id=2259 lang=python3
#
# [2259] Remove Digit From Number to Maximize Result
#

# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        index_list=[]
        for i in range(0, len(number)):
            if number[i]==digit:
                index_list.append(i)

        result=number.replace(digit, '' ,1)

        for i in range(len(index_list)):
            list_text= list(number)
            del list_text[index_list[i]]
            new_num ="".join(list_text)

            if int(result) < int(new_num):
                result= new_num
        return result        
# @lc code=end

