class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for m in nums:
            heapq.heappush(heap,m)
            if len(heap)>k:
                heapq.heappop(heap)

        return heap[0]        