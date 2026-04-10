class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        freq={}
        r=[]
        for i in range(len(nums)):
            
            t=target-nums[i]
            if t in freq:
                r.append(i)
                r.append(freq[t])
            freq[nums[i]]=i    
            if len(r)==2:
                return r    


            
            
