#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
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

        for number in last_digit_list[::-1]:
            if number == 0:
                continue
            
            if number in roman_map.keys():
                word_list.append(roman_map.get(number))
                continue

            if number > 1000 :
                word_list.append('M' * (number/1000))
            elif number >500 and number < 1000:
                x=1000-number



            


    

# @lc code=end
