class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n=len(nums)
        low=0
        high=n-1
        x=target
        left=bisect.bisect_left(nums,x)
        right=bisect.bisect_right(nums,x)-1
        if left>right:
            return [-1,-1]
        else:
            return [left,right]    
