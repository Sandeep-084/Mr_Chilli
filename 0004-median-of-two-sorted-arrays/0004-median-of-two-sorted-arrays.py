class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = nums1 + nums2
        n = len(k)
        k.sort()
        if(n%2!=0):
                q = (n)//2
                p = k[q]
                return float(p)
        else:
                q = (n)//2
                p = (n-2)//2
                e = k[p]+k[q]
                return float(e/2.0) 