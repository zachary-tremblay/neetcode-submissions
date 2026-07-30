class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1 , 0],[-1 , 0],[0 , 1],[0 , -1]]
        m, n = len(grid), len(grid[0])
        maxArea = [0]
        currentArea = [0]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return
            currentArea[0] += 1
            maxArea[0] = max(maxArea[0], currentArea[0])
            grid[i][j] = 0
            for n1, n2 in directions:
                    dfs(i+n1, j+n2)

        for i in range(m):
            for j in range(n):
                currentArea[0] = 0
                if grid[i][j]:
                    dfs(i, j)
        return maxArea[0]
            

