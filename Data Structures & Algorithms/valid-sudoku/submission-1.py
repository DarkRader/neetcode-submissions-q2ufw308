class Solution:
    def isValidRows(self, board: list[list[str]]) -> bool:
        for row in board:
            seen = set()
            for elem in row:
                if elem == ".":
                    continue
                if elem in seen:
                    return False
                seen.add(elem)

        return True

    def isValidColumns(self, board: list[list[str]]) -> bool:
        for j in range(9):
            seen = set()
            for i in range(9):
                elem = board[i][j]
                if elem == ".":
                    continue
                if elem in seen:
                    return False
                seen.add(elem)

        return True

    def isValidGrids(self, board: list[list[str]]) -> bool:
        row_gap = 0
        column_gap = 0
        for x in range(3):
            for y in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        elem = board[row_gap + i][column_gap + j]
                        if elem == ".":
                            continue
                        if elem in seen:
                            return False
                        seen.add(elem)
                column_gap += 3
            row_gap += 3
            column_gap = 0

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.isValidRows(board):
            return False

        if not self.isValidColumns(board):
            return False

        if not self.isValidGrids(board):
            return False

        return True
        