#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
import sys
from typing import List
from itertools import combinations


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_num = sys.maxsize
        for i in range(len(nums) - 2):
            first_pointer = i + 1
            second_pointer = len(nums) - 1

            while first_pointer < second_pointer:
                sum = nums[i] + nums[first_pointer] + nums[second_pointer]
                
                if abs(target - sum) < abs(target - closest_num):
                    closest_num = sum

                if sum > target:
                    second_pointer = second_pointer - 1
                else:
                    first_pointer = first_pointer + 1

        return closest_num


    ## this solution exced time limit
    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        closest = None

        if len(nums) == 3:
            return sum(nums[:3])

        for x, y, z in combinations(nums, 3):
            total = x + y + z
            if closest is None:
                closest = total

            if total == target:
                return target

            diff1 = abs(target - total)
            diff2 = abs(target - closest)

            if diff1 < diff2:
                closest = total

        return closest


solution = Solution()
array = [
    -254,
    302,
    422,
    810,
    290,
    117,
    622,
    988,
    -803,
    -773,
    -400,
    -389,
    196,
    836,
    -219,
    -902,
    455,
    -962,
    956,
    528,
    -901,
    -963,
    919,
    925,
    -455,
    548,
    -56,
    840,
    -873,
    267,
    431,
    758,
    413,
    665,
    -784,
    179,
    167,
    536,
    205,
    -493,
    -263,
    -538,
    965,
    861,
    -303,
    -919,
    764,
    946,
    -751,
    498,
    746,
    829,
    312,
    -680,
    692,
    -446,
    -636,
    412,
    -708,
    -607,
    426,
    -415,
    676,
    -146,
    213,
    432,
    -379,
    -454,
    -135,
    171,
    -627,
    471,
    160,
    382,
    892,
    844,
    885,
    720,
    -347,
    -77,
    604,
    111,
    400,
    -749,
    -399,
    -422,
    706,
    -539,
    264,
    -116,
    -913,
    -476,
    801,
    -490,
    916,
    -772,
    -21,
    697,
    -860,
    -41,
    -818,
    -175,
    -472,
    143,
    -464,
    736,
    185,
    -624,
    553,
    -731,
    -182,
    688,
    21,
    886,
    -258,
    -871,
    104,
    110,
    61,
    821,
    -81,
    638,
    -279,
    -641,
    3,
    -252,
    -48,
    995,
    825,
    -509,
    -570,
    -710,
    215,
    -130,
    415,
    32,
    -97,
    291,
    814,
    944,
    785,
    -205,
    -233,
    48,
    257,
    -907,
    268,
    -142,
    -271,
    -307,
    -1,
    -715,
    989,
    -942,
    -617,
    -250,
    -371,
    -353,
    -433,
    30,
    -982,
    258,
    -120,
    338,
    -984,
    543,
    -899,
    768,
    -221,
    817,
    -394,
    -649,
    -566,
    994,
    515,
    826,
    -232,
    178,
    -68,
    -489,
    -808,
    778,
    -958,
    952,
    -463,
    786,
    -460,
    -580,
    -560,
    56,
    -14,
    360,
    787,
    180,
    813,
    -108,
    715,
    216,
    762,
    -261,
    918,
    479,
    364,
    212,
    -273,
    470,
    -646,
    -50,
    567,
    574,
    248,
    781,
    815,
    -857,
    -842,
    172,
    -785,
    -496,
    -469,
    893,
    795,
    896,
    752,
    -602,
    186,
    -698,
    74,
    31,
    362,
    -69,
    -915,
    353,
    323,
    554,
    -683,
    239,
    811,
    350,
    -815,
    222,
    8,
    223,
    -917,
    602,
    428,
    321,
    -741,
    -943,
    502,
    478,
    463,
    194,
    753,
    -22,
    537,
    -512,
    949,
    390,
    852,
    766,
    29,
    355,
    262,
    -164,
    -114,
    313,
    -908,
    34,
    388,
    -72,
    -864,
    -471,
    -810,
    198,
    -629,
    774,
    91,
    -960,
    583,
    -366,
    -468,
    -361,
    -884,
    -718,
    -200,
    -253,
    943,
    -212,
    -283,
    396,
    870,
    798,
    448,
    -203,
    73,
    -373,
    -214,
    492,
    -349,
    866,
    367,
    -499,
    462,
    304,
    -809,
    116,
    376,
    156,
    832,
    45,
    978,
    -421,
    446,
    -684,
    -743,
    833,
    15,
    -105,
    -475,
    -583,
    -213,
    243,
    -632,
    684,
    -336,
]
print(solution.threeSumClosest(array, 5436))


# @lc code=end
