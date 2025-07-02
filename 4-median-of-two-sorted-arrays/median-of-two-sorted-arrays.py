class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        if n % 2 == 0:
            return (merged[n//2 - 1] + merged[n//2]) / 2.0
        else:
            return merged[n//2]