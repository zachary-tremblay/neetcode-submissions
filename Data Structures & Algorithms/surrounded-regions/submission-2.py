class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[-1, 0], [1,0], [0, -1], [0, 1]]
        m = len(board)
        n = len(board[0])

        #find all O's on the edge, intitiate a stack + visited grid
        stack = []
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(n):
            if board[0][i] == 'O':
                stack.append((0, i))
        for i in range(n):
            if board[m-1][i] == 'O':
                stack.append((m-1, i))
        for i in range(m-2):
            if board[i+1][0] == 'O':
                stack.append((i+1, 0))
        for i in range(m-2):
            if board[i+1][n-1] == 'O':
                stack.append((i+1, n-1))
        
        
        while stack:
            for _ in range(len(stack)):
                i, j = stack.pop()
                visited[i][j] = 1
                for n1, n2 in directions:
                    r, c = i+n1, j+n2
                    if r < 0 or r >=m or c < 0 or c >= n or visited[r][c] == 1:
                        continue
                    if board[r][c] == 'O':
                        stack.append((r, c))
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    board[i][j] = 'X'

        
