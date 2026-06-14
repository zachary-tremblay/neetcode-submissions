class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap, key is array of count of characters to a tuple, value is list of anagrams
        hm = {}

        #iterate through strs
        #for each get the array of count of chars
        for i in range(len(strs)):
            arr = [0] * 26
            for j in range(len(strs[i])):
                arr[ord(strs[i][j]) - ord("a")] += 1
            t = tuple(arr)
            #if DNE, add it to hashmap, if it does, add it to list in hashmap
            if t in hm:
                hm[t].append(strs[i])
            else:
                hm[t] = [strs[i]]
        
        return list(hm.values())