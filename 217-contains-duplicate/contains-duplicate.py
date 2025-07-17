class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=len(nums)
        d={}
        flag=False
        for i in range(a):
           if nums[i] in d: 
            d[nums[i]]+=1
            flag=True
            break
           else:
            d[nums[i]]=0
        return flag
