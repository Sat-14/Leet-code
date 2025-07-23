class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<=1:
            return True
        count=0    
        for i in range(1,n):
            if(nums[i]<nums[i-1]):
                count+=1
        if(nums[n-1]>nums[0]):
            count+=1
        if(count<2):
            return True
        else:
            return False            
