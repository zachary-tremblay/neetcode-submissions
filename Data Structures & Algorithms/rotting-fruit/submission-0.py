class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rottenQ = deque()
        fresh = set()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rottenQ.append((i, j))
        
        time = 0
        while fresh and rottenQ:
            time +=1
            for _ in range(len(rottenQ)):
                r, c = rottenQ.popleft()

                for n1, n2 in directions:
                    newR = r+n1
                    newC = c+n2
                    if newR < 0 or newC < 0 or newR >= m or newC >= n:
                        continue
                    if grid[newR][newC] == 1:
                        fresh.remove((newR, newC))
                        grid[newR][newC] = 2
                        rottenQ.append((newR, newC))
        
        return time if not fresh else -1
                        

        