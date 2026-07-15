class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for pt in points:
            distance = (pt[0]*pt[0]+pt[1]*pt[1])**(1/2)
            heapq.heappush(heap, (distance, pt))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res