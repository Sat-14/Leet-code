class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        c=0
        for i in nums:
            if(i==1):
                c+=1
                if(res<c):
                    res=c
            else:
                
                c=0
        return res                