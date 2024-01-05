#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
import heapq
from typing import List
from collections import Counter
from heapq import heapify

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        result=[]
        min_heap=[(-freq , word) for word, freq in count.items()]

        heapify(min_heap)
        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result


    #using list and dict
    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        dict={}
        for word in words:
            if word in dict:
                dict[word]=dict[word]+1
            else:
                dict[word]=1
        list= [(k,v) for k,v in dict.items()]

        list.sort(key=lambda x: (-x[1],x[0]))

        return [x[0] for x in list[:k]]

# solution = Solution()
# solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
# @lc code=end

