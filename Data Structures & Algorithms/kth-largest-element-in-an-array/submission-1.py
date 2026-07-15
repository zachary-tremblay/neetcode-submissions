class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [float('-infinity')]*k
        for n in nums:
            if n > heap[0]:
                heapq.heappush(heap, n)
                heapq.heappop(heap)
        return heap[0]
        
