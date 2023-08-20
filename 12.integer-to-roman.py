#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        self.roman_map = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        num=1994


        tens_place=1
        word_list=[]
        last_digit_list=[]
        while True:
            last_digit=num%10
            last_digit_list.append(last_digit*tens_place)
            tens_place = tens_place*10
            num=int(num/10)
            if num <= 0:
                break
        print(last_digit_list[::-1])        
    def returnRoman(self,num):
        if num == 0 :
            return ""
        if num in list(self.roman_map.keys()):
            return self.roman_map(num)
        

    

# @lc code=end
