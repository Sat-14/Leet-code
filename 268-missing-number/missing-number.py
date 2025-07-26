class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r1=0
        r2=0
        a=len(nums)
        for k in nums:
            r1^=k
        for j in  range(1,a+1):
            r2^=j
        return r1^r2       

        