class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=""
        m=""
        a=len(s)
        if(s==" "):
         return True
        for i in s:
            
            if i.isalnum():
             k=i.lower()+k
             m=m+i.lower()
        if(k==m and a!=0):
            return True
        return False        