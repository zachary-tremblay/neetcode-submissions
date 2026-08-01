class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rottenQ = deque()
        fresh = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rottenQ.append((i, j))
        
        time = 0
        while fresh !=0 and rottenQ:
            time +=1
            for _ in range(len(rottenQ)):
                r, c = rottenQ.popleft()

                for n1, n2 in directions:
                    newR = r+n1
                    newC = c+n2
                    if newR < 0 or newC < 0 or newR >= m or newC >= n:
                        continue
                    if grid[newR][newC] == 1:
                        fresh -= 1
                        grid[newR][newC] = 2
                        rottenQ.append((newR, newC))
        
        return time if fresh == 0 else -1
                        

        