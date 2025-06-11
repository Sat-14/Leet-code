class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        length=len(nums)
        output=[]
        for i  in range(length):
            for j in range(i):
                if nums[i]+nums[j]==target:
                 output.append(i)
                 output.append(j)
                 break
                
        return output        
        