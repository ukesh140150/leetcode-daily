class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3= nums1 + nums2 
        m=len(nums1)
        n=len(nums2)
        o = m+n 
        count=0
        for x in nums3 :
            count+=x
        return count/o  
