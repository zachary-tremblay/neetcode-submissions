class Solution:

    def encode(self, strs: List[str]) -> str:
        
        words = ""
        lengths = ""
        for n in strs:
            words += n
            lengths += str(len(n))
            lengths += "#"
        encoded = lengths + "$" + words
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        lengths = s[:s.find("$")]
        SplitLen = lengths.split("#")[:-1]
        words = s[s.find("$")+1:]

        decoded = []
        startIndex = 0
        for n in SplitLen:
            n = int(n)
            decoded.append(words[startIndex:startIndex + n])
            startIndex += n

        return decoded
        