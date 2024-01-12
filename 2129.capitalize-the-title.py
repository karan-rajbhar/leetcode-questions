#
# @lc app=leetcode id=2129 lang=python3
#
# [2129] Capitalize the Title
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        #split the string into words
        words = title.split(" ")
        #create an empty list to store the capitalized words
        capitalized_words = []
        #loop through the words
        for word in words:
            #capitalize the first letter of each word
            if len(word) <=2:
                capitalized_words.append(word.lower())
            else:
                capitalized_words.append(word.capitalize())
        #join the words
        return " ".join(capitalized_words)

# solution=Solution()
# print(solution.capitalizeTitle("First leTTeR of EACH Word"))
        
# @lc code=end

