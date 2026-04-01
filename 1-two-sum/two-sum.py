class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=len(nums)
        m={}
        for i in range(a):
         
         cc=target-nums[i]
         if cc in m:
            return [m[cc],i]
         m[nums[i]]=i         
         
            
            
