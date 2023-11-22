#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random

class RandomizedSet:

    def __init__(self):
        self.nums=[]
        self.dict={}
        
    def insert(self, val: int) -> bool:
        
        if val not in self.dict:
            self.nums.append(val)
            self.dict[val]=len(self.nums)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        
        if val in self.dict:
            index=self.dict[val]
            last= self.nums[-1]
            self.nums[index]=last
            self.dict[last]=index
            self.nums.pop()
            self.dict.pop(val,0)
            return True
        
        return False
            
        
        

    def getRandom(self) -> int:
        
        return random.choice(self.nums)
        
        
        
        



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(1)
# param_2 = obj.remove(2)
# param_3=obj.insert(2)
# param_3 = obj.getRandom()
# param_4= obj.remove(1)
# param_5=obj.insert(2)
# param_6=obj.getRandom()

# print(param_1,param_2,param_3,param_4,param_5,param_6)
# @lc code=end

