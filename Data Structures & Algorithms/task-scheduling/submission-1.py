class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] -= 1
        
        
        heap = []
        for cnt in freq:
            if cnt != 0:
                heapq.heappush(heap, cnt)
        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while heap or q:
            time += 1

            if not heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
