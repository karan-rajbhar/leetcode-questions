#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
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

        
        numList=[]
        reversedDictionary={}
        dictionaryItems=list(romanDict.items())
        
        for key, value in dictionaryItems[::-1]:
            reversedDictionary[value]=key

            if value in s:
                numList.append(value)
                s=s.replace(value,'.')
    

        num=0
        for romanNum in numList:
            numValue = reversedDictionary[romanNum]
            num= num+numValue

        return num


            


# @lc code=end

