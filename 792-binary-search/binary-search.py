class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        n=len(nums)
        high=n-1
        while low<=high:
            mid=(low+high) // 2
            if nums[mid]==target:
                return mid
            if target<nums[mid]:
                   low=0
                   high=mid-1
            else:
                low=mid+1

        return -1        

                   
