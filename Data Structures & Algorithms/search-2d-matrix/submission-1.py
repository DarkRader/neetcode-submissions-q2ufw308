class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l_list, r_list = 0, rows * cols - 1
        while l_list <= r_list:
            middle = l_list + (r_list - l_list) // 2
            row, col = middle // cols, middle % cols
            if matrix[row][col] < target:
                l_list = middle + 1
            elif matrix[row][col] > target:
                r_list = middle - 1
            else:
                return True

        return False