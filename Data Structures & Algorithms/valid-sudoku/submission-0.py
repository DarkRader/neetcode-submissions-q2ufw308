class Solution:
    def checkCountValid(self, num_count: list[int], elem: str):
        elem_num = int(elem) - 1
        num_count[elem_num] += 1
        if num_count[elem_num] > 1:
            return False
        return True

    def isValidRows(self, board: list[list[str]]) -> bool:
        for row in board:
            num_count = [0] * 9
            for elem in row:
                if elem == ".":
                    continue
                if not self.checkCountValid(num_count, elem):
                    return False

        return True

    def isValidColumns(self, board: list[list[str]]) -> bool:
        for j in range(9):
            num_count = [0] * 9
            for i in range(9):
                elem = board[i][j]
                if elem == ".":
                    continue
                if not self.checkCountValid(num_count, elem):
                    return False

        return True

    def isValidGrids(self, board: list[list[str]]) -> bool:
        row_gap = 0
        column_gap = 0
        for x in range(3):
            for y in range(3):
                num_count = [0] * 9
                for i in range(3):
                    for j in range(3):
                        elem = board[row_gap + i][column_gap + j]
                        if elem == ".":
                            continue
                        if not self.checkCountValid(num_count, elem):
                            return False
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
        