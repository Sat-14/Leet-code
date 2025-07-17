class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mys=set(nums1)
        mys1=set(nums2)
        result=list(mys & mys1)
        return result
        
    