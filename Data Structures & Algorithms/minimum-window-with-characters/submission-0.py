class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        tDict = {}
        sDict = {}
        minSubLen = float("infinity")
        res = ""

        for c in t:
            tDict[c] = tDict.get(c, 0) + 1

        need = len(tDict)
        have = 0
        l = 0
        for r in range(len(s)):
            sDict[s[r]] = sDict.get(s[r], 0) + 1

            if s[r] in tDict and sDict[s[r]] == tDict[s[r]]:
                have += 1
            
            while have == need:
                minSubLen = min(r - l + 1, minSubLen)
                if minSubLen == r - l + 1:
                    res = s[l:r+1]
                sDict[s[l]] -= 1
                if s[l] in tDict and sDict[s[l]] < tDict[s[l]]:
                    have -= 1
                l += 1
        return res

        

       
        
        

        

        
