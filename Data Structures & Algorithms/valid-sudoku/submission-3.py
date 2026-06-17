class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for i in range(9)]
        columns = [[] for i in range(9)]
        boxes = [[[] for i in range(3)] for i in range(3)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if value in rows[i] or value in columns[j] or value in boxes[i//3][j//3]:
                    return False
                else:
                    rows[i].append(value)
                    columns[j].append(value)
                    boxes[i//3][j//3].append(value)
        return True