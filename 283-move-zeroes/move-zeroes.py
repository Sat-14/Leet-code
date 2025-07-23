class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=len(nums)
        left=0
        if k>1 and 0 in nums:
            for right in range(1,k):
                if(nums[left]==0 and nums[right]!=0):
                    nums[left],nums[right]=nums[right],nums[left]
                    left+=1
                elif(nums[left]!=0):
                    left+=1

                    
                    
