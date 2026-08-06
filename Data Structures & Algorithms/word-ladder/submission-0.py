class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        patterns = {}
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                if pattern not in patterns:
                    patterns[pattern] = [word]
                else:
                    patterns[pattern].append(word)
        
        q = deque()
        q.append(beginWord)
        dist = 1
        visited = {beginWord}
        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == endWord:
                    return dist
                for i in range(len(curr)):
                    pat = curr[:i] + '*' + curr[i+1:]
                    
                    for nei in patterns[pat]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                
            dist += 1
        
        return 0

