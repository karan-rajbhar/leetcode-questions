class Solution(object):

    #time complexity O(min(n+m)) space complexity O(n)
    # def getCommon(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: int
    #     """
    #     intersection = set(nums1).intersection(set(nums2))

    #     if intersection :
    #         return min(intersection)

    #     return -1

    #time complexity O(nlogn + mlogm) space complexity O(1)
    
    def getCommon(self, nums1, nums2):
        i , j = 0 , 0
        while i < len(nums1) and j <len(nums2):
            
            if nums1[i] == nums2[j]:
                return nums1[i]

            if nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1

        return -1
 



        