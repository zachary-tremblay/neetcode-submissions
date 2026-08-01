class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m = len(grid)
        n = len(grid[0])
        distance = 0


        def dfs(i , j, distance):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == -1 or distance > grid[i][j]:
                return

            grid[i][j] = min(grid[i][j], distance)
            
            for r, c in directions:
                dfs(i+r, j+c, distance+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
