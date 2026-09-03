class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) < 2:
            return s
        #build a hashmap of frequencies
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        #Store frequency and char in heap
        maxHeap = []
        for key, value in freq.items():
            heapq.heappush(maxHeap, (-value, key))
        print(maxHeap)

        res = [0] * len(s)
        previous = ""
        for i in range(len(s)):
            print(maxHeap)
            mostFreq, mostChar  = heapq.heappop(maxHeap)
            if previous != mostChar:
                previous = mostChar
                res[i] = mostChar
                if mostFreq+1 < 0:
                    heapq.heappush(maxHeap, (mostFreq+1, mostChar))
            else:
                if maxHeap:
                    extraFreq, extraChar = heapq.heappop(maxHeap)
                    previous = extraChar
                    res[i] = extraChar
                    heapq.heappush(maxHeap, (mostFreq, mostChar))
                    if extraFreq + 1 < 0:
                        heapq.heappush(maxHeap, (extraFreq+1, extraChar))
                else:
                    return ""
        return "".join(res)
