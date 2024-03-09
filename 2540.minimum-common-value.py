class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        intersection = set(nums1).intersection(set(nums2))

        if intersection :
            return min(intersection)

        return -1
            


        