class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sums=0
        freq={0:1}
        counts=0
        for right in range(len(nums)):
            sums=sums+nums[right]
            
            diff=sums-goal
            if diff in freq:
                counts+=freq[diff]
            freq[sums]=freq.get(sums,0)+1    
        return counts        
