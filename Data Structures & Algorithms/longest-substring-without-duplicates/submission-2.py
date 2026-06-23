class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currLength = 0
        maxLength = 0
        currSub = []

        for i in range(len(s)):
            print(currSub)
            if s[i] not in currSub:
                currSub.append(s[i])
                currLength += 1
                if currLength > maxLength:
                    maxLength = currLength
            else:
                currSub.append(s[i])
                currSub = currSub[currSub.index(s[i])+1::]
                currLength = len(currSub)
        return maxLength
            