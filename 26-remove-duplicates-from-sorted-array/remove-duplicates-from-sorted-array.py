from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        unique=[]
        for  x in nums:
            if x not in seen:
                seen.add(x)
                unique.append(x)

        k=len(unique)
        
        nums[:k]=unique
        return k