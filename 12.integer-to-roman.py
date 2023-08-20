#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            0:"",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            20: "XX",
            30: "XXX",
            40: "XL",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: "XC",
            100: "C",
            200: "CC",
            300: "CCC",
            400: "CD",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: "CM",
            1000: "M",
            2000: "MM",
            3000: "MMM",
        }
        tens_place=1
        wordList=[]
        while num > 0:
            last_digit=num%10
            last_digit_place = last_digit*tens_place 
            wordList.append(roman_dict[last_digit_place])
            tens_place = tens_place*10
            num=int(num/10)
            
        return ''.join(wordList[::-1])

# @lc code=end
