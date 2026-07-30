class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[0 for _ in range(n+2)] for _ in range(m+2)]
        
        # Add 0 to start and end of each existing row
        bordered = [['0'] + row + ['0'] for row in grid]

        # Add a row of zeros at top and bottom
        zero_row = ['0'] * (n + 2)
        bordered = [zero_row] + bordered + [zero_row]
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if bordered[i+1][j+1] == '1' and visited[i+1][j+1] == 0:
                    islands += 1
                    self.island(bordered, i+1, j+1, visited)
                    print(visited)

        return islands

        
    def island(self, grid: List[List[str]], i: int, j: int, visited: List[List[int]]) -> None:
        visited[i][j] = 1

        if grid[i+1][j] == '1' and visited[i+1][j] == 0:
            self.island(grid, i+1, j, visited)
        if grid[i-1][j] == '1' and visited[i-1][j] == 0:
            self.island(grid, i-1, j, visited)
        if grid[i][j+1] == '1' and visited[i][j+1] == 0:
            self.island(grid, i, j+1, visited)
        if grid[i][j-1] == '1' and visited[i][j-1] == 0:
            self.island(grid, i, j-1, visited)

        