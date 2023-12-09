#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start

from typing import Collection


class Solution:
    def replaceWords(self, roots, sentence):
        _trie = lambda: Collection.defaultdict(_trie)
        trie = _trie()
        END = True
        for root in roots:
            cur = trie
            for letter in root:
                cur = cur[letter]
            cur[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur: break
                cur = cur[letter]
                if END in cur:
                    return cur[END]
            return word

        return " ".join(map(replace, sentence.split()))                
# @lc code=end

