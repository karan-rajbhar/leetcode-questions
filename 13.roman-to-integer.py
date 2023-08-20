#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            0:"",
            1: "I",
            2: "II",
            3: "III",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            10: "X",
            20: "XX",
            30: "XXX",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            100: "C",
            200: "CC",
            300: "CCC",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            1000: "M",
            2000: "MM",
            3000: "MMM",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }

        
        num_list=[]
        reversed_dictionary={}
        dictionary_items=list(roman_dict.items())
        for key, value in dictionary_items[::-1]:
            reversed_dictionary[value]=key
            if value in s:
                num_list.append(value)
                s=s.replace(value,'.')
    

        num=0
        for roman_num in num_list:
            num_value = reversed_dictionary[roman_num]
            num= num+num_value

        return num


            


# @lc code=end

