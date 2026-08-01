class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m = len(heights)
        n = len(heights[0])

        reachedOcean = [0, 0]
        res = []

        def dfs(i ,j, height, visited):
            if i < 0 or j < 0:
                reachedOcean[0] = 1
                return
            elif i >= m or j >= n:
                reachedOcean[1] = 1
                return
            elif (i, j) in visited or heights[i][j] > height:
                return
            
            visited.add((i, j))
            for r, c in directions:
                dfs(i+r, j+c, heights[i][j], visited)
        
        for i in range(m):
            for j in range(n):
                reachedOcean = [0, 0]
                dfs(i, j, heights[i][j], set())
                if reachedOcean[0] == 1 and reachedOcean[1] == 1:
                    res.append([i, j])
        return res

