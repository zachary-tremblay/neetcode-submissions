class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stn in stones:
            heapq.heappush(heap, -stn)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, -abs(x-y))
        return -heap[0] if heap else 0
