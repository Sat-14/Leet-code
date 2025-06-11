class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        c=set()
        left=0
        maxl=0
        for right in range(n):
            if s[right]  not in c:
                c.add(s[right])
                maxl=max(right-left+1,maxl)
            else:
                while s[right] in c:
                 c.remove(s[left])
                 left+=1
                c.add(s[right]) 
                maxl=max(right-left+1,maxl)
        return maxl        


        

