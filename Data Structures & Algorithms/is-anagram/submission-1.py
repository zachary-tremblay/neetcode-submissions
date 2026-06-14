class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Create 2 26 char array initialized to 0
        arr1 = [0] * 26
        arr2 = [0] * 26

        #Loop through both strings, increment index of character
        for i in range(len(s)):
            arr1[ord(s[i]) - 97] += 1
        
        for i in range(len(t)):
            arr2[ord(t[i]) - 97] += 1

        #Compare both Arrays
        for i in range(26):
            if arr1[i] != arr2[i]:
                return False
        return True