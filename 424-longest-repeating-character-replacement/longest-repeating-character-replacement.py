class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={}
        left,maxLen,nM=0,0,0
        maxv=0
        maxf=0
        diff=0

        for right in range(len(s)):
            counts[s[right]]=counts.get(s[right],0)+1
            maxv=max(counts,key=counts.get)
            maxf=max(counts.values())
            total_sum=sum(counts.values())
            diff=total_sum-maxf
            while diff >k:
                counts[s[left]]-=1
                left+=1
                diff=sum(counts.values())-max(counts.values())
            maxLen=max(maxLen,right-left+1)
        return maxLen        



            
        
             
            

