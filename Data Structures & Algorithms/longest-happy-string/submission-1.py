class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0:
            heapq.heappush(maxHeap, (-a, "a"))
        if b > 0:
            heapq.heappush(maxHeap, (-b, "b"))
        if c > 0:
            heapq.heappush(maxHeap, (-c, "c"))


        total = a+b+c
        res = [""] * total
        prev1 = ""
        prev2 = ""
        i = -1
        while maxHeap:
            i += 1
            currCount, currChar = heapq.heappop(maxHeap)
            if prev2 != currChar or (prev2 == currChar and prev1 != currChar):
                res[i] = currChar
                prev1 = prev2
                prev2 = currChar
                if currCount + 1 < 0:
                    heapq.heappush(maxHeap, (currCount+1, currChar))
            else:
                print("here2")
                if maxHeap:
                    extraCount, extraChar = heapq.heappop(maxHeap)
                    res[i] = extraChar
                    prev1 = prev2
                    prev2 = extraChar
                    heapq.heappush(maxHeap, (currCount, currChar))
                    if extraCount + 1 < 0:
                        heapq.heappush(maxHeap, (extraCount+1, extraChar))
                else:
                    return "".join(res)
        return "".join(res)
