class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        a=len(s)
        maxx=0
        for i in range(a):
            fast=i
            m={}
            for fast in range(i,a):
                
                
                if s[fast] in m:
                    
                    break

                m[s[fast]]=1
                maxx=max(maxx,fast-i+1) 
        return maxx            
                

