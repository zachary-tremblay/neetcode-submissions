class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        mostFreq = 0
        frequency = {}
        r = 0
        l = 0

        for c in s:
            if c not in frequency:
                frequency[c] = 1
            else:
                frequency[c] += 1
            mostFreq = max(frequency[c], mostFreq)

            while (r - l - mostFreq + 1) > k:
                frequency[s[l]] -= 1
                l += 1
            maxLength = max(r - l + 1, maxLength)
            r += 1
            
        return maxLength

                

            
