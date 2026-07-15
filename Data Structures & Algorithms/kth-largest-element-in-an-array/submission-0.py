class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        for i in range(k):
            curr = heapq.heappop(heap)
        return -curr
