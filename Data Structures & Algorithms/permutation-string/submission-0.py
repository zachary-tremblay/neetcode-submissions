class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #build frequency dict

        s1Dict = {}
        s2Dict = {}
        s1Length = len(s1)
        subLen = 0
        l = 0

        for c in s1:
            s1Dict[c] = s1Dict.get(c, 0) + 1

        
        for c in s2:
            s2Dict[c] = s2Dict.get(c, 0) + 1
            subLen += 1

            if subLen > s1Length:
                if s2Dict[s2[l]] > 1:
                    s2Dict[s2[l]] -= 1
                else:
                    del s2Dict[s2[l]]
                l += 1
                subLen -= 1
                
            if s1Dict == s2Dict:
                return True
        
        return False