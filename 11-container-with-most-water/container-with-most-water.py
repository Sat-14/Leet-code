class Solution:
    def maxArea(self, height: List[int]) -> int:
       l=0
       k=len(height)
       r=k-1
       ma=0
       while r>l:
        h1=height[l]
        h2=height[r]
        width=min(height[l],height[r])
        length=r-l
        ma=max(ma,length*width)
        if height[l]<height[r]:
            l=l+1
        else:
            r=r-1
       return ma         


        
       
